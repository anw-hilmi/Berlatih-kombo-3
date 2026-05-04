FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
# Upgrade pip dulu agar lebih stabil
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY model.pkl .
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]