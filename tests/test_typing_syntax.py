import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _annotations(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.arg) and node.annotation is not None:
            yield node.annotation
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.returns is not None:
                yield node.returns
        elif isinstance(node, ast.AnnAssign):
            yield node.annotation


def _contains_union_operator(annotation):
    return any(
        isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr)
        for node in ast.walk(annotation)
    )


def test_union_style_check_detects_nested_pep604_union():
    tree = ast.parse("def example(value: list[int | str]) -> None: ...")
    annotation = next(_annotations(tree))

    assert not _contains_union_operator(annotation)


def test_package_annotations_avoid_pep604_union_syntax():
    source_files = [ROOT / "pefile.py", ROOT / "peutils.py"]
    source_files.extend((ROOT / "ordlookup").rglob("*.py"))
    violations = []

    for path in source_files:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for annotation in _annotations(tree):
            if _contains_union_operator(annotation):
                violations.append(
                    f"{path.relative_to(ROOT)}:{annotation.lineno}"
                )

    assert not violations, (
        "Use typing.Union or typing.Optional instead of `|` in annotations: "
        + ", ".join(violations)
    )
