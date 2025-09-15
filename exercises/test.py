import numpy as np
import matplotlib.pyplot as plt

# --- Matrix / vector generators ---

# Temporary changes
def gen_checkerboard(n, k):
        """Return an n x k checkerboard of 0s and 1s."""
        A = np.ones((n,k))
        for i in range(n):
                t = i%2
                for j in range(t,k,2):
                        A[i][j] = 0
        return A


def gen_triangle_mat(n):
        """Return an n x n lower-triangular matrix of 1s."""
        A = np.ones((n,n))
        for i in range(n):
                for j in range(i):
                         A[i][j] = 0
        return A


def gen_rand_int(n, k, low, high):
        """Return an n x k matrix of random integers in [low, high)."""
        #A = np.zeros((n,k))
        #for i in range(n):
        #       A[i] = np.random.randint(low, high, k)
        A = np.random.randint(low, high, (n,k))
        return A


# --- Matrix manipulation ---

def reverse_rows(A):
        """Return a matrix with rows reversed."""
        n = A.shape[0]
        k = A.shape[1]
        B = np.ones((n,k))
        for i in range(n):
                for j in range(k):
                        B[i][j] = A[i][k-j-1]
        return B


def modify_diags(A):
        """Swap main and the anti-diagonal."""
        B = A.copy()
        n = A.shape[0]
        for i in range(n):
                B[i][i] = A[i][n-i-1]
                B[i][n-i-1] = A[i][i]
        return B

# --- Linear algebra ---

def project(x, y):
    """Return the projection of a (vector) x onto the direction of y."""
    return (x @ y)/(y @ y) * y


def check_orthonormal(x, y):
    """Check if two vectors are orthonormal (orthogonal + unit length).
    Returns True if they are orthonormal, False otherwise."""
    return np.allclose(x @ y, 0) and np.allclose(np.linalg.norm(x), 1) and np.allclose(np.linalg.norm(y), 1)


def linear_map(A, x):
    """Apply a linear map defined by matrix A to vector x."""
    return A @ x


def inverse_map(A, y):
        """Apply the inverse of a linear map defined by matrix A to vector y."""
        return np.linalg.inv(A) @ y


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


    pass

    # Step 2: Perform eigen-decomposition of M
    # Make use of numpy's eigenvalue decomposition function np.linalg.eig,
    # and the numpy function np.diag.
    pass

    # Step 3: Express b in the eigenbasis
    pass

    # Step 4: Solve in eigenbasis (diagonal system)
    pass  # elementwise division since D y = b'

    # Step 5: Map back to original space
    pass

    # Step 6: Verification
    pass  # check if M @ x == b

    # If result is correct return all relevant variables: M, x, b



# --- Plotting ---

def plot_matrix(A, title="Matrix", cmap="viridis"):
    plt.imshow(A, cmap=cmap, interpolation='nearest')
    plt.colorbar()
    plt.title(title)
    plt.show()

def plot_checkerboard(A):
    plt.imshow(A, cmap="gray", interpolation='nearest')
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
    #plot_checkerboard(cb)

    input("Press Enter to continue...")

    # 2. Lower-triangular
    print("\n2. Lower-triangular matrix (5x5):")
    tri = gen_triangle_mat(5)
    print(tri)
    # plot_matrix(tri, title="Lower-triangular")
    input("Press Enter to continue...")

    # 3. Reverse rows
    print("\n3. Reverse rows:")
    mat3 = np.arange(1, 10).reshape(3, 3)
    rev = reverse_rows(mat3)
    print("Original matrix:\n", mat3)
    print("Reversed rows matrix:\n", rev)
    # plot_matrix(rev, title="Rows reversed")
    input("Press Enter to continue...")

    # 4. Swap diagonals
    print("\n4. Swap main and anti-diagonal:")
    mat4 = np.arange(1, 10).reshape(3, 3)
    swapped = modify_diags(mat4)
    print("Original matrix:\n", mat3)
    print("Swapped matrix:\n", swapped)
    # plot_matrix(swapped, title="Diagonals swapped")
    input("Press Enter to continue...")

    # 4.5 Random matrix
    print("Return an n x k matrix of random integers in [low, high):")
    mat45 = gen_rand_int(5,5,0,30)
    print(mat45)
    input("Press Enter to continue...")

    # 5. Linear mapping and inverse mapping
    print("\n6. Linear mapping and inverse mapping:")
    A = np.array([[2, 0], [0, 3]])
    x = np.array([1, 4])
    y = linear_map(A, x)
    x_new = inverse_map(A, y)
    if np.allclose(x, x_new):
        print("Inverse mapping successful!")
    else:
        print("Inverse mapping failed!")
    input("Press Enter to continue...")

    # 6. Projections
    print("\n8. Projection:")
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

    # 7. Solve via transformed space
    print("\n10. Solve random system via transformed space:")

    # Call the function and capture all results
    M, b, x = solve_via_eigenbasis(n=4)

    print("\n--- Summary of Transformed Space Solution ---")
    print("Original system M:\n", M)
    print("Right-hand side b:", b)
    print("Mapped-back solution x:", x)
    print("This is a test message")
