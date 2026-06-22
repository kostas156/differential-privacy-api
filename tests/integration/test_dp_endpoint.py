def test_add_noise_success(client):
    response = client.post(
        "/v1/dp/noise",
        json={"values": [1.0, 2.0, 3.0], "epsilon": 1.0, "sensitivity": 1.0}
    )
    assert response.status_code == 200
    data = response.json()
    assert "noisy_values" in data
    assert len(data["noisy_values"]) == 3
    assert data["epsilon"] == 1.0
    assert data["scale"] == 1.0


def test_add_noise_invalid_epsilon(client):
    response = client.post(
        "/v1/dp/noise",
        json={"values": [1.0], "epsilon": 0.0, "sensitivity": 1.0}
    )
    assert response.status_code == 422


def test_add_noise_empty_values(client):
    response = client.post(
        "/v1/dp/noise",
        json={"values": [], "epsilon": 1.0, "sensitivity": 1.0}
    )
    assert response.status_code == 422