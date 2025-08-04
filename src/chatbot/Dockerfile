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
# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY src/chatbot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code
COPY src/chatbot/ .

# Expose port (change if your FastAPI app uses a different one)
EXPOSE 8000

# Run the FastAPI app (adjust if your file or app is different)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
