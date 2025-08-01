#!/bin/bash

# Donatio AI Docker Build Script

echo "Building Donatio AI Docker containers..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Warning: .env file not found. Please create one with your environment variables."
    echo "Required variables: DATABASE_URL, GROQ_API_KEY"
fi

echo "📦 Building and starting services..."
docker-compose up --build -d

echo "Services are starting up!"
echo ""
echo "Services will be available at:"
echo "   KPay Detection: http://localhost:8000"
echo "   SQL Chatbot:    http://localhost:8001"
echo ""
echo "API Documentation:"
echo "   KPay Detection: http://localhost:8000/docs"
echo "   SQL Chatbot:    http://localhost:8001/docs"
echo ""
echo "To stop services: docker-compose down"
echo "To view logs: docker-compose logs -f" 