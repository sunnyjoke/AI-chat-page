from project import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    default = client.get('/')
    assert default.status_code == 302
    assert default.headers['Location'] == '/login'

def test_login(client):
    login = client.get('/login')
    assert login.status_code == 200

def test_logout(client):
    logout = client.get('/logout')
    assert logout.status_code == 302
    assert logout.headers['Location'] == '/login'

def test_chat(client):
    chat = client.get('/chat_page')
    assert chat.status_code == 401

def test_wrong(client):
    wrong = client.get('/wrong_direction')
    assert wrong.status_code == 404
