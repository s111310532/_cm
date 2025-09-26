import cmath

def root2(a, b, c):

    D = b**2 - 4*a*c
    
    root1 = (-b + cmath.sqrt(D)) / (2*a)
    root2 = (-b - cmath.sqrt(D)) / (2*a)
    
    def f(x):
        return a*x**2 + b*x + c
    
    if cmath.isclose(f(root1), 0, rel_tol=1e-9, abs_tol=0.0):
        print(f"root1 = {root1} ✅ 通過驗證")
    else:
        print(f"root1 = {root1} ❌ 驗證失敗")
    
    if cmath.isclose(f(root2), 0, rel_tol=1e-9, abs_tol=0.0):
        print(f"root2 = {root2} ✅ 通過驗證")
    else:
        print(f"root2 = {root2} ❌ 驗證失敗")
    
    return root1, root2

print(root2(1, -3, 2))   # x^2 - 3x + 2 = 0, roots = 1, 2
print(root2(1, 2, 5))    # x^2 + 2x + 5 = 0, roots = -1±2j
