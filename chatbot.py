import streamlit as st

# Set streamlit page configuration
st.set_page_config(page_title="Rimsha Chatbot")
st.title("CHATBOT WITH Rule-Based")

# Define a dictionary of predefined user queries and their corresponding responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a chatbot, but I'm here to help. What can I do for you?",
    "goodbye": "Goodbye! Have a great day!",
    "help": "Sure, I can help with various tasks. Just ask me anything!",
    "what's your name": "I'm a chatbot, so I don't have a name, but you can call me ChatGPT.",
    "who created you": "I was created by Rimsha.",
    "who is rimsha": "Rimsha is an AI chatbot developer.",
    "what does rimsha do": "Rimsha specializes in developing chatbots and AI-powered applications.",
    "can you tell me more about rimsha work": "Rimsha has experience in natural language processing (NLP), machine learning, and building conversational AI systems.",
    "how can i contact rimsha": "You can reach out to Rimsha via email at rimsha9905@GMAIL.com.",
}

user_input = st.text_input("You:")

# Function to get the chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm not sure how to respond to that. Please ask another question."
    return chatbot_response()


if st.button("Submit"):
    # Get the chatbot's response
    response = chatbot_response(user_input)
    st.text("Chatbot: " + response)


