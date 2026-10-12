import unittest
from flask_app import app, df

class ExplorerAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_wsgi_import_loads_numeric_snapshot(self):
        self.assertEqual(len(df), 181)
        germany = df[df['Country'] == 'Germany'].iloc[0]
        self.assertEqual(germany['GDP Growth'], -0.27)
        self.assertEqual(germany['GDP (nominal, 2023)'], 4525700000000)
        self.assertEqual(self.client.get('/api/health').status_code, 200)

    def test_invalid_inputs_are_client_errors(self):
        for url in ['/api/top-values?metric=GDP%20Growth&n=oops', '/api/top-values?metric=GDP%20Growth&n=-1', '/api/top-values?metric=GDP%20Growth&n=99999', '/api/metric-stats?metric=Country', '/api/distribution-chart?metric=Country', '/api/box-plot?column=Country']:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 400)

    def test_static_routes_and_missing_page(self):
        self.assertIn(b'Atlas', self.client.get('/').data)
        for name in ['analytics.css', 'analytics-core.js', 'data.js', 'app.js']:
            self.assertEqual(self.client.get('/'+name).status_code, 200)
        self.assertEqual(self.client.get('/does-not-exist').status_code, 404)
        self.assertEqual(self.client.get('/flask_app.py').status_code, 404)

    def test_ranking_uses_values_not_currency_strings(self):
        result = self.client.get('/api/top-values?metric=GDP%20(nominal,%202023)&n=1').get_json()
        self.assertEqual(result['data'][0]['Entity'], 'United States')

if __name__ == '__main__':
    unittest.main()
