# 🌍 Global GDP Dashboard

A modern, interactive Flask web application for analyzing and visualizing Global GDP data using World Bank and UN datasets.

## 📊 Features

- **📈 Overview Dashboard** - Key metrics and data statistics at a glance
- **🌍 Country Analysis** - Compare countries by metrics with distribution charts
- **📊 Growth Trends** - Analyze trends and correlations in the data
- **📮 Forecasting** - Advanced time series forecasting capabilities (coming soon)
- **🎨 Interactive Visualizations** - Real-time charts and graphs using Plotly
- **📱 Responsive Design** - Works seamlessly on desktop and mobile devices

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Data Processing:** Pandas, NumPy
- **Visualizations:** Plotly, Plotly.js
- **Data Source:** World Bank & UN Data (181 countries, 8 metrics)

## 📁 Project Structure

```
global-gdp-dashboard/
├── flask_app.py                 # Main Flask application
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── .gitignore                   # Git ignore rules
│
├── templates/                   # HTML templates
│   ├── base.html               # Base template with navigation
│   ├── overview.html           # Dashboard overview page
│   ├── country_analysis.html   # Country comparison page
│   ├── growth_trends.html      # Trends analysis page
│   └── forecasting.html        # Forecasting features page
│
├── static/                      # Static assets
│   ├── css/
│   │   └── style.css           # Main stylesheet
│   └── js/
│       └── script.js           # Utility functions
│
├── data/                        # Data directory
│   └── Global GDP Explorer 2025 (World Bank UN Data).csv
│
├── notebooks/                   # Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_eda_visualizations.ipynb
│
└── docs/                        # Documentation
    ├── PROJECT_SUMMARY.txt
    ├── README.md
    └── summary_report.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Ganatra-Ruchir/global-gdp-dashboard.git
cd global-gdp-dashboard
```

2. **Create virtual environment** (optional but recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install flask pandas plotly numpy
```

4. **Run the application**
```bash
python flask_app.py
```

5. **Open in browser**
```
http://localhost:5000
```

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Overview dashboard |
| `/country` | GET | Country analysis page |
| `/trends` | GET | Growth trends page |
| `/forecasting` | GET | Forecasting page |
| `/api/overview-stats` | GET | Statistical summary |
| `/api/data-preview` | GET | First 5 rows of data |
| `/api/numeric-columns` | GET | List of numeric columns |
| `/api/metric-stats?metric=X` | GET | Stats for specific metric |
| `/api/distribution-chart?metric=X` | GET | Distribution chart data |
| `/api/top-values?metric=X&n=10` | GET | Top N values |
| `/api/box-plot?column=X` | GET | Box plot data |
| `/api/correlation-matrix` | GET | Correlation heatmap data |

## 🎨 Pages Overview

### Overview
- Total records and columns count
- Key statistics (mean, median, min, max)
- Data preview table
- Column information

### Country Analysis
- Select metric from dropdown
- View statistics (mean, median, min, max)
- Distribution chart
- Top 10 countries/entities ranked

### Growth Trends
- Trend analysis with box plots
- Correlation matrix heatmap
- Identify patterns and relationships

### Forecasting
- Placeholder for ARIMA models
- Exponential smoothing
- Confidence intervals
- Scenario analysis

## 📈 Data Statistics

- **Total Records:** 181 countries/entities
- **Metrics:** 8 columns including GDP, growth rates, etc.
- **Data Source:** World Bank & UN Data 2025

## 🔧 Configuration

### Flask Settings
Edit `flask_app.py` to modify:
- Port (default: 5000)
- Debug mode (default: True)
- Host (default: 0.0.0.0)

### Data Path
CSV file location: `data/Global GDP Explorer 2025 (World Bank UN Data).csv`

## 🎯 Usage Examples

### Access Overview Dashboard
Navigate to `http://localhost:5000/` to see:
- Real-time data statistics
- Data preview
- Column information

### Analyze a Country
1. Go to `http://localhost:5000/country`
2. Select a metric from dropdown
3. View stats and distribution chart
4. Check top countries table

### Explore Trends
1. Visit `http://localhost:5000/trends`
2. Select column for trend analysis
3. View box plot and correlations
4. Identify patterns in data

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in flask_app.py from 5000 to another (e.g., 5001)
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Module Not Found
```bash
pip install -r requirements.txt
```

### Data File Not Found
Ensure CSV file is in: `data/Global GDP Explorer 2025 (World Bank UN Data).csv`

## 📚 Project Details

- **Project Name:** Global GDP Dashboard
- **Type:** Flask Web Application
- **Status:** Active Development
- **Last Updated:** January 2026

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements!

### Development Workflow
1. Create a new branch (`git checkout -b feature/AmazingFeature`)
2. Commit changes (`git commit -m 'Add AmazingFeature'`)
3. Push to branch (`git push origin feature/AmazingFeature`)
4. Open Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Ganatra Ruchir**
- 🔗 GitHub: [@Ganatra-Ruchir](https://github.com/Ganatra-Ruchir)
- 📧 Location: Ahmedabad, India
- 💼 Role: Data Analyst & Web Developer

## 🙏 Acknowledgments

- Data Source: World Bank & UN
- Framework: Flask
- Visualization: Plotly
- Data Processing: Pandas

## 📞 Support

For issues, questions, or suggestions:
1. Open an issue on GitHub
2. Create a discussion
3. Submit a pull request

---

**Made with ❤️ for data analysis and visualization**
