import time
import math
def sqr(num, ms):
    time.sleep(ms / 1000)
    res = math.sqrt(num)
    return res

num = int(input())
delay = int(input())
res = sqr(num, delay)
print("Square root of", num, " after", delay, " milliseconds is", res)
