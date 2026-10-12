# Atlas — GDP Explorer V2

Release date: 12 October 2026.

## User-facing features

1. Normalize currency, comma-separated numbers and Unicode negative percentages.
2. Search the country ledger.
3. Switch between GDP, per-capita GDP, growth, population and world share.
4. Rank ascending or descending.
5. Compare up to four countries across metrics.
6. Keep comparison countries pinned while searching.
7. Calculate selected-view GDP and its share of the dataset total.
8. Inspect median and a five-bin metric distribution.
9. Explore an explicit compound-growth scenario with adjustable assumptions.
10. Export every filtered row to CSV.
11. Share search, metric, sort order and comparison in a URL.
12. Inspect quality counts and source limitations.
13. Print a report.
14. Switch and remember light/dark theme.

## Use and limits

The default interface is static: run `python -m http.server 8000` and open index.html. For the optional Flask API: use Python 3.12+, `pip install -r requirements.txt`, then `python flask_app.py`. Importing flask_app under WSGI now loads the dataset. The data is a 2023 snapshot despite the source filename saying 2025. Scenario results are arithmetic, not forecasts. Upstream revision history and the price basis for reported growth are not supplied. Existing legacy API routes remain available with numeric validation.

## Interface and reliability

Responsive layouts, keyboard focus, lightweight CSS animation with a pause control, and operating-system reduced-motion support. CSV exports quote values and neutralize common spreadsheet formula prefixes. Browser checks cover representative workflows, download events, reload persistence where applicable, JavaScript errors and mobile overflow. Passing these checks is not a guarantee of zero defects.

## Verification

```sh
npm ci
npx playwright install chromium
npm run test:browser
```

