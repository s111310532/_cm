import cmath

def root3(a, b, c, d):
    if a == 0:
        # 如果 a 為 0，則退化為二次方程式
        if b == 0:
            if c == 0: return []
            return [-d / c]
        delta_quad = c**2 - 4*b*d
        r1 = (-c + cmath.sqrt(delta_quad)) / (2*b)
        r2 = (-c - cmath.sqrt(delta_quad)) / (2*b)
        return [r1, r2]

    # 將方程式化為簡化形式 (Depressed Cubic): t^3 + pt + q = 0
    # 令 x = t - b/(3a)
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    
    # 計算判別式相關部分
    delta = (q/2)**2 + (p/3)**3
    
    # 計算立方根的兩個部分 u 和 v
    # u = cbrt(-q/2 + sqrt(delta)), v = cbrt(-q/2 - sqrt(delta))
    u_cube = -q/2 + cmath.sqrt(delta)
    v_cube = -q/2 - cmath.sqrt(delta)
    
    # 取得複數立方根 (可能有三個，我們選其中一個)
    u = u_cube**(1/3)
    
    # 為了確保 u*v = -p/3，我們計算 v
    if abs(u) != 0:
        v = -p / (3 * u)
    else:
        v = v_cube**(1/3)

    # 單位立方根 omega = e^(2*pi*i/3)
    w = cmath.exp(2j * cmath.pi / 3)
    
    # 計算 t 的三個根
    t1 = u + v
    t2 = u * w + v * (w**2)
    t3 = u * (w**2) + v * w
    
    # 轉換回原始變數 x = t - b/(3a)
    shift = b / (3 * a)
    roots = [t1 - shift, t2 - shift, t3 - shift]
    
    return roots

# 測試範例：x^3 - 6x^2 + 11x - 6 = 0 (根為 1, 2, 3)
a, b, c, d = 1, -6, 11, -6
results = root3(a, b, c, d)

print(f"方程式 {a}x^3 + {b}x^2 + {c}x + {d} = 0 的根為：")
for i, r in enumerate(results, 1):
    # 使用 round 處理浮點數微小誤差
    real = round(r.real, 10)
    imag = round(r.imag, 10)
    print(f"x{i}: {complex(real, imag)}")
