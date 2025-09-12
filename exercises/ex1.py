import numpy as np
import matplotlib.pyplot as plt

#test edit
# --- Matrix / vector generators ---

def gen_checkerboard(n, k):
    a=np.ones((n,k), dtype=int)
    for i in range (0,k):
        for j in range(0,n):
            if (i+j)%2 == 0:
                a[i,j]=0
    return(a)
    """Return an n x k checkerboard of 0s and 1s."""


def gen_triangle_mat(n):
    """Return an n x n lower-triangular matrix of 1s."""
    a=np.zeros((n,n), dtype=int)
    for i in range (0,n):
        for j in range(0,n):
            if j<=i:
                a[i,j]=1
    return(a)


def gen_rand_int(n, k, low, high):
    """Return an n x k matrix of random integers in [low, high)."""
    A = np.random.randint(low, high, size=(n, k))
    return(A)

# --- Matrix manipulation ---

def reverse_rows(A):
    """Return a matrix with rows reversed."""
    n=A.shape[0]
    B=A.copy()
    for i in range(0,n):
        B[i,:]=A[n-i-1,:]
    return(B)


def modify_diags(A):
    """Swap main and the anti-diagonal."""
    n = A.shape[0]
    B = A.copy()
    for i in range (0,n):
        B[i,i]=A[i, n-i-1]
        B[i,n-i-1]=A[i,i]  
    return B

# --- Linear algebra ---

def project(x, y):
    """Return the projection of a (vector) x onto the direction of y."""
    z=y*(x@y)/(y@y)
    return z


def check_orthonormal(x, y):
    if (np.allclose(x@y,0) and np.allclose(np.linalg.norm(x),1) and np.allclose(np.linalg.norm(y),1)):
        return True
    """Check if two vectors are orthonormal (orthogonal + unit length).
    Returns True if they are orthonormal, False otherwise."""


def linear_map(A, x):
    """Apply a linear map defined by matrix A to vector x."""
    B=A@x
    return B


def inverse_map(A, y):
    """Apply the inverse of a linear map defined by matrix A to vector y."""
    B=np.linalg.inv(A)@y
    return B


def solve_via_eigenbasis(n):
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
    # Generate a random M that is invertible, i.e. det(M) != 0, 
    # and a random vector vector b.
    M=np.zeros((n,n))
    while np.linalg.det(M)==0:
        M= np.random.randint(0, 10, size=(n, n))
        eigenvalues, eigenvectors=np.linalg.eig(M)
        if np.linalg.matrix_rank(eigenvectors) == n:
            continue
        break
    b = np.random.randint(0, 10, size=n)

    # Step 2: Perform eigen-decomposition of M
    # Make use of numpy's eigenvalue decomposition function np.linalg.eig,
    # and the numpy function np.diag.
    D=np.diag(eigenvalues)
    P=np.array(eigenvectors)

    # Step 3: Express b in the eigenbasis
    c=np.linalg.inv(P)@ b

    # Step 4: Solve in eigenbasis (diagonal system)
    y=np.zeros(n, dtype=complex)
    for i in range(0,n):
        y[i]=c[i]/D[i,i]
    # elementwise division since D y = b'

    # Step 5: Map back to original space
    x=P@y

    # Step 6: Verification # check if M @ x == b
    if np.allclose(M@x, b):
        return M,b,x
    else: return 0,0,0
    # If result is correct return all relevant variables: M, x, b



# --- Plotting ---

def plot_matrix(A, title="Matrix", cmap="viridis"):
    plt.imshow(A, cmap=cmap, interpolation='nearest')
    plt.colorbar()
    plt.title(title)
    plt.show()

def plot_checkerboard(A):
    print(cb)

    plt.imshow(A, cmap="gray", interpolation='nearest')
    plt.title("Checkerboard / Chessboard")
    plt.show()

# --- Main testing ---

if __name__ == "__main__":

    # 1. Checkerboard
    print("\n1. Checkerboard:")
    cb = gen_checkerboard(8, 8)
    plot_checkerboard(cb)

    input("Press Enter to continue...")

    # 2. Lower-triangular
    print("\n2. Lower-triangular matrix (5x5):")
    tri = gen_triangle_mat(5)
    print(tri)
    # plot_matrix(tri, title="Lower-triangular")
    input("Press Enter to continue...")

    # 3. Reverse rows
    print("\n3. Reverse rows:")
    mat3 = gen_rand_int(3, 3, 1, 10)
    rev = reverse_rows(mat3)
    print("Original matrix:\n", mat3)
    print("Reversed rows matrix:\n", rev)
    # plot_matrix(rev, title="Rows reversed")
    input("Press Enter to continue...")

    # 4. Swap diagonals
    print("\n4. Swap main and anti-diagonal:")
    mat4 = gen_rand_int(3, 3, 1, 10)
    swapped = modify_diags(mat4)
    print("Original matrix:\n", mat4)
    print("Swapped matrix:\n", swapped)
    # plot_matrix(swapped, title="Diagonals swapped")
    input("Press Enter to continue...")

    # 5. Linear mapping and inverse mapping
    print("\n5. Linear mapping and inverse mapping:")
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

    # 7. Solve via transformed space
    print("\n7. Solve random system via transformed space:")
    
    # Call the function and capture all results
    M, b, x = solve_via_eigenbasis(4)
    
    print("\n--- Summary of Transformed Space Solution ---")
    print("Original system M:\n", M)
    print("Right-hand side b:", b)
    print("Mapped-back solution x:", x)

