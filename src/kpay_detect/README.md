# KPay Slip Detection API

A FastAPI-based backend service for detecting and extracting information from KPay payment slip images using OCR.

## Features

- Upload KPay slip images via a REST API.
- Automatic extraction of payer name, phone number, and amount using OCR (EasyOCR).
- CORS enabled for easy integration with frontend applications.

## Requirements

- Python 3.11+
- FastAPI
- Uvicorn
- OpenCV
- EasyOCR
- NumPy

Install dependencies:

```bash
pip install -r requirements.txt
```
Or, if using [pyproject.toml](../pyproject.toml):
```bash
pip install .
```

## Usage

1. **Start the API server:**
    ```bash
    uvicorn main:app --reload
    ```
    (Run this command inside the `src/kpay_detect` directory.)

2. **Upload a KPay slip:**
    - Send a `POST` request to `/upload` with a file (image) using a tool like Postman or `curl`:
    ```bash
    curl -F "file=@/path/to/your/kpay_slip.jpg" http://localhost:8000/upload
    ```

3. **Response:**
    - On success, you will receive a JSON response with extracted fields:
      ```json
      {
        "clean_amount": 10000,
        "name": "John Doe",
        "phone": "0912345678"
      }
      ```

## Project Structure

```
src/kpay_detect/
├── main.py            # FastAPI server and upload endpoint
├── kpay_processor.py  # Image processing and OCR logic
├── data/              # Uploaded images (temporary)
└── README.md
```

## Notes

- The API deletes uploaded images after processing.
- Extraction logic is tailored for typical KPay slip layouts; results may vary with different formats.
- For production, restrict `allow_origins` in CORS settings.
