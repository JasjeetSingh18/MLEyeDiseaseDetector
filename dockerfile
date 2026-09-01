FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Python deps
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Run from backend folder so import "predict" works
WORKDIR /app/backend

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "predictAPI:app", "--host", "0.0.0.0", "--port", "8000"]