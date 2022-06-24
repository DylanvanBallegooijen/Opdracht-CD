import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Almost finished!!"


def test_cow(client):
    response = client.get("/cow")

    assert response.status_code == 200
    assert response.data == b"MOoooOo!"


def test_dog(client):
    response = client.get("/dog")

    assert response.status_code == 200
    assert response.data == b"Beware of this cuddling little doggy, Chester!!"
