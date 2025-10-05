import numpy as np
import matplotlib.pyplot as plt

# --- Matrix / vector generators ---

def gen_checkerboard(n, k):
    """Return an n x k checkerboard of 0s and 1s."""
    A = np.zeros((n,k), dtype=int)

    for i in range(n):
        for j in range(k):
            A[i,j] = (i+j)%2

    return A


def gen_triangle_mat(n):
    """Return an n x n lower-triangular matrix of 1s."""
    A = np.zeros((n,n), dtype=int)
    for i in range(n):
        for j in range(i):
            A[i,j] = 1

    return A


def gen_rand_int(n, k, low, high):
    """Return an n x k matrix of random integers in [low, high)."""
    A = np.random.randint(low=low, high=high, size=(n,k))

    return A


# --- Matrix manipulation ---

def reverse_rows(A):
    """Return a matrix with rows reversed."""
    n,_ = A.shape

    B = A.copy()
    #return A[:,::-1]

    B[:,::1] = A[:,::-1]
    return B

def modify_diags(A):
    """Swap main and the anti-diagonal."""
    B = A.copy()
    n,_ = B.shape

    for i in range(n):
        B[i,i] = A[i,n-1-i]
        B[i,n-1-i] = A[i,i]

    return B

# --- Linear algebra ---

def project(x, y):
    """Return the projection of a (vector) x onto the direction of y."""

    return (x@y)/(y@y)*y


def check_orthonormal(x, y):
    """Check if two vectors are orthonormal (orthogonal + unit length).
    Returns True if they are orthonormal, False otherwise."""

    return np.allclose(x@x,1) and np.allclose(x@y, 0) and np.allclose(y@y, 1)


def linear_map(A, x):
    """Apply a linear map defined by matrix A to vector x."""

    return A@x


def inverse_map(A, y):
    """Apply the inverse of a linear map defined by matrix A to vector y."""
    B = np.linalg.inv(A)
    return B@y


def solve_via_eigenbasis(n=4):
    """
    Solve a random linear system M x = b using the eigenbasis.
    1. Generate random invertible M and vector b.
    2. Compute eigen-decomposition M = P D P^{-1}.
    3. Transform system: M' = D (diagonal), b' = P^{-1} b.
    4. Solve M' y = b' for y (easy since M' is diagonal).
    5. Map back x = P y.
    6. Verify solution.
    """
    print("\n--- Solve in Eigenbasis ---")

    # Step 1: Generate a radnom linear system
    # Generate a random M that is invertible, i.e. det(M) != 0),
    # and a random vector vector b.
    M = np.random.uniform(size=(n,n))
    while np.allclose(np.linalg.det(M),0):
        M = np.random.uniform(size=(n,n))
    b = np.random.rand(n)

    # Step 2: Perform eigen-decomposition of M
    # Make use of numpy's eigenvalue decomposition function np.linalg.eig,
    # and the numpy function np.diag.
    eigval, Pt = np.linalg.eig(M)
    D = np.diag(eigval)
    P = np.linalg.inv(Pt)
    H = (Pt@D)@P

    # Step 3: Express b in the eigenbasis
    bp = P@b

    # Step 4: Solve in eigenbasis (diagonal system)
    y = bp/eigval

    # Step 5: Map back to original space
    x = Pt@y

    # Step 6: Verification
    xp = np.linalg.solve(M,b)
    if not np.allclose(xp, x):
        #print("Expected answer:", xp, "found: ", x)
        return
    else:
        # If result is correct return all relevant variables: M, x, b
        return M,x,b



# --- Plotting ---

def plot_matrix(A, title="Matrix", cmap="viridis"):
    plt.imshow(A, cmap=cmap, interpolation='nearest')
    plt.colorbar()
    plt.title(title)
    plt.show()

def plot_checkerboard(A):
    plt.imshow(A, cmap="gray", interpolation='nearest')
    plt.title("Checkerboard / Chessboard")
    plt.show()

# --- Main testing ---

if __name__ == "__main__":

    # 1. Checkerboard
    print("\n1. Checkerboard:")
    cb = gen_checkerboard(8, 8)
    print(cb)
    plot_checkerboard(cb)

    input("Press Enter to continue...")

    # 2. Lower-triangular
    print("\n2. Lower-triangular matrix (5x5):")
    tri = gen_triangle_mat(5)
    print(tri)
    input("Press Enter to continue...")

    # 3. Lower-triangular
    print("\n3. Random matrix (5x5) with values from [1,5):")
    rand_mat = gen_rand_int(5, 5, 1, 5)
    print(rand_mat)
    input("Press Enter to continue...")

    # 4. Reverse rows
    print("\n4. Reverse rows:")
    mat3 = np.arange(1, 10).reshape(3, 3)
    rev = reverse_rows(mat3)
    print("Original matrix:\n", mat3)
    print("Reversed rows matrix:\n", rev)
    input("Press Enter to continue...")

    # 5. Swap diagonals
    print("\n5. Swap main and anti-diagonal:")
    mat4 = np.arange(1, 10).reshape(3, 3)
    swapped = modify_diags(mat4)
    print("Original matrix:\n", mat4)
    print("Swapped matrix:\n", swapped)
    input("Press Enter to continue...")

    # 6. Projections
    print("\n6. Projection:")
    v = np.array([3, 4])
    u = np.array([1, 0])
    z = np.array([0, 1])

    proj_v_onto_u = project(v, u)
    proj_v_onto_z = project(v, z)

    v_new = proj_v_onto_u * u + proj_v_onto_z * z

    if check_orthonormal(u, z):
        if np.allclose(v, v_new):
            print("Projection successful!")
    input("Press Enter to continue...")

    # 7. Linear mapping and inverse mapping
    print("\n7. Linear mapping and inverse mapping:")
    A = np.array([[2, 0], [0, 3]])
    x = np.array([1, 4])
    y = linear_map(A, x)
    x_new = inverse_map(A, y)
    if np.allclose(x, x_new):
        print("Inverse mapping successful!")
    else:
        print("Inverse mapping failed!")
    input("Press Enter to continue...")

    # 8. Solve via transformed space
    print("\n8. Solve random system via transformed space:")

    # Call the function and capture all results
    M, x, b = solve_via_eigenbasis(n=4)

    print("\n--- Summary of Transformed Space Solution ---")
    print("Original system M:\n", M)
    print("Right-hand side b:", b)
    print("Mapped-back solution x:", x)
