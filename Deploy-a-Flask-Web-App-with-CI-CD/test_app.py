import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get('/')

    assert response.status_code == 200
    assert b'Gowtham E-Commerce Store' in response.data


def test_contact_page(client):
    response = client.get('/contact')

    assert response.status_code == 200
    assert b'+91 8883197578' in response.data


def test_product_page(client):
    response = client.get('/product/1')

    assert response.status_code == 200
    assert b'Laptop' in response.data


def test_invalid_product(client):
    response = client.get('/product/999')

    assert response.status_code == 404