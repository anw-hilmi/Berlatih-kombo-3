FROM python:3.10-slim

WORKDIR /app

# Salin requirements dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin model.pkl dan app.py saja (Ignore lainnya via .dockerignore)
COPY model.pkl .
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]