import google.generativeai as ai
import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage

# Google API Configuration
API_KEY = 'AIzaSyCry02qgple8zxa86lbRglzYo6rQcmox_I'  # Your API key here
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# Load images for user (human) and bot (chatbot)

def load_images():
    user_image = PhotoImage(file="human.png")  # User image (human logo)
    bot_image = PhotoImage(file="chatbot.png")  # Bot image (chatbot logo)

    # Resize the images using subsample (reduce the image size)
    user_image = user_image.subsample(9, 9)  # Decrease by a factor of 4 (adjust as needed)
    bot_image = bot_image.subsample(9, 9)    # Decrease by a factor of 4 (adjust as needed)

   



    return user_image, bot_image

def send_message():
    message = str(user_input.get())
    if message.lower() == 'bye':
        chat_window.insert(tk.END, "Goodbye!\n", "user_text")
        window.quit()
    else:
        response = chat.send_message(message)
        
        # Format the response text to remove unwanted characters and replace new lines
        response_text = response.text.replace('*', '').replace(':', '').replace('\n', ' ')
        response_text = ' '.join(response_text.split())  # Normalize spaces
        
        # Split the response into sentences
        sentences = response_text.split('.')  # Split the text by sentences (after each period)
        sentences = [sentence.strip() + '.' for sentence in sentences if sentence]  # Clean up each sentence

        # Ensure there are at least 8 sentences (for 2 paragraphs with 4 sentences each)
        if len(sentences) >= 8:
            first_paragraph = ' '.join(sentences[:4])  # First paragraph (4 sentences)
            second_paragraph = ' '.join(sentences[4:8])  # Second paragraph (4 sentences)
        else:
            # If fewer sentences, balance them between two paragraphs
            split_index = len(sentences) // 2
            first_paragraph = ' '.join(sentences[:split_index])
            second_paragraph = ' '.join(sentences[split_index:])
        
        # Insert the two paragraphs into the chat window with images
        chat_window.image_create(tk.END, image=user_image)  # Insert user image
        chat_window.insert(tk.END, f' You: {message}\n', "user_text")
        chat_window.image_create(tk.END, image=bot_image)  # Insert bot image
        chat_window.insert(tk.END, f' Bot:\n{first_paragraph}\n\n', "bot_text")
        chat_window.insert(tk.END, f'{second_paragraph}\n\n', "bot_text")
        
        user_input.delete(0, tk.END)  # Clear the input field after sending the message

# Create a GUI window
window = tk.Tk()
window.title("Caldwell Chatbot")

# Set a white and red color scheme
window.configure(bg="white")  # Set the background color to white

# Load images for the user and bot
user_image, bot_image = load_images()

# Customize font styles
user_font = ("Helvetica", 12, "bold")
bot_font = ("Helvetica", 12, "italic")

# Create a text area to display the chat
chat_window = scrolledtext.ScrolledText(window, height=30, width=80, wrap=tk.WORD, bg="white", fg="black", padx=10, pady=10, font=("Helvetica", 12))
chat_window.pack(padx=10, pady=10)

# Tag configurations for styling
chat_window.tag_configure("user_text", foreground="#FF0000", font=user_font)  # Red color for user text
chat_window.tag_configure("bot_text", foreground="#0000FF", font=bot_font)    # Blue color for bot text

# Create an entry box for user input
user_input = tk.Entry(window, width=50, bg="white", fg="black", font=("Helvetica", 14), bd=2)
user_input.pack(pady=10)

# Create a send button with a modern flat style in red color
send_button = tk.Button(window, text="Send", command=send_message, width=12, height=1, font=("Verdana", 12, 'bold'), 
                        bg="#FF0000", fg="white", activebackground="#CC0000", relief="flat", bd=0)
send_button.pack(pady=5)

# Set minimum window size
window.minsize(600, 500)

# Run the GUI loop
window.mainloop()
