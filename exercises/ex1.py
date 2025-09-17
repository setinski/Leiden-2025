import numpy as np
import matplotlib.pyplot as plt

# --- Matrix / vector generators ---

def gen_checkerboard(n, k):
    """Return an n x k checkerboard of 0s and 1s."""
    m = np.ones((n,k))
    for i in range(n):
        for j in range(k):
            if j % 2 == i % 2:
                m[i,j] = 0
    return m

def gen_triangle_mat(n):
    """Return an n x n lower-triangular matrix of 1s."""
    m = np.ones((n,n))
    for i in range(n):
        for j in range(n):
            if i < j:
                m[i,j] = 0
    return m

def gen_rand_int(n, k, low, high):
    """Return an n x k matrix of random integers in [low, high)."""
    m = np.ones((n,k))
    for i in range(n):
        for j in range(k):
            m[i,j] = np.random.randint(low, high)
    return m

# --- Matrix manipulation ---

def reverse_rows(A):
    """Return a matrix with rows reversed."""
    B = np.copy(A)
    v = A.shape
    n = v[0]
    k = v[1]
    for i in range(n):
        for j in range(k):
            A[i,j] = B[i,k-j-1]
    return A

def modify_diags(A):
    """Swap main and the anti-diagonal."""
    B = np.copy(A)
    v = A.shape
    n = v[0]
    k = v[1]
    m = min(n,k)
    for i in range(m):
        A[i,k-i-1] = B[i,i]
        A[i,i] = B[i,k-i-1]
    return A

# --- Linear algebra ---

def project(x, y):
    """Return the projection of a (vector) x onto the direction of y."""
    yy = 0
    xy = 0
    s = 0
    if x.shape == y.shape:
        n = x.shape[0]
        for i in range(n):
            yy = yy + y[i]*y[i]
            xy = xy + x[i]*y[i]
        s = xy / yy
        for i in range(n):
            x[i] = s*y[i]
    return x

def check_orthonormal(x, y):
    """Check if two vectors are orthonormal (orthogonal + unit length).
    Returns True if they are orthonormal, False otherwise."""
    d = 0
    u = 0
    v = 0
    if x.shape == y.shape:
        n = x.shape[0]
        for i in range(n):
            d = d + x[i]*y[i]
            u = u + x[i]*x[i]
            v = v + y[i]*y[i]
        if d == 0 and np.sqrt(u) == 1 and np.sqrt(v) == 1:
            return True
        else: return False

def linear_map(A, x):
    """Apply a linear map defined by matrix A to vector x."""
    return A @ x

def inverse_map(A, y):
    """Apply the inverse of a linear map defined by matrix A to vector y."""
    B = np.linalg.inv(A)
    return B @ y

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
    low = -10 #Is it possible to use -infinity here ...
    high = 10 # ...and infinity here?
    m = gen_rand_int(n, n, low, high)
    while np.linalg.det(m) == 0:
        m = gen_rand_int(n, n, low, high)
    b = gen_rand_int(n, 1, low, high)

    # Step 2: Perform eigen-decomposition of M
    # Make use of numpy's eigenvalue decomposition function np.linalg.eig,
    # and the numpy function np.diag.
    d = np.diag(np.linalg.eig(m)[0])

    # Step 3: Express b in the eigenbasis
    p = np.linalg.eig(m)[1]
    bprime = inverse_map(p,b)

    # Step 4: Solve in eigenbasis (diagonal system)
    y = np.linalg.solve(d,bprime)
    #y = np.zeros((n,1))
    #for i in range(n):
    #    y[i] = bprime[i]/d[i,i]
    # I think it doesn't work since the complex numbers do not get divided correctly,
    # but I don't see how I can solve it.

    # Step 5: Map back to original space
    x = linear_map(p, y)

    # Step 6: Verification
    bb = linear_map(m, x)

    # If result is correct return all relevant variables: M, x, b
    if bb.all() == b.all():
        return m, x, b
    else: return None, None, None

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
    #plot_checkerboard(cb)
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
    M, b, x = solve_via_eigenbasis(n=4)
    
    print("\n--- Summary of Transformed Space Solution ---")
    print("Original system M:\n", M)
    print("Right-hand side b:", b)
    print("Mapped-back solution x:", x)
