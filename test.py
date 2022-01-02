from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_null_prediction():
    response = client.post('/v1/prediction', json={
                                                    "brand_name": 0,
                                                    "model_name": 0,
                                                    "motor_size": 0,
                                                    "years": 0,
                                                    "kms_driven": 0,
                                                    "mileage": 0,
                                                    "owner": 0,
                                                    "power": 0
                                                    })
    assert response.status_code == 200
    assert response.json()['price'] > 0


def test_random_prediction():
    response = client.post('/v1/prediction', json={
                                                    "brand_name": "Bajaj",
                                                    "model_name": "Discover",
                                                    "motor_size": 100.0,
                                                    "years": 6,
                                                    "kms_driven": 80,
                                                    "mileage": 80,
                                                    "owner": 1,
                                                    "power": 7.7
                                                    })

    assert response.status_code == 200
    assert response.json()['price'] != 0 

    