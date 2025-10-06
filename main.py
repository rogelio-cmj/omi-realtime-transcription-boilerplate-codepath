from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


@app.post("/webhook")
async def webhook(request: Request):
    # Get the raw JSON data
    try:
        data = await request.json()
        print("Received data:", data)
        
        uid = data.get("uid", "")
        transcript = data.get("transcript", {})

        # Hint: The transcript contains segments with text data
        # Hint: Access the latest segment with transcript["segments"][-1]["text"]
        # Hint: Return a dictionary with a "message" key and the value being the notification message

        # Task: Implement keyword detection and response logic of your choice
        # example: if the word "tired" is mentioned, return a message notifying the user to take a break

        # TODO: Write your code below this line
        
        # Get the latest transcript text
        if "segments" in transcript and len(transcript["segments"]) > 0:
            latest_text = transcript["segments"][-1]["text"].lower()
            
            # Define keyword detection rules
            keywords = {
                "tired": "💤 You sound tired! Consider taking a break to recharge.",
                "hungry": "🍕 Feeling hungry? Time for a snack or meal!",
                "stressed": "😰 Take a deep breath! Try a 5-minute meditation.",
                "excited": "🎉 Great energy! Keep that enthusiasm going!",
                "codepath": "💻 CodePath detected! You're doing awesome in your open source journey!",
                "open source": "🚀 Open source rocks! Keep contributing to the community!",
                "help": "🤝 Need assistance? Don't hesitate to ask for help!",
                "break": "☕ Taking a break is important for productivity!"
            }
            
            # Check for keywords and return appropriate message
            for keyword, message in keywords.items():
                if keyword in latest_text:
                    return {"message": message}
            
            # Default response if no keywords matched
            return {"message": f"📝 Transcribed: {transcript['segments'][-1]['text'][:50]}..."}
        
        # Return empty response if no segments
        return {"message": "👋 Listening..."}
    
    except Exception as e:
        print(f"Error processing webhook: {e}")
        return {"message": "👋 Received your message!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
