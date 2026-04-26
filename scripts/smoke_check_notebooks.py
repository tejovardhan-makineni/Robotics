from __future__ import annotations

import os
import warnings
from pathlib import Path

import nbformat


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"


def main():
    os.environ.setdefault("MPLBACKEND", "Agg")
    warnings.filterwarnings("ignore", message="FigureCanvasAgg is non-interactive.*")
    warnings.filterwarnings("ignore", message="More than 20 figures have been opened.*")
    for path in sorted(NOTEBOOK_DIR.glob("*.ipynb")):
        namespace = {}
        print(f"RUN {path.relative_to(ROOT)}", flush=True)
        notebook = nbformat.read(path, as_version=4)
        for index, cell in enumerate(notebook.cells, start=1):
            if cell.cell_type != "code":
                continue
            try:
                exec(cell.source, namespace)
                if namespace.get("plt") is not None:
                    namespace["plt"].close("all")
            except Exception as exc:
                raise RuntimeError(f"{path.name} failed in cell {index}") from exc
        print(f"OK  {path.relative_to(ROOT)}", flush=True)


if __name__ == "__main__":
    main()
