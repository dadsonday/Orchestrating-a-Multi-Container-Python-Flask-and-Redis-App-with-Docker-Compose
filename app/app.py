from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis connection
redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def home():
    count = r.incr("visits")
    return f"Hello! This page has been visited {count} times.Like and follow CloudDaemon"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

