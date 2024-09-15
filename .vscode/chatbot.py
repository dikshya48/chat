import panel as pn
import requests

# Enable Panel extension
pn.extension()

# API Key and Custom Search Engine ID
API_KEY = 'AIzaSyDkug-jwkUm0SThkMTxasgD7H7ItNjj20Y'
CSE_ID = '7154c5ffd1a6f4f67'

# Function to perform Google Custom Search
def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CSE_ID}&q={query}"  # Use query instead of contents
    response = requests.get(url)
    results = response.json()
    items = results.get("items", [])
    
    # Return a list of snippets (up to 3)
    return [item['snippet'] for item in items[:1]]

# Callback function for the chat interface
def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    if contents == 'exit':
        instance.send('Goodbye!')
        instance.close()
    elif contents.lower() == "":
        return f""
    else:
        search_results = google_search(contents)
        if search_results:
            return '\n\n'.join(search_results)
        return "I couldn't find any results for your query."

# Create the Chat Interface and serve it
chat = pn.chat.ChatInterface(callback=callback)
chat.servable()

# Serve the chat interface on a higher port (e.g., 8080)
pn.serve(chat, port=8080, websocket_origin=['*'])
