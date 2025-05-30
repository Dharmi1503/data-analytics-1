import stanza
stanza.download('en')
import stanza

# Load the English NLP pipeline
nlp = stanza.Pipeline('en')

# Process a text
doc = nlp("Google was founded in 1998 by Larry Page and Sergey Brin in California.")

# Named Entity Recognition (NER)
print("Named Entities:")
for ent in doc.ents:
    print(ent.text, "-", ent.type)

# POS Tagging
print("\nPart-of-Speech Tags:")
for sentence in doc.sentences:
    for word in sentence.words:
        print(f"{word.text} - {word.pos}")



