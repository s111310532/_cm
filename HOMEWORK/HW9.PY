1.線性指的是滿足兩個性質：加法性 f(x+y) = f(x) + f(y)$與 齊次性 f(cx) = cf(x)。
代數意指用「符號」來代表數值或運算。線性代數就是研究如何透過矩陣和向量這些符號，來系統化地解決線性方程組的問題。
2.空間在數學中，是指一個集合，並在這個集合上定義了某些結構，向量空間提供了一個「舞台」，讓向量可以在其中進行線性組合，且結果仍在這個舞台內。
3.向量可以看作是 n*1 的矩陣。矩陣最直觀的意義是線性變換，它是一個函數，把一個空間中的向量映射(映射/轉換)到另一個空間中。
4.縮放與旋轉：可以直接用2*2或3*3矩陣表示。
平移： 線性變換必須固定原點，但平移會移動原點，因此它屬於「仿射變換」。為了用矩陣表達平移，我們會引入齊次坐標，將 2D 提升到 3D 空間來運算。
5.行列式代表變換後的 「體積縮放比例」。若 |A| = 2，代表變換後的圖形面積/體積變為原來的 2 倍。若 |A| = 0，代表空間發生了壓縮，例如 3D 壓成了一個平面
6-10.特徵值分解 (EVD)： 尋找變換中「方向不變」的向量（特徵向量）以及其「縮放倍數」（特徵值）。這常用於了解系統的長期穩定性。
QR 分解： 將矩陣分解為一個正交矩陣 $Q$ 和上三角矩陣 $R$。它是數值計算（如求特徵值）的基礎。
SVD 分解： 線性代數的「巔峰」。它能將任何矩陣（不限方陣）分解，揭示數據在不同維度上的重要性。
PCA (主成分分析)： 數據降維技術。其背後的數學原理就是對協方差矩陣進行特徵值分解或直接對數據進行 SVD。
1.import numpy as np

def recursive_det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        # 取得子矩陣 (移除第 0 列與第 j 行)
        sub_matrix = np.delete(np.delete(matrix, 0, axis=0), j, axis=1)
        # 餘因式展開
        det += ((-1)**j) * matrix[0][j] * recursive_det(sub_matrix)
    return det

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"遞迴計算結果: {recursive_det(A)}")
2.from scipy.linalg import lu

def lu_det(matrix):
    P, L, U = lu(matrix)
    # P 是置換矩陣，其行列式為 1 或 -1 (取決於交換次數)
    det_P = np.linalg.det(P) 
    det_U = np.diag(U).prod()
    return det_P * det_U

A = np.random.rand(5, 5)
print(f"LU 分解計算法: {lu_det(A)}")
3.from scipy.linalg import lu, eig, svd

A = np.array([[4, 11, 14], [8, 7, -2], [3, 1, 0]])

# 1. LU
P, L, U = lu(A)
print("LU 驗證:", np.allclose(P @ L @ U, A))

# 2. 特徵值分解 (A = VΛV⁻¹)
vals, vecs = eig(A)
print("Eig 驗證:", np.allclose(vecs @ np.diag(vals) @ np.linalg.inv(vecs), A))

# 3. SVD (A = UΣVᴴ)
U_svd, s, Vh = svd(A)
print("SVD 驗證:", np.allclose(U_svd @ np.diag(s) @ Vh, A))
4.def svd_via_eig(A):
    # 計算 A.T @ A
    ATA = A.T @ A
    # 特徵值分解
    eigenvalues, V = np.linalg.eigh(ATA)
    
    # 排序特徵值（由大到小）
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    V = V[:, idx]
    
    # 計算奇異值
    s = np.sqrt(np.maximum(eigenvalues, 0))
    
    # 計算 U = A * V * Σ⁻¹
    U = A @ V / s
    
    return U, s, V.T

A = np.array([[1, 2], [3, 4], [5, 6]])
U, s, Vh = svd_via_eig(A)
print("手作 SVD 奇異值:", s)
5.def manual_pca(X, n_components):
    # 1. 去中心化 (Standardization)
    X_centered = X - np.mean(X, axis=0)
    
    # 2. 計算協方差矩陣
    cov_matrix = np.cov(X_centered.T)
    
    # 3. 特徵值分解
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    
    # 4. 排序並選擇前 k 個特徵向量
    idx = eigenvalues.argsort()[::-1]
    top_eigenvectors = eigenvectors[:, idx[:n_components]]
    
    # 5. 將原數據投影到新空間
    return X_centered @ top_eigenvectors

# 測試
X = np.random.rand(100, 5) # 100個樣本, 5個特徵
reduced_X = manual_pca(X, 2)
print("降維後數據形狀:", reduced_X.shape)
