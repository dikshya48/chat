import google.generativeai as ai
import panel as pn

# Configure the API key
API_KEY = 'AIzaSyCry02qgple8zxa86lbRglzYo6rQcmox_I'  # Your API key here
ai.configure(api_key=API_KEY)

# Create a model instance for text generation
model = ai.GenerativeModel("gemini-pro")  # Correctly instantiate the GenerativeModel
chat = model.start_chat()  # Now you can start the chat

# Create a function to handle the conversation
def send_message(event=None):
    message = user_input.value  # Get user input
    if message.lower() == 'bye':
        conversation.value += f"\nYou: {message}\nBot: Goodbye!\n"
        return
    
    # Get response from the chat model
    response = chat.send_message(message)
    
    # Format the response text to remove unwanted characters and replace new lines
    response_text = response.text.replace('*', '').replace(';', '').replace('\n', ' ')
    response_text = ' '.join(response_text.split())  # Normalize spaces
    
    # Split the response into sentences
    sentences = response_text.split('. ')  # Split the text by sentences (after each period)
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
    
    # Update the conversation panel with both paragraphs
    conversation.value += f"\nYou: {message}\nBot:\n{first_paragraph}\n\n{second_paragraph}\n"
    
    user_input.value = ''  # Clear the input field after sending the message

# Create Panel widgets
conversation = pn.widgets.TextAreaInput(value='', placeholder='Conversation will appear here...', height=300, width=600, disabled=True)
user_input = pn.widgets.TextInput(placeholder='Enter your message here...', width=400)
send_button = pn.widgets.Button(name='Send', button_type='primary')

# Bind the send_button to the send_message function
send_button.on_click(send_message)

# Layout the widgets
layout = pn.Column(
    conversation,
    pn.Row(user_input, send_button),
)

# Serve the layout using Panel
layout.servable()

# To run the Panel app, execute: `panel serve your_script_name.py` in the terminal
