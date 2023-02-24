import time
import math

#boilerplate
total_n = int(999_999)
i = 0
max_n = 0
max_count = 0
start_time = time.time()

#calculate
for i in range(total_n):
    n = i + 1
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        count += 1
    
    if count > max_count:
        max_count = count
        max_n = i

#print results
elapsed_time = math.floor((time.time()-start_time)*1000)

print(max_n, max_count, "?", elapsed_time, "ms")