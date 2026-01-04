import numpy as np

def dft(f):
    """
    1. dft(f) 正轉換
    計算公式: F[k] = sum_{n=0}^{N-1} f[n] * exp(-i * 2 * pi * k * n / N)
    """
    N = len(f)
    n = np.arange(N)
    k = n.reshape((N, 1))
    # 根據歐拉公式與傅立葉定義建立轉換矩陣
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, f)

def idft(F):
    """
    2. idft(F) 逆轉換
    計算公式: f[n] = (1/N) * sum_{k=0}^{N-1} F[k] * exp(i * 2 * pi * k * n / N)
    注意：離散版本的歸一化係數通常為 1/N
    """
    N = len(F)
    n = np.arange(N)
    k = n.reshape((N, 1))
    # 逆轉換的指數符號為正
    M = np.exp(2j * np.pi * k * n / N)
    return np.dot(M, F) / N

# --- 3. 驗證某函數 f ---

# 建立一個測試信號：包含頻率為 5Hz 和 10Hz 的正弦波
fs = 100  # 取樣頻率
t = np.linspace(0, 1, fs, endpoint=False)
f_original = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)

# 執行正轉換
F_transformed = dft(f_original)

# 執行逆轉換
f_reconstructed = idft(F_transformed)

# 驗證原始函數與逆轉換後的結果是否一致 (考慮數值誤差)
is_equal = np.allclose(f_original, f_reconstructed.real)

print(f"原始數據前 5 點: {f_original[:5]}")
print(f"逆轉換後前 5 點: {f_reconstructed.real[:5]}")
print(f"\n驗證結果：兩者是否一致? {is_equal}")
