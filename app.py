from flask import Flask, request, jsonify
from scraper import get_amazon_price

app = Flask(__name__)

@app.route('/price', methods=['GET'])
def price_route():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    price = get_amazon_price(url)
    if price:
        return jsonify({"price": price})
    else:
        return jsonify({"error": "Unable to fetch price"}), 500

if __name__ == '__main__':
    app.run(debug=True)