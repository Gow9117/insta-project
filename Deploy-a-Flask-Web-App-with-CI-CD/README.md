# Flask E-Commerce Web Application

A simple E-Commerce web application built using Flask. This project demonstrates basic web development concepts and can be used as a DevOps portfolio project with Docker, Jenkins, Pytest, and Kubernetes.

## Features

* Home page displaying products
* Product details page
* Contact page
* Responsive CSS styling
* Docker containerization
* Pytest unit testing
* CI/CD ready

## Project Structure

```text
flask-ecommerce/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── __pycache__/
│
├── templates/
│   ├── index.html
│   ├── product.html
│   └── contact.html
│
└── static/
    └── style.css
```

## Prerequisites

* Python 3.x
* pip
* Docker (optional)

## Installation

Clone the repository:

```bash
git clone https://github.com/your-repository/flask-ecommerce.git
cd flask-ecommerce
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

## Running the Application

Start the Flask application:

```bash
python3 app.py
```

Application URL:

```text
http://localhost:5000
```

## Running Tests

Execute unit tests using Pytest:

```bash
pytest -v
```

Example output:

```text
================= test session starts =================
test_app.py::test_home_page PASSED
test_app.py::test_contact_page PASSED
test_app.py::test_product_page PASSED
test_app.py::test_invalid_product PASSED

================= 4 passed =================
```

## Docker Deployment

Build Docker image:

```bash
docker build -t flask-ecommerce .
```

Run Docker container:

```bash
docker run -d -p 5000:5000 --name flask-app flask-ecommerce
```

Verify container:

```bash
docker ps
```

## Technologies Used

* Python
* Flask
* HTML
* CSS
* Docker
* Pytest

## Future Enhancements

* User Authentication
* Shopping Cart
* Payment Gateway Integration
* Product Database (MySQL/PostgreSQL)
* Jenkins CI/CD Pipeline
* Kubernetes Deployment
* Monitoring with Prometheus and Grafana

## Author

Developed as a Flask and DevOps learning project.
