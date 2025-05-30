from transformers import pipeline

# Load sentiment analysis pipeline with default model (BERT-based)
classifier = pipeline("sentiment-analysis")

# Your input text
text = "I had an amazing day! Everything went better than expected."

# Analyze sentiment
result = classifier(text)

# Show result
print("Text:", text)
print("Sentiment:", result[0]['label'])
print("Confidence Score:", round(result[0]['score'], 3))
