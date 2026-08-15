from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_detect_endpoint():
    response = client.post("/api/detect", json={"essay": "This is a simple test essay. It has multiple sentences. It should return a valid response."})
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "confidence" in data
    assert "overall_score" in data
    assert "sentence_highlights" in data
    assert len(data["sentence_highlights"]) == 3
    assert data["sentence_highlights"][0]["sentence"] == "This is a simple test essay."

def test_health_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "detector-api"}
