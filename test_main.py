import pytest
from main import app

@pytest.fixture
def client():
    # Configure app for testing
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the root route returns 200 OK."""
    response = client.get('/')
    assert response.status_code == 200

def test_noam_route(client):
    """Test the /Noam route returns 200 OK and expected text."""
    response = client.get('/Noam')
    assert response.status_code == 200
    assert b"Hello Noam! (The GOAT)" in response.data