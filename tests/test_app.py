import pytest

from app import app


@pytest.fixture
def client():
    test_app = app

    with test_app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get('/')
    assert b"https://firebasestorage.googleapis.com" in rv.data
