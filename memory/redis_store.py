import redis
import json


r=redis.Redis(
    host="your-host",
    port=6379,
    password="your-password",
    decode_responses=True
)

def get_session(user_id):
    data = r.get(user_id)
    return json.loads(data) if data else {}

def set_session(user_id, data):
    r.setex(user_id, 1800, json.dumps(data))
