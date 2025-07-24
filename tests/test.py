import pytest
from app import app  # Make sure 'app.py' is your filename

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_existing_user(client):
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json == {"id": 1, "name": "Ajit"}

def test_get_non_existing_user(client):
    response = client.get('/users/99')
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}

def test_get_another_user(client):
    response = client.get('/users/2')
    assert response.status_code == 200
    assert response.json == {"id": 2, "name": "Ravi"}
