# Import necessary libraries
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK data files (needed for tokenization and stopwords)
nltk.download('punkt')
nltk.download('stopwords')

# Define a dictionary of predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I assist you?"],
    "how are you": ["I'm just a bot, but I'm doing great! How about you?"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "help": ["Sure, I am here to help! Ask me anything."],
    "default": ["I'm sorry, I don't understand that."]
}

# Function to preprocess user input
def preprocess_input(user_input):
    """
    This function tokenizes the input, converts it to lowercase,
    and removes common stopwords like 'the', 'is', etc.
    """
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(user_input.lower())  # Tokenize and convert to lowercase
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

# Function to generate chatbot responses
def chatbot_response(user_input):
    """
    This function generates a response based on user input.
    It checks for matching keywords in the input and returns a response.
    """
    tokens = preprocess_input(user_input)
    for token in tokens:  # Check each token in the input
        if token in responses:  # If token matches a key in responses
            return random.choice(responses[token])  # Return a random response from the list
    return random.choice(responses["default"])  # Default response if no match is found

# Main function to interact with the chatbot
def main():
    print("Chatbot: Hello! Type 'bye' to exit.")  # Initial greeting from the bot
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if user wants to exit
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye!")  # Exit message
            break
        
        # Generate and print bot response
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot program
if __name__ == "__main__":
    main()