"""Reproducibly normalize the two repository-owned snapshots, without network data."""
import csv
import json
import math
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]

def number(value):
    text = str(value).strip().replace('−', '-').replace(',', '').replace('$', '').replace('%', '')
    try:
        result = float(text)
        return result if math.isfinite(result) else None
    except ValueError:
        return None

def write(data):
    (ROOT/'data.js').write_text('window.DATA = '+json.dumps(data,ensure_ascii=False,separators=(',', ':'))+';\n',encoding='utf-8')

gdp = ROOT

with next((gdp / 'data').glob('*.csv')).open(encoding='utf-8-sig', newline='') as stream:
    rows = [dict(country=r['Country'], gdp=number(r['GDP (nominal, 2023)']), growth=number(r['GDP Growth']), population=number(r['Population 2023']), perCapita=number(r['GDP per capita']), share=number(r['Share of World GDP'])) for r in csv.DictReader(stream)]
write(rows)

