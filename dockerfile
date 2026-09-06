FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

# Install CPU-only PyTorch + torchvision
RUN pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    torch torchvision

# Install the rest
COPY requirementsCPU.txt .
RUN pip install --no-cache-dir -r requirementsCPU.txt

COPY . .

WORKDIR /app/backend

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "predictAPI:app", "--host", "0.0.0.0", "--port", "8000"]