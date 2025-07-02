### 运行fast api
```bash
pip install fastapi

pip install "uvicorn[standard]"

uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir /root/td_backend

docker run --rm -p 8000:8000 detect:v1.0 uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir /root/td_backend
# docker run --rm -d -p 8000:8000 detect:v1.0 uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir /root/td_backend

nohup gunicorn -w 4 -b 0.0.0.0:8006 -k uvicorn.workers.UvicornWorker main:app >log.out 2>&1 &
```
