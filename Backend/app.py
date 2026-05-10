from flask import Flask, jsonify
import sqlite3
import pandas as pd

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('sales.db')
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

# API endpoint to get overall sales statistics
@app.route('/sales/stats', methods=['GET'])
def get_sales_stats():
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()

    total_sales = df['sales'].sum()
    average_sales = df['sales'].mean()
    std_deviation = df['sales'].std()

    return jsonify({
        'total_sales': total_sales,
        'average_sales': average_sales,
        'standard_deviation': std_deviation
    })

# API endpoint to get product-wise sales summary
@app.route('/sales/product', methods=['GET'])
def get_sales_by_product():
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()

    sales_by_product = df.groupby('product')['sales'].sum().to_dict()

    return jsonify(sales_by_product)

# API endpoint to get region-wise sales summary
@app.route('/sales/region', methods=['GET'])
def get_sales_by_region():
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()

    sales_by_region = df.groupby('region')['sales'].sum().to_dict()

    return jsonify(sales_by_region)

# API endpoint to get monthly sales trends
@app.route('/sales/monthly', methods=['GET'])
def get_monthly_sales_trends():
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()

    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')

    monthly_sales_trends = df.groupby('month')['sales'].sum().to_dict()

    return jsonify(monthly_sales_trends)

if __name__ == '__main__':
    app.run(debug=True)
