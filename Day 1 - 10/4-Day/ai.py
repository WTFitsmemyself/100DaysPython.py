# Install dependencies first:
# pip install transformers torch

from transformers import pipeline

# Load a pre-trained sentiment analysis model
classifier = pipeline("sentiment-analysis")

# Example text
text = "my friend is hinata, I think she is not cute"

# Run the classifier
result = classifier(text)

print(result)
