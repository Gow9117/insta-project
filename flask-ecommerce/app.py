import os

from flask import Flask, render_template

app = Flask(__name__)

products = {
    1: {
        "name": "Laptop",
        "price": 55000,
        "description": "High-performance laptop for developers.",
    },
    2: {
        "name": "Wireless Mouse",
        "price": 999,
        "description": "Ergonomic wireless mouse.",
    },
    3: {
        "name": "Mechanical Keyboard",
        "price": 2999,
        "description": "RGB mechanical keyboard.",
    },
}


@app.route("/")
def home():
    return render_template("index.html", products=products)


@app.route("/product/<int:product_id>")
def product_details(product_id):
    product = products.get(product_id)
    if not product:
        return "<h2>Product Not Found</h2>", 404
    return render_template("product.html", product=product)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0").lower() in ("1", "true", "yes")
    app.run(host="0.0.0.0", port=port, debug=debug)
