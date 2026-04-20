import redis
import json
import os

REDIS_HOST = os.getenv("https://kind-pup-81297.upstash.io")
REDIS_PASSWORD = os.getenv("gQAAAAAAAT2RAAIncDE3NThmZGJhYjVlNDY0MWNmOTdkZTM5YWZkNmVhZjM0MnAxODEyOTc")

# If no Redis (local fallback)
if not REDIS_HOST:
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
else:
    r = redis.Redis(
        host=REDIS_HOST,
        port=6379,
        password=REDIS_PASSWORD,
        ssl=True,
        decode_responses=True
    )

def get_session(user_id):
    try:
        data = r.get(user_id)
        return json.loads(data) if data else {}
    except Exception as e:
        print("Redis Error:", e)
        return {}

def set_session(user_id, data):
    try:
        r.setex(user_id, 1800, json.dumps(data))
    except Exception as e:
        print("Redis Error:", e)
