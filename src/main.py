from src import create_app
import nltk

try:
    import spacy
    SPACY_AVAILABLE = True
except ImportError:
    SPACY_AVAILABLE = False
    print("Warning: spaCy not installed. Install with: pip install spacy")


def initialize_nlp():
    """Initialize NLP libraries."""
    try:
        nltk.download('punkt', quiet=True)
        if SPACY_AVAILABLE:
            # Note: spacy model needs to be installed: python -m spacy download en_core_web_sm
            try:
                nlp = spacy.load("en_core_web_sm")
                return nlp
            except OSError:
                print("Warning: spaCy model 'en_core_web_sm' not found. Install with: python -m spacy download en_core_web_sm")
                return None
        return None
    except Exception as e:
        print(f"Warning: Error initializing NLP: {e}")
        return None


def process_input(text):
    """Process text input using NLP tools."""
    # Initialize NLP
    nlp = initialize_nlp()
    
    # Basic NLP processing
    try:
        tokens = nltk.word_tokenize(text)
    except LookupError:
        # If punkt tokenizer not downloaded, use simple split
        tokens = text.split()
    
    entities = []
    
    if nlp:
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return f"Received {text}. Tokens: {len(tokens)}, Entities: {entities}"


# Create the Flask application
app = create_app('development')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)