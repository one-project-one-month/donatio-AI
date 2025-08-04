# FROM python:3.11-slim

# WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     gcc \
#     g++ \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt .


# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 8001

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

FROM python:3.11-slim

WORKDIR /app/src/chatbot

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY src/chatbot/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src/chatbot/ ./

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
