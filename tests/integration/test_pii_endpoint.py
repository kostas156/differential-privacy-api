def test_mask_pii_success(client):
    response = client.post(
        "/v1/pii/mask",
        json={"text": "My email is hello@example.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "masked_text" in data
    assert "[EMAIL_ADDRESS]" in data["masked_text"]
    assert "detection_count" in data


def test_mask_pii_empty_text(client):
    response = client.post(
        "/v1/pii/mask",
        json={"text": ""}
    )
    assert response.status_code == 422


def test_mask_pii_missing_text(client):
    response = client.post(
        "/v1/pii/mask",
        json={}
    )
    assert response.status_code == 422