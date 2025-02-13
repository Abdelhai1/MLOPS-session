from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Cloudflare AI API configuration
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/ai/run/"
headers = {"Authorization": "Bearer API_TOKEN"}

# Define the model to use
MODEL = "@cf/meta/llama-3-8b-instruct"

class ChatRequest(BaseModel):
    message: str

def run_cloudflare_ai(model, inputs):
    """
    Sends a request to the Cloudflare AI API and returns the response.
    """
    input_data = {"messages": inputs}
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input_data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Prepare the input for the model
        inputs = [
            {"role": "system", "content": "You are a friendly assistant that helps users with their queries."},
            {"role": "user", "content": request.message},
        ]

        # Call the Cloudflare AI API
        response = run_cloudflare_ai(MODEL, inputs)

        # Extract the bot's response
        bot_response = response.get("result", {}).get("response", "No response generated.")
        return {"choices": [{"message": {"content": bot_response}}]}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)