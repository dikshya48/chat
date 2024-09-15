import google.generativeai as ai
import tkinter as tk
import os

# Set up your API Key
API_KEY = 'AIzaSyDSSPKpuSWFjgJxJydT64_5o6lvGBVxsj0'
ai.configure(api_key=API_KEY)

# Function to interact with Google Chatbot
def send_message():
    message = user_input.get().strip()
    if not message:  # Check if the message is empty
        chat_window.insert(tk.END, "Chatbot: Please enter a message.\n")
        return
    if message.lower() == 'bye':
        chat_window.insert(tk.END, "Chatbot: Goodbye!\n")
        window.quit()
    else:
        try:
            # Use the chat model to send a message and receive a response
            response = ai.chat(text=message, model="chat-bison")
            chat_window.insert(tk.END, f'You: {message}\n')
            chat_window.insert(tk.END, f'Chatbot: {response["candidates"][0]["content"]}\n')
        except Exception as e:
            chat_window.insert(tk.END, f'Chatbot: Error: {str(e)}\n')
        user_input.delete(0, tk.END)
        chat_window.see(tk.END)  # Scroll to the end

# Set up the Tkinter window
window = tk.Tk()
window.title("Chatbot")

# Create a text area to display chat history
chat_window = tk.Text(window, height=25, width=100)
chat_window.pack()

# Create an input box for user text
user_input = tk.Entry(window, width=50)
user_input.pack()

# Create a send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Run the Tkinter event loop
window.mainloop()
