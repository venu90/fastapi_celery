# FastAPI + Celery + Redis Demo

## Features
- Background task processing using Celery
- Redis as broker and cache
- FastAPI endpoints

## Endpoints
- GET /add?x=1&y=2
- GET /result/{task_id}
- GET /cached/{key}

## Run

Start Redis:
redis-server

or 
docker run -d -p 6379:6379 redis

Start API:
uvicorn app:app --reload

Start Worker:
celery -A app.celery_app worker --pool=solo --loglevel=info





-------------------------

git usage---

git init
git add .
git commit -m "Initial commit: FastAPI + Celery + Redis project"
git remote add origin https://github.com/your-username/fastapi-celery-redis-demo.git
git branch -M main
git push -u origin main

--next changes to fiel or added fies
git add .
git commit -m "Added README"
git push