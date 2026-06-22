import pytest
from app.core.privacy.laplace import compute_scale, add_laplace_noise

def test_compute_scale_correct():
    assert compute_scale(sensitivity=1.0, epsilon=0.5) == 2.0

def test_compute_scale_invalid_epsilon():
    with pytest.raises(ValueError):
        compute_scale(sensitivity=1.0, epsilon=0.0)

def test_compute_scale_invalid_sensitivity():
    with pytest.raises(ValueError):
        compute_scale(sensitivity=0.0, epsilon=1.0)

def test_add_laplace_noise_output_length():
    values = [1.0, 2.0, 3.0]
    result = add_laplace_noise(values=values, sensitivity=1.0, epsilon=1.0)
    assert len(result["noisy_values"]) == len(values)

def test_add_laplace_noise_returns_correct_metadata():
    result = add_laplace_noise(values=[100.0], sensitivity=2.0, epsilon=0.5)
    assert result["epsilon"] == 0.5
    assert result["sensitivity"] == 2.0
    assert result["scale"] == 4.0

def test_add_laplace_noise_values_different_from_original():
    values = [1000.0] * 100
    result = add_laplace_noise(values=values, sensitivity=1.0, epsilon=0.01)
    assert any(v != 1000.0 for v in result["noisy_values"])