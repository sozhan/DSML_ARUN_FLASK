from predictions import app
import pytest
import json

@pytest.fixture
def client():
    return app.test_client()

def test_pinger(client):
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"MESSAGE": "Hi I am pinging V2...."}

def test_predictions(client):
    test_data = {
    "Gender": "Male",
    "Married": "Yes",
    "ApplicantIncome": 500,
    "LoanAmount": 50000000,
    "Credit_History": 1.0
    }
    resp = client.post('/predict', json= test_data)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status": 'Rejected'}
