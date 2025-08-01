# Donatio AI

A comprehensive AI-powered donation management system with KPay slip detection and SQL chatbot capabilities.

## Project Overview

This project consists of two main components:

1. **KPay Slip Detection** - Automatically extracts donation amounts from KPay payment slips
2. **SQL Chatbot** - Intelligent chatbot for querying donation database with role-based access

## Project Structure

```
donatio-AI/
├── src/
│   ├── kpay_detect/          # KPay slip detection service
│   │   ├── main.py           # FastAPI server for KPay processing
│   │   ├── kpay_processor.py # Core KPay slip processing logic
│   │   ├── data/             # Sample images for testing
│   │   └── README.md         # KPay-specific documentation
│   └── chatbot/              # SQL chatbot service
│       ├── main.py           # FastAPI server for SQL chatbot
│       └── requirements.txt   # Python dependencies
├── test/                     # Test files
└── pyproject.toml           # Project configuration
```

## Prerequisites

- Python 3.8+
- UV package manager (recommended) or pip
- Environment variables configured (see Setup section)

## Setup

### 1. Install Dependencies

Using UV (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -r src/chatbot/requirements.txt
```

### 2. Environment Variables

Create a `.env` file in the project root:

```env
# Database connection for SQL chatbot
DATABASE_URL=your_database_connection_string

# Groq API key for LLM
GROQ_API_KEY=your_groq_api_key
```

### 3. Database Setup

Ensure your database is running and accessible via the `DATABASE_URL` environment variable.

## Running the Services

### KPay Slip Detection Service

Start the KPay detection service:

```bash
cd src/kpay_detect
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The service will be available at `http://localhost:8000`

#### API Endpoints

- **POST** `/upload` - Upload and process KPay slip images
  - **Request**: Multipart form with image file
  - **Response**: JSON with extracted amount and metadata

#### Example Usage

```bash
curl -X POST "http://localhost:8000/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/kpay_slip.jpg"
```

### SQL Chatbot Service

Start the SQL chatbot service:

```bash
cd src/chatbot
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

The service will be available at `http://localhost:8001`

#### API Endpoints

- **POST** `/generate` - Generate SQL-based responses
  - **Request Body**:
    ```json
    {
      "sender_role": "donar" | "organization",
      "question": "Your question here"
    }
    ```
  - **Response**: Natural language answer based on database query

#### Example Usage

```bash
curl -X POST "http://localhost:8001/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "sender_role": "donar",
    "question": "What are my recent donations?"
  }'
```

## Features

### KPay Slip Detection

- **Automatic Amount Extraction**: Extracts donation amounts from KPay payment slips
- **Image Processing**: Handles various image formats and qualities
- **Temporary File Management**: Automatically cleans up uploaded files
- **Error Handling**: Comprehensive error handling and validation

### SQL Chatbot

- **Role-Based Access**: Different responses for donors vs organizations
- **Natural Language Processing**: Converts questions to SQL queries
- **Intelligent Responses**: Provides human-like answers based on database results
- **Memory Management**: Maintains conversation context
- **Structured Output**: Ensures reliable SQL query generation

## Development

### Running Tests

```bash
python -m pytest test/
```

### Code Structure

- **KPay Detection**: Uses FastAPI, processes images with OCR
- **SQL Chatbot**: Uses LangGraph for conversation flow, Groq for LLM, LangChain for database integration

## API Documentation

Once the services are running, you can access the interactive API documentation:

- KPay Service: `http://localhost:8000/docs`
- SQL Chatbot: `http://localhost:8001/docs`

