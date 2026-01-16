"""
Global GDP Dashboard - Flask Web Application
Interactive dashboard with HTML/CSS/JavaScript frontend
"""

from flask import Flask, render_template, jsonify, request
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import sys
import json
import numpy as np

# Add src to path
app_dir = Path(__file__).parent
project_root = app_dir.parent
sys.path.insert(0, str(project_root / 'src'))

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['JSON_SORT_KEYS'] = False

# Global data variable
df = None

def load_data():
    """Load and cache data"""
    global df
    try:
        # Try processed data first
        processed_path = project_root / 'data' / 'processed' / 'feature_engineered_gdp.csv'
        if processed_path.exists():
            df = pd.read_csv(processed_path)
            return True
        else:
            # Fall back to raw data
            raw_path = project_root / 'data' / 'raw' / 'global_gdp.csv'
            if raw_path.exists():
                df = pd.read_csv(raw_path)
                return True
            else:
                # Try data folder directly
                data_path = app_dir / 'data' / 'Global GDP Explorer 2025 (World Bank  UN Data).csv'
                if data_path.exists():
                    df = pd.read_csv(data_path)
                    return True
    except Exception as e:
        print(f"Error loading data: {str(e)}")
    return False

def get_numeric_cols():
    """Get numeric columns from dataframe"""
    if df is None:
        return []
    return df.select_dtypes(include=['number']).columns.tolist()

def get_string_cols():
    """Get string columns from dataframe"""
    if df is None:
        return []
    return df.select_dtypes(include=['object']).columns.tolist()

# Routes
@app.route('/')
def index():
    """Overview page"""
    if df is None:
        return "Error: Data not loaded", 500
    
    return render_template('overview.html',
                         rows=len(df),
                         cols=len(df.columns))

@app.route('/country')
def country_analysis():
    """Country analysis page"""
    return render_template('country_analysis.html')

@app.route('/trends')
def growth_trends():
    """Growth trends page"""
    return render_template('growth_trends.html')

@app.route('/forecasting')
def forecasting():
    """Forecasting page"""
    return render_template('forecasting.html')

# API Routes
@app.route('/api/overview-stats')
def api_overview_stats():
    """Get overview statistics"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    numeric_cols = get_numeric_cols()
    stats = {}
    
    for col in numeric_cols:
        stats[col] = {
            'mean': float(df[col].mean()),
            'median': float(df[col].median()),
            'std': float(df[col].std()),
            'min': float(df[col].min()),
            'max': float(df[col].max())
        }
    
    return jsonify({'stats': stats})

@app.route('/api/data-preview')
def api_data_preview():
    """Get data preview (first 5 rows)"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    preview = df.head(5).fillna('N/A').to_dict('records')
    return jsonify({'data': preview})

@app.route('/api/data-description')
def api_data_description():
    """Get data description statistics"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    description = df.describe().fillna('N/A').to_dict()
    return jsonify(description)

@app.route('/api/column-info')
def api_column_info():
    """Get column information"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    columns = []
    for col in df.columns:
        columns.append({
            'name': col,
            'type': str(df[col].dtype),
            'non_null': int(df[col].count()),
            'null': int(df[col].isna().sum())
        })
    
    return jsonify({'columns': columns})

@app.route('/api/numeric-columns')
def api_numeric_columns():
    """Get list of numeric columns"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    numeric_cols = get_numeric_cols()
    return jsonify({'columns': numeric_cols})

@app.route('/api/metric-stats')
def api_metric_stats():
    """Get statistics for a specific metric"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    metric = request.args.get('metric')
    if not metric or metric not in df.columns:
        return jsonify({'error': 'Invalid metric'}), 400
    
    col_data = df[metric].dropna()
    
    stats = {
        'mean': float(col_data.mean()),
        'median': float(col_data.median()),
        'std': float(col_data.std()),
        'min': float(col_data.min()),
        'max': float(col_data.max()),
        'count': int(len(col_data))
    }
    
    return jsonify(stats)

@app.route('/api/distribution-chart')
def api_distribution_chart():
    """Get distribution chart data for a metric"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    metric = request.args.get('metric')
    if not metric or metric not in df.columns:
        return jsonify({'error': 'Invalid metric'}), 400
    
    col_data = df[metric].dropna()
    
    fig = px.histogram(col_data, nbins=30, title=f'Distribution of {metric}')
    fig.update_layout(showlegend=False, height=400)
    
    return jsonify(json.loads(fig.to_json()))

@app.route('/api/top-values')
def api_top_values():
    """Get top N values for a metric"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    metric = request.args.get('metric')
    n = int(request.args.get('n', 10))
    
    if not metric or metric not in df.columns:
        return jsonify({'error': 'Invalid metric'}), 400
    
    # Try to get country/entity column
    entity_col = None
    for col in ['Country', 'Entity', 'Country Name', 'Country/Entity']:
        if col in df.columns:
            entity_col = col
            break
    
    if entity_col:
        top_data = df[[entity_col, metric]].dropna().nlargest(n, metric)
        top_data.columns = ['Entity', metric]
        data = top_data.to_dict('records')
    else:
        top_data = df[metric].dropna().nlargest(n)
        data = [{'Value': float(v)} for v in top_data.values]
    
    return jsonify({'data': data})

@app.route('/api/box-plot')
def api_box_plot():
    """Get box plot for a column"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    column = request.args.get('column')
    if not column or column not in df.columns:
        return jsonify({'error': 'Invalid column'}), 400
    
    col_data = df[column].dropna()
    
    fig = go.Figure(data=[go.Box(y=col_data, name=column)])
    fig.update_layout(title=f'Box Plot: {column}', height=400)
    
    return jsonify(json.loads(fig.to_json()))

@app.route('/api/correlation-matrix')
def api_correlation_matrix():
    """Get correlation matrix"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    numeric_cols = get_numeric_cols()
    
    if len(numeric_cols) < 2:
        return jsonify({'error': 'Need at least 2 numeric columns'}), 400
    
    corr_matrix = df[numeric_cols].corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        zmid=0
    ))
    fig.update_layout(title='Correlation Matrix', height=600)
    
    return jsonify(json.loads(fig.to_json()))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# Main
if __name__ == '__main__':
    # Load data
    if load_data():
        print(f"✓ Data loaded successfully! Shape: {df.shape}")
        print(f"✓ Starting Flask app on http://localhost:5000")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("✗ Failed to load data!")
        sys.exit(1)
