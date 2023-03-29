import numpy as np

def jacobi_method(A, b, x_init, tol=10e-7, max_iter=100):
    n = len(A)
    x = x_init
    x_new = np.zeros(n)

    for k in range(max_iter):
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += A[i, j] * x[j]
            x_new[i] = (b[i] - s) / A[i, i]

        print(f"Iterasi ke-{k+1}: {x_new}")
        
        #if np.linalg.norm(x_new - x) < tol:
        if np.all(np.abs(x_new - x) < tol):
            print(f"Konvergensi tercapai pada iterasi ke-{k+1}")
            return x_new
        x = x_new.copy()

    raise RuntimeError(f"Jacobi method did not converge after {max_iter} iterations")

if __name__ == "__main__":
    A = np.array([
        [4, -1, 1],
        [4, -8, 1],
        [-2, 1, 5]
    ])

    b = np.array([7, -21, 15])

    x_init = np.array(list(map(float, input("Masukkan vektor solusi awal (pisahkan dengan spasi): ").split())))
    
    x = jacobi_method(A, b, x_init)
    print("Solution:", np.round(x,6))
    #print("Residual:", np.linalg.norm(A @ np.round(x,3) - b))