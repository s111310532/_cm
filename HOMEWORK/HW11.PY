import numpy as np

def solve_ode_general(coefficients):
    """
    求解常係數齊次常微分方程: a_n*y^(n) + ... + a_1*y' + a_0*y = 0
    參數 coefficients: 串列 [a_n, a_{n-1}, ..., a_0]
    """
    # 1. 提取特徵方程式的根
    # numpy.roots 接受多項式係數並回傳所有根（包含重根與複數根）
    roots = np.roots(coefficients)
    
    # 2. 統計根的出現次數（處理重根問題）
    # 由於浮點數運算可能有誤差，使用 round 處理
    unique_roots, counts = np.unique(np.round(roots, 10), return_counts=True)
    
    solution_terms = []
    c_index = 1
    
    for root, count in zip(unique_roots, counts):
        # 處理複數根 (alpha + bi)
        if np.iscomplex(root):
            # 複數根通常成對出現，我們只處理正虛部的那一個來構建 sin/cos
            if root.imag > 0:
                alpha = root.real
                beta = root.imag
                for p in range(count):
                    t_factor = f"x^{p} * " if p > 0 else ""
                    solution_terms.append(f"e^({alpha}x) * ({t_factor}C{c_index}*cos({beta}x) + {t_factor}C{c_index+1}*sin({beta}x))")
                    c_index += 2
        else:
            # 處理實數根
            real_root = root.real
            for p in range(
