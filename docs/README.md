# 📊 Global GDP Dashboard

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Latest-green)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualization-brightgreen)](https://plotly.com/python/)
[![Status](https://img.shields.io/badge/Status-Active-green)]()
[![Last Commit](https://img.shields.io/github/last-commit/Ganatra-Ruchir/new)]()

> 🚀 Professional-grade interactive data analysis and visualization dashboard for exploring Global GDP trends, forecasting, and country comparisons using World Bank and UN data sources.

---

## 📈 Project Overview

This comprehensive dashboard application provides advanced analytics and visualization capabilities for analyzing global economic indicators. Built with modern web technologies and data science libraries, it enables users to:

- 📊 **Visualize** Global GDP trends across countries and time periods
- 🔍 **Analyze** Economic patterns and country comparisons  
- 🎯 **Forecast** Future GDP trends using statistical models
- 💡 **Extract** Actionable insights from World Bank and UN datasets

---

## 🎨 Dashboard Preview

### Key Features at a Glance:
- **Interactive Charts** - Drill down into data with hover details and zoom capabilities
- **Real-time Filtering** - Dynamic country and metric selection
- **Trend Analysis** - Historical patterns and growth rate calculations
- **Forecasting Engine** - Predictive models for economic projections
- **Professional UI** - Clean, responsive design optimized for insights

---

lobal GDP Dashboard

An interactive data analysis and visualization dashboard for exploring Global GDP trends from World Bank and UN data sources.

## 📁 Project Structure

```
global-gdp-dashboard/
├── data/
│   ├── raw/                      # Raw data files
│   ├── processed/                # Cleaned and processed data
│   └── external/                 # Reference data (country codes, regions)
│
├── notebooks/
│   ├── 01_data_exploration.ipynb      # Initial data exploration
│   ├── 02_data_cleaning.ipynb         # Data cleaning and preprocessing
│   ├── 03_feature_engineering.ipynb   # Feature creation and transformation
│   └── 04_eda_visualizations.ipynb    # Exploratory analysis and visualization
│
├── src/
│   ├── data/                     # Data loading and preprocessing modules
│   │   ├── load_data.py         # Data loading functions
│   │   └── preprocess.py        # Data cleaning functions
│   │
│   ├── analysis/                 # Analysis modules
│   │   ├── gdp_trends.py        # Trend analysis
│   │   ├── country_comparison.py # Country comparison analysis
│   │   └── growth_forecasting.py # Forecasting models
│   │
│   └── utils/
│       └── helpers.py           # Utility functions
│
├── dashboard/
│   ├── app.py                    # Main Streamlit application
│   ├── pages/                    # Dashboard pages
│   │   ├── overview.py          # Overview page
│   │   ├── country_analysis.py  # Country analysis page
│   │   ├── growth_trends.py     # Growth trends page
│   │   └── forecasting.py       # Forecasting page
│   │
│   └── assets/
│       ├── style.css            # CSS styling
│       └── logo.png             # Dashboard logo
│
├── reports/
│   ├── figures/                 # Generated visualizations
│   └── summary_report.md        # Summary report
│
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── .gitignore                  # Git ignore file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager

### Installation

1. **Clone or setup the project**
```bash
cd global-gdp-dashboard
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Place your data**
- Add your Global GDP CSV file to `data/raw/global_gdp.csv`
- Ensure columns are properly named

## 📊 Usage

### Data Processing

1. **Run Data Exploration Notebook**
   - Opens `notebooks/01_data_exploration.ipynb`
   - Analyzes raw data structure and quality

2. **Run Data Cleaning Notebook**
   - Opens `notebooks/02_data_cleaning.ipynb`
   - Cleans and preprocesses data
   - Outputs to `data/processed/cleaned_gdp.csv`

3. **Run Feature Engineering Notebook**
   - Opens `notebooks/03_feature_engineering.ipynb`
   - Creates derived features and metrics
   - Outputs to `data/processed/feature_engineered_gdp.csv`

4. **Run EDA Notebook**
   - Opens `notebooks/04_eda_visualizations.ipynb`
   - Generates comprehensive visualizations

### Launch Dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will open in your default browser at `http://localhost:8501`

## 📈 Dashboard Features

### Overview Page
- Key metrics and statistics
- Data quality summary
- Quick data preview

### Country Analysis
- Top countries by selected metric
- Country rankings and comparisons
- Custom filtering options

### Growth Trends
- Historical growth rate analysis
- Trend identification
- Distribution analysis

### Forecasting
- Time series forecasting models
- Confidence intervals
- Scenario analysis (coming soon)

## 🔧 Core Modules

### data/load_data.py
- `load_raw_data()` - Load raw CSV data
- `load_processed_data()` - Load cleaned data
- `save_processed_data()` - Save processed data
- `get_data_path()` - Get path to data directory

### data/preprocess.py
- `clean_data()` - Main cleaning pipeline
- `handle_missing_values()` - Handle null values
- `remove_duplicates()` - Remove duplicate rows
- `standardize_column_names()` - Standardize naming
- `convert_data_types()` - Convert to appropriate types

### analysis/gdp_trends.py
- `calculate_growth_rate()` - Calculate growth rates
- `get_trend_statistics()` - Get trend metrics
- `calculate_moving_average()` - Calculate moving averages
- `identify_peaks_troughs()` - Identify extrema

### analysis/country_comparison.py
- `compare_countries()` - Compare metrics across countries
- `get_rank_by_metric()` - Rank countries
- `calculate_market_share()` - Calculate market share
- `get_top_performers()` - Get top performing countries

### analysis/growth_forecasting.py
- `linear_trend_forecast()` - Linear trend forecasting
- `exponential_smoothing()` - Exponential smoothing
- `calculate_cagr()` - Calculate compound annual growth rate
- `forecast_with_confidence_interval()` - Forecast with CI

### utils/helpers.py
- `get_summary_stats()` - Summary statistics
- `print_data_quality_report()` - Data quality report
- `format_currency()` - Format as currency
- `format_percentage()` - Format as percentage
- `get_top_n()` - Get top N values

## 📝 Data Requirements

Your GDP data should have at least the following columns:
- Country/Region identifier
- Year or date
- GDP value (or similar metric)

Supported formats:
- CSV files
- Excel files (.xlsx)
- Other tabular formats

## 🎯 Analysis Capabilities

- **Exploratory Analysis**: Visualize data distributions and patterns
- **Time Series Analysis**: Track GDP trends over time
- **Comparative Analysis**: Compare GDP across countries and regions
- **Growth Analysis**: Analyze growth rates and trends
- **Forecasting**: Project future GDP values
- **Statistical Analysis**: Generate summary statistics and insights

## 🔍 Sample Analysis Workflows

### Workflow 1: Quick Overview
1. Load raw data
2. Generate exploration report
3. Identify key countries and trends
4. Export summary

### Workflow 2: Deep Dive Analysis
1. Data exploration and quality check
2. Clean and preprocess data
3. Feature engineering
4. EDA with visualizations
5. Trend analysis
6. Forecasting

### Workflow 3: Dashboard Monitoring
1. Update raw data
2. Rerun preprocessing notebooks
3. Refresh dashboard
4. Monitor trends and anomalies

## 📚 Jupyter Notebooks Guide

### Notebook 1: Data Exploration (01_data_exploration.ipynb)
- Load and inspect raw data
- Check data types and structure
- Identify missing values
- Generate summary statistics
- Visualize data distributions

### Notebook 2: Data Cleaning (02_data_cleaning.ipynb)
- Remove duplicates
- Handle missing values
- Detect outliers
- Standardize formats
- Generate quality report

### Notebook 3: Feature Engineering (03_feature_engineering.ipynb)
- Create growth rate features
- Calculate moving averages
- Generate GDP categories
- Compute global percentage
- Create time-based features

### Notebook 4: EDA Visualizations (04_eda_visualizations.ipynb)
- Distribution analysis
- Country rankings
- Time series trends
- Correlation analysis
- Interactive visualizations

## ⚙️ Configuration

### Environment Variables
```bash
DATA_PATH=./data
OUTPUT_PATH=./reports
```

### Dashboard Settings
Edit `dashboard/app.py` to customize:
- Page title and icon
- Layout and styling
- Default metrics
- Filter options

## 🐛 Troubleshooting

### Data Loading Issues
- Ensure CSV file exists in `data/raw/`
- Check column names are consistent
- Verify file encoding is UTF-8

### Dashboard Issues
- Clear Streamlit cache: `streamlit cache clear`
- Reinstall dependencies: `pip install -r requirements.txt --upgrade`
- Check Python version: `python --version`

### Notebook Issues
- Ensure Jupyter is installed: `pip install jupyter`
- Check kernel is available: `jupyter kernelspec list`
- Update packages: `pip install --upgrade -r requirements.txt`

## 📈 Performance Tips

- Use processed data instead of raw data for analysis
- Cache data in Streamlit for faster loading
- Filter large datasets before visualization
- Use aggregation for time series analysis

## 🤝 Contributing

Contributions are welcome! Please:
1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 📧 Support

For issues, questions, or suggestions:
- Create an issue in the repository
- Check existing documentation
- Review notebook examples

## 🎓 Learning Resources

- [Pandas Documentation](https://pandas.pydata.org/)
- [Plotly Documentation](https://plotly.com/python/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Jupyter Notebook Guide](https://jupyter.org/documentation)

## 🔗 Data Sources

- **World Bank**: https://data.worldbank.org/
- **UN Data**: http://data.un.org/
- **IMF**: https://www.imf.org/

## 📅 Project Timeline

- **Initial Setup**: January 2026
- **Data Collection**: Ongoing
- **Analysis**: Continuous
- **Dashboard Updates**: Monthly

## ✨ Future Enhancements

- [ ] Advanced forecasting models (ARIMA, Prophet)
- [ ] Regional aggregation and analysis
- [ ] Economic indicators correlation
- [ ] Scenario planning tools
- [ ] Data export functionality
- [ ] Multi-language support
- [ ] Real-time data updates
- [ ] API integration

---

**Created**: January 2026
**Last Updated**: January 2026
**Version**: 1.0.0
