import redis
import json
import os

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    password=os.getenv("REDIS_PASSWORD", None),
    ssl=True if os.getenv("REDIS_HOST") else False,
    decode_responses=True
)

def get_session(user_id):
    data = r.get(user_id)
    return json.loads(data) if data else {}

def set_session(user_id, data):
    r.setex(user_id, 1800, json.dumps(data))  # TTL = 30 mins
