1、2.import math

p = 0.5
n = 10000

# 1. 直接計算 (結果通常會是 0.0)
direct_prob = p ** n
print(f"1. 直接計算結果: {direct_prob}")

# 2. 使用對數計算
# log10(0.5^10000) = 10000 * log10(0.5)
log_prob = n * math.log10(p)
print(f"2. Log10 計算結果: {log_prob}")
print(f"   這代表機率大約是 10 的 {log_prob:.2f} 次方")
3、4.import numpy as np

def get_metrics(p, q):
    p = np.array(p) + 1e-12 # 加上極小值防止 log(0)
    q = np.array(q) + 1e-12
    
    entropy = -np.sum(p * np.log2(p))
    cross_entropy = -np.sum(p * np.log2(q))
    kl_divergence = np.sum(p * np.log2(p / q))
    # 互資訊 (Mutual Information) 需要聯合機率分佈，此處簡化示意
    
    return entropy, cross_entropy, kl_divergence

# 驗證第 4 題
p_dist = [0.5, 0.5]
q_dist = [0.8, 0.2]

h_p, h_pq, kl = get_metrics(p_dist, q_dist)
print(f"熵 H(p): {h_p:.4f}")
print(f"交叉熵 H(p, q): {h_pq:.4f}")
print(f"KL 散度: {kl:.4f}")
print(f"驗證: H(p, q) > H(p, p) 是 {h_pq > h_p}")
5.def hamming_74_encode(data):
    # 假設 data 為 4 個 bits 的列表，如 [1, 0, 1, 1]
    d1, d2, d3, d4 = data
    p1 = d1 ^ d2 ^ d4  # 檢查位 1
    p2 = d1 ^ d3 ^ d4  # 檢查位 2
    p3 = d2 ^ d3 ^ d4  # 檢查位 3
    # 標準排列通常為: [p1, p2, d1, p3, d2, d3, d4]
    return [p1, p2, d1, p3, d2, d3, d4]

def hamming_74_decode(received):
    # 接收到的 7 位元: [r1, r2, r3, r4, r5, r6, r7]
    r1, r2, r3, r4, r5, r6, r7 = received
    s1 = r1 ^ r3 ^ r5 ^ r7
    s2 = r2 ^ r3 ^ r6 ^ r7
    s3 = r4 ^ r5 ^ r6 ^ r7
    
    error_pos = s1 * 1 + s2 * 2 + s3 * 4
    if error_pos != 0:
        print(f"偵測到第 {error_pos} 位元錯誤，正在修正...")
        received[error_pos-1] ^= 1
        
    return [received[2], received[4], received[5], received[6]]
6.夏農信道編碼定理:任何一個通道都有一個極限傳輸速率，稱為通道容量 (Channel Capacity, C)。
只要你的傳輸速率 R < C，就一定存在一種編碼方式，可以讓傳輸錯誤率無限趨近於零。
如果 R > C，則無論如何設計編碼，都無法保證無誤傳輸。
夏農-哈特利定理:這是針對連續信號計算通道容量的公式，C = B \log_2(1 + \frac{S}{N})
