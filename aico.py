import tkinter as tk
from tkinter import scrolledtext
import cohere

# Initialize the Cohere client
api_key = 'use your own'
co = cohere.Client(api_key)

def send_message():
    user_message = user_input.get("1.0", tk.END).strip()
    if user_message:
        conversation.insert(tk.END, f"You: {user_message}\n")
        user_input.delete("1.0", tk.END)
        
        try:
            # Get response from Cohere
            response = co.generate(
                model='command-xlarge-nightly',
                prompt=user_message,
                max_tokens=50
            )
            ai_message = response.generations[0].text.strip()
            conversation.insert(tk.END, f"AI: {ai_message}\n")
        except Exception as e:
            conversation.insert(tk.END, f"Error: {e}\n")

# Create the main window
window = tk.Tk()
window.title("Cohere AI Chat")

# Create a scrolled text widget for the conversation
conversation = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='normal', width=50, height=20)
conversation.pack(padx=10, pady=10)

# Create a text widget for user input
user_input = tk.Text(window, height=3, width=50)
user_input.pack(padx=10, pady=(0, 10))

# Create a button to send the message
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=(0, 10))

# Start the Tkinter event loop
window.mainloop()
