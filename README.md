# Atlas — GDP Explorer V2

The default interface is static: run `python -m http.server 8000` and open index.html. For the optional Flask API: use Python 3.12+, `pip install -r requirements.txt`, then `python flask_app.py`. Importing flask_app under WSGI now loads the dataset. The data is a 2023 snapshot despite the source filename saying 2025. Scenario results are arithmetic, not forecasts. Upstream revision history and the price basis for reported growth are not supplied. Existing legacy API routes remain available with numeric validation.

See [V2 features and validation](V2_RELEASE.md). The earlier project documentation is retained in [README_GITHUB.md](README_GITHUB.md).
