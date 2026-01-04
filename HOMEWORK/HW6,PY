1.import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    # 使用一般式 ax + by + c = 0
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Circle:
    def __init__(self, center, r):
        self.center = center  # Point 物件
        self.r = r
2.兩直線的交點
def line_intersection(p1, p2, p3, p4):
    # x1, y1, x2, y2...
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    
    # 分母 (Denominator)
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None  # 平行或共線，無單一交點
    
    # 分子計算
    intersect_x = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
    intersect_y = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
    
    return (intersect_x, intersect_y)
  直線與圓的交點
import math

def line_circle_intersection(p1, p2, circle_center, r):
    cx, cy = circle_center
    x1, y1 = p1
    x2, y2 = p2
    
    # 向量化運算
    dx, dy = x2 - x1, y2 - y1
    f_x, f_y = x1 - cx, y1 - cy
    
    a = dx**2 + dy**2
    b = 2 * (f_x * dx + f_y * dy)
    c = (f_x**2 + f_y**2) - r**2
    
    # 判別式
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []  # 無交點
    
    discriminant = math.sqrt(discriminant)
    t1 = (-b - discriminant) / (2*a)
    t2 = (-b + discriminant) / (2*a)
    
    points = []
    # 若需判斷線段而非無限直線，需檢查 0 <= t <= 1
    for t in set([t1, t2]):
        points.append((x1 + t * dx, y1 + t * dy))
        
    return points
   兩個圓的交點
def circle_intersection(c1, r1, c2, r2):
    x1, y1 = c1
    x2, y2 = c2
    dx, dy = x2 - x1, y2 - y1
    d = math.sqrt(dx**2 + dy**2)
    
    if d > r1 + r2 or d < abs(r1 - r2) or d == 0:
        return [] # 不相交或重合
    
    # 這裡使用幾何法求解
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(max(0, r1**2 - a**2))
    
    # 找到兩圓心連線上的點 P2
    x2_prime = x1 + a * dx / d
    y2_prime = y1 + a * dy / d
    
    # 垂直偏移點
    rx = -dy * (h / d)
    ry = dx * (h / d)
    
    intersect1 = (x2_prime + rx, y2_prime + ry)
    intersect2 = (x2_prime - rx, y2_prime - ry)
    
    return list(set([intersect1, intersect2])) # 使用 set 處理切點（只有一個點的情況）
3、4.import numpy as np

# 1. 定義點與直線
# 直線由兩點 L1, L2 決定
P = np.array([3, 5])    # 線外一點
L1 = np.array([0, 0])   # 直線上的一點
L2 = np.array([8, 2])   # 直線上的另一點

# 2. 找出垂足 H (投影點)
# 向量 v 是直線方向，向量 w 是 L1 到 P 的位移
v = L2 - L1
w = P - L1

# 投影公式：H = L1 + (w ‧ v / v ‧ v) * v
projection = np.dot(w, v) / np.dot(v, v)
H = L1 + projection * v

# 3. 選取直線上的另一點 A (這裡直接用 L2)
A = L2

# 4. 計算邊長
a = np.linalg.norm(P - H)  # 股：P 到垂足的距離
b = np.linalg.norm(A - H)  # 股：A 到垂足的距離
c = np.linalg.norm(P - A)  # 斜邊：P 到 A 的距離

# 5. 驗證畢氏定理
lhs = a**2 + b**2
rhs = c**2

print(f"點 P 座標: {P}")
print(f"垂足 H 座標: {H}")
print(f"直線上的點 A 座標: {A}")
print("-" * 30)
print(f"股 a 的平方 (PH²): {lhs - b**2:.4f}")
print(f"股 b 的平方 (HA²): {b**2:.4f}")
print(f"a² + b² = {lhs:.4f}")
print(f"c² (斜邊 PA²)= {rhs:.4f}")
print(f"驗證結果: {np.isclose(lhs, rhs)}")
5.class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]
6.import math

class GeometryTransformer:
    @staticmethod
    def translate(point, dx, dy):
        """平移：將點移動 (dx, dy) 距離"""
        return Point(point.x + dx, point.y + dy)

    @staticmethod
    def scale(point, sx, sy, reference_point=None):
        """
        縮放：以參考點為中心進行縮放。
        若 reference_point 為 None，則以原點 (0,0) 為中心。
        """
        if reference_point is None:
            return Point(point.x * sx, point.y * sy)
        
        # 先移到原點，縮放後再移回去
        new_x = reference_point.x + (point.x - reference_point.x) * sx
        new_y = reference_point.y + (point.y - reference_point.y) * sy
        return Point(new_x, new_y)

    @staticmethod
    def rotate(point, angle_deg, center=None):
        """
        旋轉：將點繞著 center 旋轉 angle_deg 度（逆時針）。
        """
        angle_rad = math.radians(angle_deg)
        if center is None:
            center = Point(0, 0)
        
        # 相對座標
        temp_x = point.x - center.x
        temp_y = point.y - center.y
        
        # 旋轉矩陣運算
  
rotated_x = temp_x * math.cos(angle_rad) - temp_y * math.sin(angle_rad)
        rotated_y = temp_x * math.sin(angle_rad) + temp_y * math.cos(angle_rad)
        
        return Point(rotated_x + center.x, rotated_y + center.y)

# --- 套用到物件上的範例 ---

def transform_triangle(triangle, dx, dy, angle, scale_factor):
    # 1. 平移三角形的所有頂點
    moved_points = [GeometryTransformer.translate(p, dx, dy) for p in triangle.points]
    
    # 2. 以第一個頂點為中心旋轉
    center = moved_points[0]
    rotated_points = [GeometryTransformer.rotate(p, angle, center) for p in moved_points]
    
    # 3. 縮放
    final_points = [GeometryTransformer.scale(p, scale_factor, scale_factor, center) for p in rotated_points]
    
    return Triangle(*final_points)

def transform_circle(circle, dx, dy, scale_factor):
    # 圓的變換：平移中心點，縮放半徑
    new_center = GeometryTransformer.translate(circle.center, dx, dy)
    new_radius = circle.r * scale_factor
    return Circle(new_center, new_radius)
7.向量幾何： 直線可以看作點與法向量的集合。點積（Dot Product）可用於計算投影與垂直。

代數方程： 圓與線的關係本質上是二次方程的根。

線性代數： 平移、縮放、旋轉在電腦圖形學中通常使用 齊次座標 (Homogeneous Coordinates) 矩陣來統一處理。


