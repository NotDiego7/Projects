import time

print(time.localtime().tm_sec)

secs = time.time()
print(time.localtime(secs))