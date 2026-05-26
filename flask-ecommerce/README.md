# Flask E-Commerce Web Application

A simple E-Commerce web application built using Flask. This project demonstrates basic web development concepts and can be used as a DevOps portfolio project with Docker, Jenkins, Pytest, and Kubernetes.

## Project Structure

```text
flask-ecommerce/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── jenkins.sh
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── product.html
│   └── contact.html
│
└── static/
    └── style.css
```

## Installation (EC2 or local)

```bash
git clone https://github.com/Gow9117/insta-project.git
cd insta-project/flask-ecommerce
pip3 install -r requirements.txt
python3 app.py
```

## Running Tests

```bash
python3 -m pytest test_app.py -v
```

## Docker Deployment

```bash
docker build -t flask-ecommerce .
docker run -d -p 5000:5000 --name flask-app flask-ecommerce
```

Application URL: `http://<host>:5000`
