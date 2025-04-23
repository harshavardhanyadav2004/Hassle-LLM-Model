# Property Assistant API

A FastAPI-based application that provides two AI-powered services for property management:
1. **Issue Detection Agent** - Analyzes property images to identify problems
2. **Tenancy FAQ Agent** - Answers common questions related to tenancy

## Architecture

The application runs in a Docker container and connects to a local Ollama instance running AI models:
- **llava** model for image analysis
- **gemma:2b** model for answering tenancy FAQs

## Prerequisites

- Ubuntu 22.04 LTS (or compatible Linux distribution)
- Docker and Docker Compose
- Ollama running with the required models

## Hardware Requirements

Tested on an Azure D4_v3 VM with:
- 4 CPUs
- 16 GiB RAM

## Installation & Setup

### 1. Set up Ollama

Install Ollama and pull the required models:

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull required models
ollama pull llava
ollama pull gemma:2b

# Start Ollama server
ollama serve
```

### 2. Deploy the API

Clone this repository:

```bash
git clone https://github.com/yourusername/property-assistant-api.git
cd property-assistant-api
```

Build and run the Docker container:

```bash
docker build -t property-assistant-api .
docker run -d -p 8000:8000 --name property-assistant property-assistant-api
```

## API Endpoints

### POST /chat

A single endpoint that determines which agent to use based on whether an image is uploaded:

**Request:**
- `prompt`: Text query (required)
- `file`: Image file (optional)

**Response:**
```json
{
  "agent": "Issue Detection Agent|Tenancy FAQ Agent",
  "response": "AI-generated response"
}
```

## Usage Examples

### Analyzing Property Images

```bash
curl -X POST "http://localhost:8000/chat" \
  -F "prompt=What issues can you see in this kitchen?" \
  -F "file=@kitchen_image.jpg"
```

### Answering Tenancy Questions

```bash
curl -X POST "http://localhost:8000/chat" \
  -F "prompt=What are my rights as a tenant regarding repairs?"
```

## Architecture Diagram

```
┌─────────────┐     ┌───────────────────┐     ┌─────────────────────┐
│ Client      │────▶│ FastAPI Container │────▶│ Ollama Container    │
│ (HTTP POST) │     │ (Port 8000)       │     │ (Port 11434)        │
└─────────────┘     └───────────────────┘     └─────────────────────┘
                            │                           │
                            ▼                           ▼
                    ┌──────────────────┐       ┌──────────────────┐
                    │ Issue Detection  │       │ AI Models        │
                    │ or Tenancy FAQ   │       │ - llava          │
                    │ Agent            │       │ - gemma:2b       │
                    └──────────────────┘       └──────────────────┘
```

## Files Structure

- `main.py` - FastAPI application entry point
- `image_analysis.py` - Issue Detection Agent logic
- `tenancy_faq.py` - Tenancy FAQ Agent logic
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container build instructions

## Development

To run the project locally without Docker:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
## Access the backend Documentation using the Azure vm ip

```bash

http://20.84.56.193:8000/docs#/default

```
