import re

def build_language_model():
    """Build a model containing language-specific common words."""
    return {
        "English": {"the", "and", "of", "to", "in", "is", "it", "that", "he", "was", "for", "on", "with", "as", "his", "by", "at", "from"},
        "French": {"le", "et", "la", "a", "de", "en", "est", "un", "pour", "que", "il", "les", "des", "dans", "du", "sur", "au", "par"},
        "German": {"und", "die", "der", "in", "zu", "das", "ist", "auf", "fur", "mit", "den", "von", "nicht", "sie", "es", "ein", "ich", "du"},
        "Spanish": {"el", "de", "la", "y", "en", "que", "es", "un", "por", "los", "del", "con", "para", "una", "como", "las", "al", "se"}
    }

def normalize_text(text):
    """Normalize text by removing non-ASCII characters and converting to lowercase."""
    # Replace non-ASCII characters with a blank space
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return text.lower()

def detect_language(text, model):
    """Detect the language of the input text based on common words."""
    # Normalize the text
    words = set(normalize_text(text).split())
    
    # Calculate the intersection with each language's common words
    scores = {language: len(words & common_words) for language, common_words in model.items()}
    
    # Return the language with the highest score
    return max(scores, key=scores.get)

def main():
    # Build the language model
    model = build_language_model()

    # Read the input text (supports multiple lines)
    text = ""
    while True:
        try:
            line = input().strip()
            if line == "":
                break
            text += " " + line
        except EOFError:
            break

    # Detect the language
    language = detect_language(text, model)
    
    # Output the result
    print(language)

if __name__ == "__main__":
    main()
