import numpy as np
import pytest
from ex2 import ( in_lattice, simple_rounding,
    Gram_Schmidt_orth, nearest_plane)
from generic_functions import in_span

np.random.seed(42)

# Generate random bases, targets, and diameters for testing
dimensions = [1, 2, 4]

instances_per_dim = 5  # number of instances per dimension

bases = []
for dim in dimensions:
    for _ in range(instances_per_dim):
        B = np.random.randint(-50, 50, size=(dim, dim))
        
        # Check if full rank
        if np.linalg.matrix_rank(B) == dim:
            bases.append(B)


@pytest.mark.parametrize("B", bases)
def test_in_lattice(B):
    n, _ = B.shape

    # Test known lattice points
    for _ in range(20):
        x = np.random.randint(-50, 50, size=n)
        v = x @ B
        assert in_lattice(B, v), f"Known lattice point {v} not recognized"

    # Test non-lattice points
    for _ in range(20):
        x = np.random.randint(-50, 50, size=n)
        v = x @ B + np.random.uniform(0.1, 0.9, size=B.shape[1])  # Add small non-integer shift
        assert not in_lattice(B, v), f"Non-lattice point {v} incorrectly accepted"

    # Test borderline numerical tolerance
    for _ in range(20):
        x = np.random.randint(-50, 50, size=n)
        v = x @ B + 1e-9 * np.random.randn(B.shape[1])  # Add tiny numerical noise
        assert in_lattice(B, v), f"Point {v} within tolerance was not accepted"

@pytest.mark.parametrize("B", bases)
def test_simple_rounding(B):
    n, _ = B.shape

    for _ in range(20):
        x = np.random.uniform(-50, 50, size=n)
        xr = np.round(x)

        if not np.allclose(x, xr, atol=0.499): # Avoid numerical borderline cases
            continue
        
        
        t = x @ B
        res = simple_rounding(B, t)

        assert res is not None, "Result is NaN value."
        assert in_lattice(B, res), "Result vector is not in the lattice."
        assert np.allclose(res, xr @ B)

@pytest.mark.parametrize("B", bases)
def test_gram_schmidt(B):
    Bs = Gram_Schmidt_orth(B)
    n, _ = B.shape

    assert Bs.shape == B.shape, f"Expected shape {B.shape}, got {Bs.shape}"
    assert np.allclose(B[0], Bs[0])

    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                assert np.allclose(Bs[i] @ Bs[j], 0), f"Bs{i} and Bs{j} are not orthogonal (1)."

    for i in range(1, n):
        for j in range(1, i):
            assert np.allclose(Bs[i] @ B[j], 0), f"B{i} and Bs{j} are not orthogonal (2)."
    
    for i in range(1, B.shape[0] + 1):
        # Is the i-th row of B in the span of the first i rows of Bs?
        assert in_span(Bs[:i, :], B[i-1, :]), f"Mismatch at row {i}"

        # Is the i-th row of Bs in the span of the first i rows of B?
        assert in_span(B[:i, :], Bs[i-1, :]), f"Mismatch at row {i}"
        
@pytest.mark.parametrize("B", bases)
def test_nearest_plane(B):
    n, _ = B.shape
    Bs = Gram_Schmidt_orth(B)

    for _ in range(20):
        x = np.random.uniform(-50, 50, size=n)
        t = x @ B
        v = nearest_plane(B, Bs, np.copy(t))

        assert in_lattice(B, v), "Result vector is not in the lattice."

        e = t - v
        for j in range(n):
            shadow = (e @ Bs[j]) / (Bs[j] @ Bs[j])
            assert shadow < 0.501 or shadow > 0.501
