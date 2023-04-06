import numpy as np

def gauss_seidel_method(A, b, x_init, tol=1e-6, max_iter=100):
    n = len(A)
    x = x_init.copy()

    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += A[i, j] * x[j]
            x[i] = (b[i] - s) / A[i, i]

        print(f"Iterasi ke-{k+1}: {x}")

        if np.all(np.abs(x - x_old) < tol):
            print(f"Konvergensi tercapai pada iterasi ke-{k+1}")
            return x

    raise RuntimeError(f"Gauss-Seidel method did not converge after {max_iter} iterations")

if __name__ == "__main__":
    A = np.array([
        [4, -1, 1],
        [4, -8, 1],
        [-2, 1, 5]
    ])

    b = np.array([7, -21, 15])

    x_init = np.array(list(map(float, input("Masukkan vektor solusi awal (pisahkan dengan spasi): ").split())))

    x = gauss_seidel_method(A, b, x_init)
    print("Solution:", np.round(x,6))
    #print("Residual:", np.linalg.norm(A @ x - b))