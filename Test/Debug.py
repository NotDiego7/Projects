import time

# print(time.localtime().tm_sec)

# secs = time.time()
# print(time.localtime(secs))

def delay(function):
    time.sleep(5.0)
    return function()

@delay
def say_hello():
    print('Hello, world.')

say_hello()