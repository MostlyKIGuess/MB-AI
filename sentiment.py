from fuzzywuzzy import fuzz

APPRECIATION_PHRASES = ["thanks", "thank you", "great", "good job", "well done", "appreciate it", "good"]
DISCOURAGEMENT_PHRASES = ["not helpful", "bad", "poor", "wrong", "incorrect", "disappointed"]

APPRECIATION_RESPONSE = "You're welcome! I'm glad I could help. If you have more questions, feel free to ask."
DISCOURAGEMENT_RESPONSE = "I'm sorry to hear that you are not satisfied with my response. Could you please provide more details or ask another question so I can assist you better?"

GREETINGS = ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"]

def detect_sentiment(message):
    """Detect sentiment in user message."""
    for phrase in APPRECIATION_PHRASES:
        if fuzz.ratio(message.lower(), phrase.lower()) > 90:
            return 'appreciation'
    for phrase in DISCOURAGEMENT_PHRASES:
        if fuzz.ratio(message.lower(), phrase.lower()) > 90:
            return 'discouragement'
    return None

def is_greeting(user_input):
    """Check if the input is a greeting."""
    user_input = user_input.strip().lower()
    for greeting in GREETINGS:
        if fuzz.ratio(user_input, greeting) > 90:
            return True
    return False

def get_response_for_sentiment(sentiment):
    """Get appropriate response based on sentiment."""
    if sentiment == 'appreciation':
        return APPRECIATION_RESPONSE
    elif sentiment == 'discouragement':
        return DISCOURAGEMENT_RESPONSE
    return None
