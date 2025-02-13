import tkinter as tk
import requests

# FastAPI server URL
API_URL = "http://127.0.0.1:8000/chat"

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    # Display user message in the chat window
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_input}\n")
    chat_window.config(state=tk.DISABLED)

    # Send message to FastAPI backend
    try:
        response = requests.post(API_URL, json={"message": user_input})
        if response.status_code == 200:
            bot_response = response.json()["choices"][0]["message"]["content"]
            chat_window.config(state=tk.NORMAL)
            chat_window.insert(tk.END, f"Bot: {bot_response}\n")
            chat_window.config(state=tk.DISABLED)
        else:
            chat_window.config(state=tk.NORMAL)
            chat_window.insert(tk.END, f"Error: {response.text}\n")
            chat_window.config(state=tk.DISABLED)
    except Exception as e:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"Error: {str(e)}\n")
        chat_window.config(state=tk.DISABLED)

    # Clear the input field
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Cloudflare Chatbot")

# Chat window
chat_window = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Input field
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=10, fill=tk.X)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()