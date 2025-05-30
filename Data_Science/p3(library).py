import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple is looking to buy a startup in the UK for $1 billion."

# Process the text
doc = nlp(text)

# Print named entities
print("Named Entities:")
for ent in doc.ents:
    print(ent.text, "-", ent.label_)
