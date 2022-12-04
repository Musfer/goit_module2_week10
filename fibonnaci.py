import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def fibonacci(x):
    print(f"Calling f({x})")
    if x in (0, 1):
        return 1
    return fibonacci(x-1) + fibonacci(x-2)


if __name__ == "__main__":
    for i in range(50):
        print(f"fibonacci({i})={fibonacci(i)}")
