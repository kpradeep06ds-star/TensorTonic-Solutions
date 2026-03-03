import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if len(x) == len(p):
        if not np.isclose(np.sum(p), 1.0, atol=1e-6):
            raise ValueError("Values are higher than 1")
        return np.dot(x, p)
    else:
        raise ValueError("Shapes do not match")
