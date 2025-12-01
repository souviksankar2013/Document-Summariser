# Document Summariser

A small Python project that provides a basis for extracting and summarising documents. The repository contains the minimal implementation files `app_lib.py` and `main_app.py`.

**Purpose:**
- Provide a lightweight starting point for document ingestion and summarisation workflows, using Amazon Bedrock for model inference.

**Built With**
- Amazon Bedrock (via `boto3` / Bedrock Runtime) — the summarisation call in `app_lib.py` uses Bedrock's `converse` API and a Bedrock model ID.

**Contents:**
- `app_lib.py`: Helper library functions that call Amazon Bedrock using `boto3`.
- `main_app.py`: Streamlit-based entry-point for uploading documents and requesting summaries.
- `LICENSE`: Project license.

**Features**
- Minimal, easy-to-extend structure for document summarisation backed by Bedrock.

**Requirements**
- Python 3.8+ (recommended)
- See `requirements.txt` for Python package dependencies used by the code in this repository (includes `awscli` for convenience when configuring AWS credentials).

**Quick Start (Windows PowerShell)**

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Configure AWS credentials and region (Bedrock requires an AWS account and the correct region):

```powershell
aws configure
```

Make sure the configured IAM user/role has permission to call Bedrock (e.g., `bedrock:InvokeModel` / `bedrock:Converse`).

4. Run the application (basic example):

```powershell
streamlit run main_app.py
```

Note: `main_app.py` is a Streamlit app — use `streamlit run` to start the UI. The app uploads a file and sends the bytes to the Bedrock model via `app_lib.get_summary`.

**Bedrock-specific notes**
- The code calls Bedrock's `converse` API with the model ID `us.anthropic.claude-3-7-sonnet-20250219-v1:0` as an example. Replace the `modelId` in `app_lib.py` with the model you intend to use.
- Ensure your AWS region supports Bedrock and your IAM principal has the required permissions.

**Development**
- Read `app_lib.py` and `main_app.py` to understand the current behaviour and extension points.
- If you plan to parse PDF/DOCX contents before sending them to Bedrock (to extract text or metadata), consider adding libraries such as `pdfplumber` or `python-docx`.
- Consider adding tests, a CI workflow, and a `pyproject.toml` or `setup.cfg` if packaging.

**Contributing**
- Open an issue or PR with a clear description of changes.
- Keep changes small and focused; include tests when adding functionality.

**License**
- See the `LICENSE` file in the repository root.

---

I updated the README to mention Amazon Bedrock and included notes about configuring AWS credentials. I can also:
- create or refine `requirements.txt` (I will add it next),
- update `app_lib.py` to make the Bedrock `modelId` configurable via environment variables or a settings file,
- add example input documents and a demo script.

Tell me which you'd like next.
