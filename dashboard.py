from flask import Flask, jsonify, request

from sales import fetch_sales, fetch_totals

app = Flask(__name__)


@app.route("/api/dashboard/totals")
def totals():
    return jsonify(fetch_totals())


@app.route("/api/dashboard/region")
def region_breakdown():
    """Sales for one region, for the internal dashboard."""
    region = request.args.get("region", "")
    return jsonify(fetch_sales(region))
