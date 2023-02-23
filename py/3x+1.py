import time
t1 = time.time()
max_count = 0
max_i = 0
for i in range(1000):
    count = 0
    n = i
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    
    if count > max_count:
        max_count = count
        max_i = i

print(max_i, max_count)
print(time.time() - t1)