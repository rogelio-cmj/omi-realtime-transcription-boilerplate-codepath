# OMI Integration App - Realtime Transcription 

A FastAPI webhook server for receiving and processing data from OMI. Example boilerplate for CodePath opensource students

## Features

- FastAPI webhook endpoint at `/webhook`
- CORS middleware enabled for all origins
- Processes transcript data and user IDs
- Real-time data handling

## Installation

### 1. Install uv

**uv** is an extremely fast Python package installer and resolver, written in Rust. It's a drop-in replacement for pip and pip-tools that's 10-100x faster.

**Install uv:** Follow the installation instructions at [https://docs.astral.sh/uv/getting-started/installation/#standalone-installer](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

### 2. Install Project Dependencies

```bash
uv sync
```

This will:
- Create a virtual environment automatically
- Install all dependencies from `pyproject.toml`
- Lock the exact versions in `uv.lock`

## Running the API

**Important:** Run these steps in order.

### 1. First, start the FastAPI server

```bash
uv run main.py
```

The server will start on `http://127.0.0.1:8000`

*What does `uv run` do?* - Automatically activates the virtual environment and runs the file with correct dependencies.

### 2. Then, set up ngrok tunnel

**Why ngrok?** - Your local server needs to be accessible from the internet for OMI webhooks to work.

**Setup ngrok:** [https://dashboard.ngrok.com/get-started/setup/macos](https://dashboard.ngrok.com/get-started/setup/macos)

**Create tunnel** (in a new terminal):
```bash
ngrok http 8000
```

You'll see output like:
```
ngrok                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                        
Visit http://localhost:4040 for ngrok dashboard                                                                                                                                                                                        

Session Status                online                                                                                                                                                                                                    
Account                       your-account (Plan: Free)                                                                                                                                                                                
Version                       3.x.x                                                                                                                                                                                                     
Region                        United States (us)                                                                                                                                                                                        
Latency                       -                                                                                                                                                                                                         
Web Interface                 http://127.0.0.1:4040                                                                                                                                                                                    
Forwarding                    https://abc123.ngrok.io -> http://localhost:8000                                                                                                                                                         

Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                                                                                               
                              0       0       0.00    0.00    0.00    0.00
```

#### Use the public URL

The webhook endpoint is the forwarding URL plus `/webhook`:

- **Forwarding URL:** `https://abc123.ngrok.io`
- **Webhook Endpoint:** `https://abc123.ngrok.io/webhook`

**Copy this complete webhook URL and paste it into the OMI app** as your webhook endpoint. This is the URL that OMI will use to send transcript data to your local server.

## Student Assignment

### Task: Implement Keyword Detection

1. **Open `main.py`** and find the TODO section in the webhook function
2. **Implement keyword detection logic** - check if specific words appear in the transcript
3. **Return custom notification messages** based on detected keywords
