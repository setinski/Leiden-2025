import numpy as np
import matplotlib.pyplot as plt

# --- Matrix / vector generators ---

def gen_checkerboard(n, k):
    """Return an n x k checkerboard of 0s and 1s."""
    a = np.zeros((n,k), dtype=int)
    # the obvious solution
    #
    # for i in range(0,n):
    #     for j in range(0,k):
    #         if (j+i) % 2 == 1:
    #             a[i][j] = 1
    #
    # is slightly slower than:
    for j in range(1,k,2):
            a[0][j] = 1
            a[1][j-1] = 1
    for i in range(1,n):
            a[i,:] = a[i%2,:]
    return a

def gen_triangle_mat(n):
    """Return an n x n lower-triangular matrix of 1s."""
    a = np.zeros((n,n), dtype=int)
    for i in range(n):
        for j in range(i+1):
            a[i][j] = 1
    return a


def gen_rand_int(n, k, low, high):
    """Return an n x k matrix of random integers in [low, high)."""
    return np.random.randint(low,high,(n,k))

# --- Matrix manipulation ---

def reverse_rows(A):
    """Return a matrix with rows reversed."""
    B = A.copy()
    i = 0
    for row in A:
        B[i,:] = row[::-1]
        i += 1
    return B


def modify_diags(A):
    """Swap main and the anti-diagonal."""
    i = 0
    B = A.copy()
    for row in A:
        B[i,i] = row[-i-1]
        B[i,-i-1] = row[i]
        i += 1
    return B

# --- Linear algebra ---

def project(x, y):
    """Return the projection of a (vector) x onto the direction of y."""
    return (x@y)/(y@y)*y 


def check_orthonormal(x, y):
    """Check if two vectors are orthonormal (orthogonal + unit length).
    Returns True if they are orthonormal, False otherwise."""
    return x @ y == 0


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

    # Step 1: Generate a random linear system
    # Generate a random M that is invertible, i.e. det(M) != 0), 
    # and a random vector vector b.
    M = np.random.rand(n, n)
    np.fill_diagonal(M, np.sum(np.abs(M), axis=1))
    # this ensures that M is diagonally dominant and hence invertible
    b = np.random.rand(n)

    # Step 2: Perform eigen-decomposition of M
    # Make use of numpy's eigenvalue decomposition function np.linalg.eig,
    # and the numpy function np.diag.
    v,P = np.linalg.eig(M)
    D = np.diag(1/v) # inverse of eigenvalues
    print(D)
    Pinv = np.linalg.inv(P)

    # Step 3: Express b in the eigenbasis
    bprime = Pinv @ b

    # Step 4: Solve in eigenbasis (diagonal system)
    y = D @ bprime

    # Step 5: Map back to original space
    x = P @ y

    # Step 6: Verification
    # If result is correct return all relevant variables: M, x, b
    if np.all([M@x, b]):
        return M, x, b
    
    return None, None, None



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

    # # 1. Checkerboard
    # print("\n1. Checkerboard:")
    # cb = gen_checkerboard(8, 8)
    # print(cb)
    # plot_checkerboard(cb)
    # input("Press Enter to continue...")

    # # 2. Lower-triangular
    # print("\n2. Lower-triangular matrix (5x5):")
    # tri = gen_triangle_mat(5)
    # print(tri)
    # input("Press Enter to continue...")

    # # 3. Lower-triangular
    # print("\n3. Random matrix (5x5) with values from [1,5):")
    # rand_mat = gen_rand_int(5, 5, 1, 5)
    # print(rand_mat)
    # input("Press Enter to continue...")

    # # 4. Reverse rows
    # print("\n4. Reverse rows:")
    # mat3 = np.arange(1, 10).reshape(3, 3)
    # rev = reverse_rows(mat3)
    # print("Original matrix:\n", mat3)
    # print("Reversed rows matrix:\n", rev)
    # input("Press Enter to continue...")

    # # 5. Swap diagonals
    # print("\n5. Swap main and anti-diagonal:")
    # mat4 = np.arange(1, 10).reshape(3, 3)
    # swapped = modify_diags(mat4)
    # print("Original matrix:\n", mat4)
    # print("Swapped matrix:\n", swapped)
    # input("Press Enter to continue...")

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
    M, b, x = solve_via_eigenbasis(n=4)
    
    print("\n--- Summary of Transformed Space Solution ---")
    print("Original system M:\n", M)
    print("Right-hand side b:", b)
    print("Mapped-back solution x:", x)
