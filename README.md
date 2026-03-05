# AI-Documents

A modern MkDocs Material documentation site with automated GitHub Pages deployment to the `gh-pages` branch.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-mkdocs.txt
mkdocs serve
```

Open <http://127.0.0.1:8000>.

## Build

```bash
mkdocs build --clean
```

## Deploy to GitHub Pages

Push to `main` or `master`.

The workflow at `.github/workflows/mkdocs-gh-pages.yml` will:
1. Install dependencies
2. Build the docs
3. Deploy to `gh-pages` using `mkdocs gh-deploy`
