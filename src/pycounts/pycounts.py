from collections import Counter
from string import punctuation

def load_text(input_file):
    """load text form a text file and return as a string."""
    with open(input_file, "r") as file:
        text = file.read()
    return text

def clean_text(text):
    """lowercase and remove punctualtion from a string"""
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text

def count_words(input_file):
    """count unique words in a string"""
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)

