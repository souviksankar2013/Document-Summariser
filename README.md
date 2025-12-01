# Document Summariser

A small Python project that provides a basis for extracting and summarising documents. The repository contains the minimal implementation files `app_lib.py` and `main_app.py`.

**Purpose:**
- Provide a lightweight starting point for document ingestion and summarisation workflows.

**Contents:**
- `app_lib.py`: Helper library functions used by the application.
- `main_app.py`: Entry-point script / example runner.
- `LICENSE`: Project license.

**Features**
- Minimal, easy-to-extend structure for document summarisation.

**Requirements**
- Python 3.8+ (recommended)
- Any third-party dependencies (if used) should be listed in `requirements.txt` (not included by default).

**Quick Start (Windows PowerShell)**

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies (if a `requirements.txt` is present):

```powershell
pip install -r requirements.txt
```

3. Run the application (basic example):

```powershell
python main_app.py
```

Note: `main_app.py` is the entry script in this repo — open it to see expected arguments or behavior. If the project has CLI options or expects file input, adapt the command accordingly (for example, `python main_app.py path\to\document.pdf`).

**Development**
- Read `app_lib.py` and `main_app.py` to understand the current behaviour and extension points.
- Add a `requirements.txt` file listing external packages you use (e.g., `transformers`, `sentence-transformers`, `pdfplumber`, etc.).
- Consider adding tests, a CI workflow, and a `pyproject.toml` or `setup.cfg` if packaging.

**Contributing**
- Open an issue or PR with a clear description of changes.
- Keep changes small and focused; include tests when adding functionality.

**License**
- See the `LICENSE` file in the repository root.

---

If you want, I can:
- add a `requirements.txt` with likely dependencies,
- update `main_app.py` to accept command-line arguments for input files,
- or add an example `README` usage section tailored to how `main_app.py` currently works (I can inspect it and update the README accordingly).

Feel free to tell me which of the above you'd like next.
