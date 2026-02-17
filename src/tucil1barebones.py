import time
from collections import defaultdict


filename = input("Masukkan nama file (.txt): ")
try:
    with open(filename, "r") as f:
        matrice = [line.strip() for line in f if line.strip() != ""]
except:
    print("File tidak ditemukan.")
    exit()

n = len(matrice)
if n == 0:
    print("Input kosong.")
    exit()

for row in matrice:
    if len(row) != n:
        print("Board tidak valid (harus NxN).")
        exit()

coords = defaultdict(list)
for y in range(n):
    for x in range(n):
        coords[matrice[y][x]].append((x, y))
colors = list(coords.keys())
if len(colors) != n:
    print("Jumlah warna harus sama dengan ukuran board.")
    exit()

c = len(colors)
solution = []

def solve():
    temp = len(solution)
    if temp==c:
        check(solution.copy())
    else:
        for i in coords[colors[temp]]:
            solution.append(i)
            solve()
            solution.pop()

iter_count = 0
ans = []
def check(case):
    global iter_count

    print(f"Iter[#{iter_count}]: ", end="")
    for x, y in case:
        print(f"({x},{y})", end=" ")
    
    rows = set()
    cols = set()
    valid = True
    # check per baris dan kolom
    for x, y in case:
        if x in cols or y in rows:
            valid = False
            break
        cols.add(x)
        rows.add(y)
    # check radius 1 (8 arah sekitar)
    for i in range(len(case)):
        x1, y1 = case[i]
        for j in range(i+1, len(case)):
            x2, y2 = case[j]
            if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
                valid = False
                break
        if not valid:
            break

    if valid:
        ans.append(case.copy())
        print(" [VALID]")
    else:
        print(" [NOT VALID]")
    iter_count += 1

# Main
start_time = time.time()
solve()
end_time = time.time()
elapsed_ms = (end_time - start_time) * 1000
print("---------------------------------------------------------------------------------------")
print(f"Valid solutions: {len(ans)}")
print("SOLUTIONS:")
if len(ans) == 0:
    print("No valid solutions")
else:
    for i in ans:
        print(i)
print(f"Time needed: {elapsed_ms}ms")
print(f"Iterations: {iter_count}")


