"""Check the bundled OpenAPI definitions.

For both ogcapi-environmental-data-retrieval-1-oas30.bundled.json and
-oas31.bundled.json this checks that
  - every local $ref resolves, both against the document root and when a
    schema with its own $id is treated as a separate resource;
  - no component name ends in -2, -3, ... (the bundler renames one of two
    different schemas that share a file name).
For the OpenAPI 3.1 bundle it also checks that the CoverageJSON schemas accept
a set of valid CoverageJSON documents and reject a set of invalid ones. (The
OpenAPI 3.0 CoverageJSON schemas are hand-written and are not checked yet.)

Usage:
  python3 check_openapi_bundles.py [DIR] [--canonical SOURCE]
DIR holds the two bundles (default: current directory). With --canonical,
each sample is also validated against the canonical CoverageJSON schema
(path or URL, e.g. https://schemas.opengis.net/covjson/1.0/coveragejson.json)
to confirm the expected results. Requires jsonschema. Exits 1 on any failure.
"""
import argparse
import collections
import copy
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request

from jsonschema import Draft7Validator, Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

T0, T1 = "2026-09-30T00:00:00Z", "2026-09-30T01:00:00Z"
GEO = {"coordinates": ["x", "y"],
       "system": {"type": "GeographicCRS", "id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"}}
TIME = {"coordinates": ["t"], "system": {"type": "TemporalRS", "calendar": "Gregorian"}}
VERT = {"coordinates": ["z"], "system": {"type": "VerticalCRS"}}
SQUARE = [[[0, 0], [1, 0], [1, 1], [0, 0]]]
SQUARE2 = [[[2, 2], [3, 2], [3, 3], [2, 2]]]
PARAMETERS = {"t2m": {"type": "Parameter", "observedProperty": {"label": {"en": "Air temperature"}},
                      "unit": {"symbol": "K"}}}


def domain(domain_type, axes, referencing=(GEO, TIME)):
    d = {"type": "Domain", "axes": axes, "referencing": list(referencing)}
    if domain_type:
        d["domainType"] = domain_type
    return d


def coverage(dom, ranges=None, parameters=PARAMETERS):
    c = {"type": "Coverage", "domain": dom,
         "ranges": ranges or {"t2m": {"type": "NdArray", "dataType": "float", "values": [283.1]}}}
    if parameters is not None:
        c["parameters"] = parameters
    return c


def tuples(coords, values):
    return {"dataType": "tuple", "coordinates": coords, "values": values}


def polygons(values):
    return {"dataType": "polygon", "coordinates": ["x", "y"], "values": values}


def ndarray(data_type, values, **kw):
    return {"type": "NdArray", "dataType": data_type, "values": values, **kw}


# (name, document, expected to be valid) - validated against the top-level
# CoverageJSON schema; NdArray samples are also validated against the ndArray
# schema on its own.
SAMPLES = [
    # NdArray
    ("NdArray 0-D float", ndarray("float", [1.5]), True),
    ("NdArray 1-D float with null", ndarray("float", [1.5, None, 2.0], axisNames=["t"], shape=[3]), True),
    ("NdArray 2-D float", ndarray("float", [1.5, 2.5], axisNames=["y", "x"], shape=[1, 2]), True),
    ("NdArray 1-D integer", ndarray("integer", [1, 2], axisNames=["t"], shape=[2]), True),
    ("NdArray 0-D integer", ndarray("integer", [7]), True),
    ("NdArray 1-D string", ndarray("string", ["a", "b"], axisNames=["t"], shape=[2]), True),
    ("NdArray all null", ndarray("float", [None, None], axisNames=["t"], shape=[2]), True),
    ("NdArray float type, string values", ndarray("float", ["x"]), False),
    ("NdArray integer type, float values", ndarray("integer", [1.5]), False),
    ("NdArray 2 values without shape/axisNames", ndarray("float", [1.0, 2.0]), False),
    ("NdArray empty values", ndarray("float", []), False),
    # Domains, one per domain type
    ("Domain Grid", domain("Grid", {"x": {"values": [1.0, 2.0, 3.0]}, "y": {"start": 50, "stop": 51, "num": 2},
                                    "t": {"values": [T0]}}), True),
    ("Domain Trajectory", domain("Trajectory", {"composite": tuples(["t", "x", "y"], [[T0, 1, 2], [T1, 1.5, 2.5]]),
                                                "z": {"values": [10]}}), True),
    ("Domain VerticalProfile", domain("VerticalProfile", {"x": {"values": [1]}, "y": {"values": [2]},
                                                          "z": {"values": [10, 20, 30]}, "t": {"values": [T0]}},
                                      (GEO, VERT, TIME)), True),
    ("Domain Point", domain("Point", {"x": {"values": [1]}, "y": {"values": [2]}, "t": {"values": [T0]}}), True),
    ("Domain PointSeries", domain("PointSeries", {"x": {"values": [1]}, "y": {"values": [2]},
                                                  "t": {"values": [T0, T1]}}), True),
    ("Domain MultiPoint", domain("MultiPoint", {"composite": tuples(["x", "y"], [[1, 2], [3, 4]])}), True),
    ("Domain MultiPointSeries", domain("MultiPointSeries", {"composite": tuples(["x", "y"], [[1, 2], [3, 4]]),
                                                            "t": {"values": [T0, T1]}}), True),
    ("Domain Section", domain("Section", {"composite": tuples(["t", "x", "y"], [[T0, 1, 2], [T1, 3, 4]]),
                                          "z": {"values": [10, 20]}}, (GEO, VERT, TIME)), True),
    ("Domain Polygon", domain("Polygon", {"composite": polygons([SQUARE]), "t": {"values": [T0]}}), True),
    ("Domain PolygonSeries", domain("PolygonSeries", {"composite": polygons([SQUARE]),
                                                      "t": {"values": [T0, T1]}}), True),
    ("Domain MultiPolygon", domain("MultiPolygon", {"composite": polygons([SQUARE, SQUARE2])}), True),
    ("Domain MultiPolygonSeries", domain("MultiPolygonSeries", {"composite": polygons([SQUARE, SQUARE2]),
                                                                "t": {"values": [T0, T1]}}), True),
    ("Domain without domainType", domain(None, {"foo": {"values": ["a", "b"]}}), True),
    ("Domain with custom domainType", domain("Custom", {"foo": {"values": [1, 2]}}), True),
    ("Domain Grid without y", domain("Grid", {"x": {"values": [1.0]}, "t": {"values": [T0]}}), False),
    ("Domain Grid with numeric t", domain("Grid", {"x": {"values": [1.0]}, "y": {"values": [2.0]},
                                                   "t": {"values": [1, 2]}}), False),
    ("Domain PointSeries with 2 x values", domain("PointSeries", {"x": {"values": [1, 2]}, "y": {"values": [2]},
                                                                  "t": {"values": [T0]}}), False),
    ("Domain Point with extra axis", domain("Point", {"x": {"values": [1]}, "y": {"values": [2]},
                                                      "foo": {"values": [3]}}), False),
    ("Domain Trajectory with 2-value tuples", domain("Trajectory", {"composite": tuples(["t", "x", "y"], [[T0, 1]])}),
     False),
    ("Domain Trajectory with coordinates x, y, t", domain("Trajectory", {"composite": tuples(["x", "y", "t"],
                                                                                             [[1, 2, T0]])}), False),
    ("Domain Polygon with 2 polygons", domain("Polygon", {"composite": polygons([SQUARE, SQUARE2])}), False),
    ("Domain PolygonSeries with 2 polygons", domain("PolygonSeries", {"composite": polygons([SQUARE, SQUARE2]),
                                                                      "t": {"values": [T0]}}), False),
    ("Domain VerticalProfile without z", domain("VerticalProfile", {"x": {"values": [1]}, "y": {"values": [2]}}),
     False),
    ("Domain MultiPoint with 4-value tuples", domain("MultiPoint", {"composite": tuples(["x", "y"],
                                                                                        [[1, 2, 3, 4]])}), False),
    ("Domain MultiPoint with boolean in tuple", domain("MultiPoint", {"composite": tuples(["x", "y"], [[1, True]])}),
     False),
    ("Domain Section without z", domain("Section", {"composite": tuples(["t", "x", "y"], [[T0, 1, 2]])}), False),
    ("Domain axis with start and stop only", domain(None, {"x": {"start": 0, "stop": 1}}), False),
    ("Domain axis with num 0", domain(None, {"x": {"start": 0, "stop": 1, "num": 0}}), False),
    ("Domain axis with mixed values", domain(None, {"x": {"values": [1, "a"]}}), False),
    ("Domain label key that is not a language tag",
     domain(None, {"c": {"values": ["a"]}},
            ({"coordinates": ["c"], "system": {"type": "IdentifierRS",
                                              "targetConcept": {"label": {"not a tag!": "Country"}}}},)),
     False),
    ("Domain without referencing", {"type": "Domain", "domainType": "Point",
                                    "axes": {"x": {"values": [1]}, "y": {"values": [2]}}}, False),
    ("Domain axis with duplicate values", domain(None, {"x": {"values": [1, 1]}}), False),
    ("Domain TemporalRS without calendar", domain("Point", {"x": {"values": [1]}, "y": {"values": [2]}},
                                                  (GEO, {"coordinates": ["t"], "system": {"type": "TemporalRS"}})),
     False),
    ("Domain IdentifierRS without targetConcept",
     domain(None, {"c": {"values": ["a"]}}, ({"coordinates": ["c"], "system": {"type": "IdentifierRS"}},)), False),
    ("Domain IdentifierRS with targetConcept",
     domain(None, {"c": {"values": ["a"]}},
            ({"coordinates": ["c"], "system": {"type": "IdentifierRS", "targetConcept": {"label": {"en": "Country"}}}},)),
     True),
    # Coverages
    ("Coverage PointSeries", coverage(
        domain("PointSeries", {"x": {"values": [25.0]}, "y": {"values": [60.0]}, "t": {"values": [T0, T1]}}),
        {"t2m": ndarray("float", [283.1, 284.2], axisNames=["t"], shape=[2])}), True),
    ("Coverage Grid", coverage(
        domain("Grid", {"x": {"values": [1.0, 2.0, 3.0]}, "y": {"values": [1.0, 2.0]}, "t": {"values": [T0]}}),
        {"t2m": ndarray("float", [1, 2, 3, 4, 5, 6], axisNames=["t", "y", "x"], shape=[1, 2, 3])}), True),
    ("Coverage with domain and range URLs", coverage("https://example.org/domain.json",
                                                     {"t2m": "https://example.org/t2m.json"}), True),
    ("Coverage with TiledNdArray range", coverage(
        domain("Grid", {"x": {"values": [1.0, 2.0]}, "y": {"values": [1.0, 2.0]}}),
        {"t2m": {"type": "TiledNdArray", "dataType": "float", "axisNames": ["y", "x"], "shape": [2, 2],
                 "tileSets": [{"tileShape": [None, None], "urlTemplate": "https://example.org/t2m.json"}]}}), True),
    ("Coverage with unit symbol object", coverage(
        domain("Point", {"x": {"values": [1]}, "y": {"values": [2]}}),
        parameters={"t2m": {"type": "Parameter", "observedProperty": {"label": {"en": "Air temperature"}},
                            "unit": {"symbol": {"type": "http://www.opengis.net/def/uom/UCUM/", "value": "K"}}}}),
     True),
    ("Coverage without parameters", coverage(domain("Point", {"x": {"values": [1]}, "y": {"values": [2]}}),
                                             parameters=None), False),
    ("Coverage with wrong range dataType", coverage(
        domain("Point", {"x": {"values": [1]}, "y": {"values": [2]}}), {"t2m": ndarray("integer", [1.5])}), False),
    ("Coverage with unit without label or symbol", coverage(
        domain("Point", {"x": {"values": [1]}, "y": {"values": [2]}}),
        parameters={"t2m": {"type": "Parameter", "observedProperty": {"label": {"en": "T"}}, "unit": {"id": "K"}}}),
     False),
    ("Coverage with invalid domain", coverage(domain("Grid", {"x": {"values": [1.0]}})), False),
    ("Coverage with numeric domain", coverage(42), False),
    ("Coverage with numeric range", coverage(domain("Point", {"x": {"values": [1]}, "y": {"values": [2]}}),
                                             {"t2m": 42}), False),
    ("Coverage with unknown range type", coverage(domain("Point", {"x": {"values": [1]}, "y": {"values": [2]}}),
                                                  {"t2m": {"type": "Foo"}}), False),
    ("Coverage with TiledNdArray without tileSets", coverage(
        domain("Grid", {"x": {"values": [1.0, 2.0]}, "y": {"values": [1.0, 2.0]}}),
        {"t2m": {"type": "TiledNdArray", "dataType": "float", "axisNames": ["y", "x"], "shape": [2, 2]}}), False),
    ("Coverage with numeric unit symbol", coverage(
        domain("Point", {"x": {"values": [1]}, "y": {"values": [2]}}),
        parameters={"t2m": {"type": "Parameter", "observedProperty": {"label": {"en": "T"}}, "unit": {"symbol": 42}}}),
     False),
    ("Coverage with unit symbol object without value", coverage(
        domain("Point", {"x": {"values": [1]}, "y": {"values": [2]}}),
        parameters={"t2m": {"type": "Parameter", "observedProperty": {"label": {"en": "T"}},
                            "unit": {"symbol": {"type": "x"}}}}), False),
    # Coverage collections
    ("CoverageCollection", {"type": "CoverageCollection", "parameters": PARAMETERS, "referencing": [GEO, TIME],
                            "coverages": [coverage(domain("Point", {"x": {"values": [1]}, "y": {"values": [2]}}, ()),
                                                   parameters=None)]}, True),
    ("CoverageCollection without any parameters",
     {"type": "CoverageCollection", "referencing": [GEO, TIME],
      "coverages": [coverage(domain("Point", {"x": {"values": [1]}, "y": {"values": [2]}}, ()), parameters=None)]},
     False),
]
# Every domain type restricts its axes: adding an unknown axis must be rejected.
SAMPLES += [(f"{name} with extra axis", {**doc, "axes": {**doc["axes"], "foo": {"values": [1]}}}, False)
            for name, doc, expected in list(SAMPLES)
            if expected and doc.get("type") == "Domain" and doc.get("domainType") in (
                "Grid", "Trajectory", "VerticalProfile", "Point", "PointSeries", "MultiPoint", "MultiPointSeries",
                "Section", "Polygon", "PolygonSeries", "MultiPolygon", "MultiPolygonSeries")]


def resolves(root, fragment):
    x = root
    for key in urllib.parse.unquote(fragment).lstrip("/").split("/"):
        key = key.replace("~1", "/").replace("~0", "~")
        if isinstance(x, list) and key.isdigit() and int(key) < len(x):
            x = x[int(key)]
        elif isinstance(x, dict) and key in x:
            x = x[key]
        else:
            return False
    return True


def dangling_refs(bundle, honour_id):
    bad = collections.Counter()

    def walk(o, base, path):
        if isinstance(o, dict):
            if honour_id and "$id" in o and path:
                base = o  # a schema with $id is its own resource
            ref = o.get("$ref")
            if isinstance(ref, str) and ref.startswith("#/") and not resolves(base, ref[1:]):
                bad[ref] += 1
            for k, v in o.items():
                walk(v, base, f"{path}/{k}")
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, base, f"{path}/{i}")

    walk(bundle, bundle, "")
    return bad


def bundle_validators(bundle):
    registry = Registry().with_resource(
        "urn:bundle", Resource.from_contents(bundle, default_specification=DRAFT202012))
    return lambda name: Draft202012Validator({"$ref": f"urn:bundle#/components/schemas/{name}"},
                                             registry=registry)


def verdict(validator, document):
    try:
        errors = list(validator.iter_errors(copy.deepcopy(document)))
    except Exception as e:  # unresolvable $ref and similar
        return None, f"{type(e).__name__}: {str(e)[:100]}"
    return not errors, errors[0].message[:100] if errors else ""


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("dir", nargs="?", default=".")
    parser.add_argument("--canonical", help="path or URL of the canonical CoverageJSON schema")
    args = parser.parse_args()
    failed = False

    if args.canonical:
        if args.canonical.startswith(("http://", "https://")):
            with urllib.request.urlopen(args.canonical) as r:
                canonical = json.load(r)
        else:
            canonical = json.loads(pathlib.Path(args.canonical).read_text())
        validator = Draft7Validator(canonical)
        wrong = [name for name, doc, expected in SAMPLES if verdict(validator, doc)[0] != expected]
        print(f"== canonical schema: {len(SAMPLES) - len(wrong)} of {len(SAMPLES)} samples as expected")
        for name in wrong:
            print(f"   UNEXPECTED {name}")
        failed |= bool(wrong)

    for version in ("oas30", "oas31"):
        path = pathlib.Path(args.dir) / f"ogcapi-environmental-data-retrieval-1-{version}.bundled.json"
        bundle = json.loads(path.read_text())
        print(f"== {path.name} (openapi {bundle.get('openapi')}, version {bundle['info']['version']})")
        for honour_id in (False, True):
            bad = dangling_refs(bundle, honour_id)
            label = "$id-aware" if honour_id else "document root"
            print(f"   unresolvable local $refs ({label}): {sum(bad.values())}")
            for ref, n in bad.most_common(6):
                print(f"      {n:3d}x {ref}")
            failed |= bool(bad)
        renamed = [f"{section}/{name}" for section, items in bundle.get("components", {}).items()
                   if isinstance(items, dict) for name in items if re.search(r"-\d+$", name)]
        print(f"   components renamed by the bundler: {len(renamed)}")
        for name in renamed:
            print(f"      {name}")
        failed |= bool(renamed)
        if version == "oas30":
            continue
        schemas = bundle["components"]["schemas"]
        if "coverageJSON" not in schemas or "ndArray" not in schemas:
            print("   missing components/schemas/coverageJSON or ndArray")
            failed = True
            continue
        validator = bundle_validators(bundle)
        passed = 0
        for name, doc, expected in SAMPLES:
            targets = ["coverageJSON"] + (["ndArray"] if doc.get("type") == "NdArray" else [])
            for target in targets:
                ok, message = verdict(validator(target), doc)
                if ok == expected:
                    passed += 1
                    continue
                failed = True
                outcome = "ERROR" if ok is None else ("REJECTED" if expected else "ACCEPTED")
                print(f"   {outcome} {name} via {target}: {message}")
        total = sum(2 if doc.get("type") == "NdArray" else 1 for _, doc, _ in SAMPLES)
        print(f"   CoverageJSON samples: {passed} of {total} as expected")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
