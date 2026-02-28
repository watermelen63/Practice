# 🔹 檢查字串、一串數字或list中有幾個重複最多的字元:
from collections inport Counter
Counter(variable).most_common(1)[0][1]

# 🔹 切片:
Python內建函數(不須import)
variable[begin:end:間隔]
ex.
n = input()
n1 = n[0:1]
print(n1)

# 🔹 heapq — 最小堆（小頂堆）
讓你可以快速地找出最小值

函式用法：

heapq.heapify(list)：把 list 變成 min-heap。

heapq.heappop(heap)：從 heap 中取出最小的元素。

heapq.heappush(heap, item)：把新元素加入 heap，保持 heap 結構。

# 🔹 bisect — 二分搜尋模組（Binary Search）
用來在已排序的列表中快速查找插入位置或查找元素。

## 函式用法（語意版說明）：
### ✅ bisect.bisect_right(alive_stages_list, current_stage_index)：
在 alive_stages_list 中，找到 current_stage_index 右邊的插入點。
➡ 用來找「下一個還有沙包的關卡」。

### ✅ bisect.bisect_left(alive_stages_list, current_stage_index)：
在 alive_stages_list 中，找到 current_stage_index 正確的位置（若要刪除用這個）。
➡ 通常用來移除關卡，例如當沙包被搬完後，要把該關卡從列表中移除。

# 🔹 .ljust(value)
把字串向右補空到value的長度

# 🔹 .rjust(value)
把字串向左補空到value的長度

# 🔹math
在使用之前必須先import math
Python 的 `math` 模組包含大量數學相關函式，以下整理最常用的並分類：

---

## ✅ **數學常數**

* `math.pi`：圓周率 π (≈ 3.141592653589793)
* `math.e`：自然常數 e (≈ 2.718281828459045)
* `math.tau`：圓常數 τ (2π)
* `math.inf`：正無窮大
* `math.nan`：非數值 NaN

---

## ✅ **基本運算**

* `math.ceil(x)`：向上取整數
* `math.floor(x)`：向下取整數
* `math.trunc(x)`：截斷小數（取整數部分）
* `math.fabs(x)`：取絕對值（回傳浮點數）
* `math.factorial(x)`：階乘 x!
* `math.gcd(a, b)`：最大公因數（GCD）
* `math.lcm(a, b)`：最小公倍數（Python 3.9+）
* `math.copysign(x, y)`：取 x 的絕對值並附上 y 的符號

---

## ✅ **冪次與對數**

* `math.pow(x, y)`：x 的 y 次方
* `math.sqrt(x)`：平方根
* `math.exp(x)`：e^x
* `math.log(x)`：自然對數 ln(x)
* `math.log10(x)`：以 10 為底對數
* `math.log2(x)`：以 2 為底對數
* `math.log(x, base)`：任意底對數

---

## ✅ **三角函數**

* `math.sin(x)`、`math.cos(x)`、`math.tan(x)`
* `math.asin(x)`、`math.acos(x)`、`math.atan(x)`
* `math.atan2(y, x)`：回傳點 (x, y) 的角度（處理象限）
* `math.hypot(x, y)`：計算 √(x² + y²)

---

## ✅ **弧度與角度轉換**

* `math.radians(x)`：度數轉弧度
* `math.degrees(x)`：弧度轉度數

---

## ✅ **雙曲函數**

* `math.sinh(x)`、`math.cosh(x)`、`math.tanh(x)`
* `math.asinh(x)`、`math.acosh(x)`、`math.atanh(x)`

---

## ✅ **浮點數操作**

* `math.isfinite(x)`：是否有限數值
* `math.isinf(x)`：是否無窮大
* `math.isnan(x)`：是否 NaN
* `math.modf(x)`：回傳小數部分與整數部分（tuple）
* `math.frexp(x)`：分解浮點數為 (尾數, 指數)
* `math.ldexp(x, i)`：計算 x \* (2^i)
* `math.fsum(iterable)`：精確浮點和（比 `sum()` 精準）
* `math.prod(iterable)`：序列連乘（Python 3.8+）
* `math.nextafter(x, y)`：x 向 y 方向的下一個浮點數
* `math.ulp(x)`：單位最小值（距離下一個浮點數）

---

## ✅ **距離與幾何**

* `math.dist(p, q)`：計算兩點距離（Python 3.8+）
* `math.hypot(*coordinates)`：計算多維歐氏距離

---

### 🔥 **總結**

* **數論**：`gcd`, `lcm`, `factorial`
* **浮點運算**：`fsum`, `prod`
* **幾何與距離**：`hypot`, `dist`

---

# 🔹list comprehension
List = [x]

# NumPy
