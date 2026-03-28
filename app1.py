from fastapi import FastAPI, Body
from celery import Celery
import time
import redis

# -----------------------------
# 🔹 Celery Configuration
# -----------------------------
celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# -----------------------------
# 🔹 Redis Cache Client
# -----------------------------
redis_client = redis.Redis(host="localhost", port=6379, db=1)

# -----------------------------
# 🔹 Background Task
# -----------------------------
@celery_app.task
def heavy_task(x, y):
    print("Processing task...")
    time.sleep(5)  # simulate heavy work
    return x + y

# -----------------------------
# 🔹 FastAPI App
# -----------------------------
app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

# -----------------------------
# 🔹 Trigger Background Task
# -----------------------------
@app.get("/add")
def add(x: int, y: int):
    task = heavy_task.delay(x, y)
    return {"task_id": task.id}

# -----------------------------
# 🔹 Check Task Result
# -----------------------------
@app.get("/result/{task_id}")
def get_result(task_id: str):
    result = celery_app.AsyncResult(task_id)
    return {
        "status": result.status,
        "result": result.result
    }

# -----------------------------
# 🔹 Redis Cache Example
# -----------------------------
@app.get("/cached/{key}")
def get_cached(key: str):
    value = redis_client.get(key)

    if value:
        return {"cached": True, "value": value.decode()}

    # simulate expensive computation
    value = f"computed-{key}"
    redis_client.setex(key, 60, value)

    return {"cached": False, "value": value}

# -----------------------------
# 🔹 POST version (better API)
# -----------------------------
@app.post("/add")
def add_post(data: dict = Body(...)):
    x = data.get("x")
    y = data.get("y")

    task = heavy_task.delay(x, y)
    return {"task_id": task.id}