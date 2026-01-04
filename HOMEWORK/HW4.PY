def f(coeffs, x):
    # 計算多項式 c[0] + c[1]*x + c[2]*x^2 + ...
    res = 0
    for i, c in enumerate(coeffs):
        res += c * (x ** i)
    return res

def hill_climbing_root(coeffs, start_x):
    curr_x = start_x
    step_size = 0.01  # 每次移動的步長
    
    for i in range(10000): # 最多嘗試一萬次
        curr_val = abs(f(coeffs, curr_x))
        
        next_x_right = curr_x + step_size
        next_x_left = curr_x - step_size
        
        # 看看左邊還是右邊比較好（絕對值更小）
        if abs(f(coeffs, next_x_right)) < curr_val:
            curr_x = next_x_right
        elif abs(f(coeffs, next_x_left)) < curr_val:
            curr_x = next_x_left
        else:
            # 左右都沒有更好，代表到山谷了
            break
            
    return curr_x

# 範例：f(x) = -4 + 0*x + 1*x^2  (即 x^2 - 4 = 0)
coeffs = [-4, 0, 1]
root = hill_climbing_root(coeffs, start_x=10)
print(f"找到的根大約是: {root:.4f}")
