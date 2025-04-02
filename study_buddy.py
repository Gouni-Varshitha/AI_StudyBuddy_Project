# Step 1: Define the dataset
study_topics = {
    "binary trees": "Binary trees are hierarchical data structures used for searching and sorting.",
    "machine learning": "Machine Learning enables systems to learn from data without explicit programming.",
    "sorting algorithms": "Sorting algorithms, like Bubble Sort or Merge Sort, arrange data in a particular order.",
    "artificial intelligence": "AI is the simulation of human intelligence in machines designed to think and learn."
}
import nltk

nltk.download('punkt')  # Download the Punkt tokenizer
nltk.download('stopwords')
nltk.download('punkt_tab') # Download the stopwords resource

# Step 2: Add the preprocessing function
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_input(user_input):
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(user_input.lower())
    return [word for word in tokens if word not in stop_words]

# Step 3: Add the response function
def get_response(query):
    query_words = preprocess_input(query)
    for topic, explanation in study_topics.items():
        if any(word in topic for word in query_words):
            return f"Topic: {topic}\nExplanation: {explanation}"
    return "Sorry, I couldn't find information on that topic."

# Step 4: Add the test code (for now)
user_question = input("Enter your study question: ")
print(get_response(user_question))