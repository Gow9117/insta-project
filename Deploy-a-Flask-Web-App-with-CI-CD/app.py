import os

from flask import Flask

app = Flask(__name__)

products = {
    1: {
        "name": "Laptop",
        "price": 55000,
        "description": "High-performance laptop for developers."
    },
    2: {
        "name": "Wireless Mouse",
        "price": 999,
        "description": "Ergonomic wireless mouse."
    },
    3: {
        "name": "Mechanical Keyboard",
        "price": 2999,
        "description": "RGB mechanical keyboard."
    }
}

CSS = """
<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.header {
    background-color: #2c3e50;
    color: white;
    text-align: center;
    padding: 20px;
}

.container {
    width: 80%;
    margin: auto;
    padding: 20px;
}

.product-card {
    background: white;
    padding: 15px;
    margin: 15px 0;
    border-radius: 8px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.2);
}

.price {
    color: green;
    font-size: 20px;
    font-weight: bold;
}

.btn {
    display: inline-block;
    background-color: #3498db;
    color: white;
    padding: 10px 15px;
    text-decoration: none;
    border-radius: 5px;
}

.btn:hover {
    background-color: #2980b9;
}

.footer {
    text-align: center;
    background-color: #2c3e50;
    color: white;
    padding: 10px;
    margin-top: 20px;
}
</style>
"""


@app.route("/")
def home():
    html = f"""
    <html>
    <head>
        <title>Simple E-Commerce Store</title>
        {CSS}
    </head>
    <body>

        <div class="header">
            <h1>🛒 Gowtham E-Commerce Store</h1>
            <p>Best Deals on Electronics</p>
        </div>

        <div class="container">
            <h2>Featured Products</h2>
    """

    for pid, product in products.items():
        html += f"""
            <div class="product-card">
                <h3>{product['name']}</h3>
                <p class="price">₹{product['price']}</p>
                <p>{product['description']}</p>
                <a class="btn" href="/product/{pid}">View Details</a>
            </div>
        """

    html += """
        </div>

        <div class="footer">
            © 2026 Gowtham Store
        </div>

    </body>
    </html>
    """
    return html


@app.route("/product/<int:product_id>")
def product_details(product_id):
    product = products.get(product_id)

    if not product:
        return "<h2>Product Not Found</h2>", 404

    return f"""
    <html>
    <head>
        <title>{product['name']}</title>
        {CSS}
    </head>
    <body>

        <div class="header">
            <h1>{product['name']}</h1>
        </div>

        <div class="container">
            <div class="product-card">
                <h2>{product['name']}</h2>
                <p class="price">₹{product['price']}</p>
                <p>{product['description']}</p>

                <button class="btn">Add to Cart</button>
                <br><br>

                <a class="btn" href="/">Back to Products</a>
            </div>
        </div>

    </body>
    </html>
    """


@app.route("/contact")
def contact():
    return f"""
    <html>
    <head>
        <title>Contact Us</title>
        {CSS}
    </head>
    <body>

        <div class="header">
            <h1>Contact Us</h1>
        </div>

        <div class="container">
            <div class="product-card">
                <h3>Email</h3>
                <p>gow9117@gmail.com</p>

                <h3>Phone</h3>
                <p>+91 8883197578</p>

                <a class="btn" href="/">Home</a>
            </div>
        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0").lower() in ("1", "true", "yes")
    app.run(host="0.0.0.0", port=port, debug=debug)