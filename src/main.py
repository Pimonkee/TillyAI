import os
import sys
from flask import Flask, request, jsonify
import pymongo
import redis
import nltk
import spacy

# Initialize Flask app
app = Flask(__name__)

# Initialize MongoDB client
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["tilly_db"]

# Initialize Redis client
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Initialize NLP tools
nltk.download('punkt')
spacy_model = spacy.load("en_core_web_sm")

# Example route for testing
@app.route('/tilly', methods=['POST'])
def tilly_response():
    user_input = request.json.get("text")
    response = process_input(user_input)
    return jsonify({"response": response})

def process_input(text):
    # Example NLP processing
    tokens = nltk.word_tokenize(text)
    doc = spacy_model(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Example MongoDB interaction
    db.responses.insert_one({"input": text, "tokens": tokens, "entities": entities})

    # Example Redis interaction
    redis_client.set('last_input', text)

    # Example response generation (this should be much more complex in a real implementation)
    return f"Received {text}. Extracted entities: {entities}"

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)