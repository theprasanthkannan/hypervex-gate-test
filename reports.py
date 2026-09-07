from flask import Flask, jsonify, request

from db import run_query

app = Flask(__name__)


@app.route("/api/reports")
def sales_report():
    """Sales for a region, for the internal reporting dashboard."""
    region = request.args.get("region", "")
    return jsonify(run_query(f"SELECT * FROM sales WHERE region = '{region}'"))
