import numpy as np
from app.config import settings

def compute_scale(sensitivity: float, epsilon: float) -> float:
    """
    Compute the Laplace distribution scale parameter (b = sensitivity / epsilon).

    Args:
        sensitivity (float): Global sensitivity (Δf) - max impact of a single record.
        epsilon (float): Pricacy budget (ε) - controls privacy/utility trade-off.
    
    Returns:
        Scale parameter (b) for the Laplace distribution.
    
    Raises:
        ValueError: If epsilon or sensitivity are not positive.
    """
    if epsilon <= 0:
        raise ValueError(f"Epsilon must be positive, got {epsilon}.")
    if sensitivity <= 0:
        raise ValueError(f"Sensitivity must be positive, got {sensitivity}.")

    return sensitivity / epsilon


def add_laplace_noise(
        values: list[float],
        sensitivity: float = settings.default_sensitivity,
        epsilon: float = settings.default_epsilon
) -> dict:
    """
    Apply the Laplace mechanism to a list of numerical values for differential privacy.

    Args:
        values (list[float]): The numerical data to privatize.
        sensitivity (float): Global sensitivity (Δf).
        epsilon (float): Privacy budget (ε).
    
    Returns:
        Dictionary with noisy values and metadata.
    """
    scale = compute_scale(sensitivity, epsilon)

    noise = np.random.laplace(loc=0.0, scale=scale, size=len(values))

    original_values = np.array(values)
    noisy_values = original_values + noise

    return {
        "noisy_values": noisy_values.tolist(),
        "epsilon": epsilon,
        "sensitivity": sensitivity,
        "scale": round(scale, 6)
    }