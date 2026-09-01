from fastapi.testclient import TestClient
from predictAPI import app
from pathlib import Path

client = TestClient(app)

TEST_IMAGE = (
    Path(__file__).resolve().parent.parent
    / "testData"
    / "test1.jpg"
)

def test_get():
    """This is a simple test to verify the API"""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Please see /docs for API usage."}

def test_eyeDisease1():
    """This is test 1 to verify the API returns the correct eye Disease"""

    response = client.post(
        "/eyes",
        files= {
            "eyePic" : (
                "test1.jpg",
                TEST_IMAGE.readbytes(),
                "image/jpg"
            )
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "result": {
            "disease": "Normal",
            "condidence": '%d'
        }
    }