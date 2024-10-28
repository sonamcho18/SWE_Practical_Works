def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('resources.txt')
print(content[:100])  # Print the first 100 characters

def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")

from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

# Run the analysis
analyze_text('resources.txt')

# Exercise 1
def count_unique_words(text):
    # Remove punctuation and convert to lowercase
    words = text.lower().split()
    words = [word.strip('.,!?;()[]') for word in words]
    
    # Use a set to store unique words
    unique_words = set(words)
    
    return len(unique_words)

# Example text
text = read_file('resources.txt')

# Count the number of unique words
unique_word_count = count_unique_words(text)
print("Number of unique words:", unique_word_count)

# Exercise 2
def count_unique_words(text):
    # Remove punctuation and convert to lowercase
    words = text.lower().split()
    words = [word.strip('.,!?;()[]') for word in words]
    
    # Use a set to store unique words
    unique_words = set(words)
    
    return len(unique_words)

def find_longest_word(text):
    # Remove punctuation and convert to lowercase
    words = text.lower().split()
    words = [word.strip('.,!?;()[]') for word in words]
    
    # Find the longest word
    longest_word = max(words, key=len)
    
    return longest_word

# Example text
text = read_file ('resources.txt')

# Count the number of unique words
unique_word_count = count_unique_words(text)
print("Number of unique words:", unique_word_count)

# Find the longest word
longest_word = find_longest_word(text)
print("Longest word:", longest_word)

# Exercise 3
def count_unique_words(text):
    # Remove punctuation and convert to lowercase
    words = text.lower().split()
    words = [word.strip('.,!?;()[]') for word in words]
    
    # Use a set to store unique words
    unique_words = set(words)
    
    return len(unique_words)

def find_longest_word(text):
    # Remove punctuation and convert to lowercase
    words = text.lower().split()
    
    # Find the longest word
    longest_word = max(words, key=len)
    
    return longest_word

def count_word_occurrences(text, target_word):
    # Remove punctuation and convert to lowercase
    words = text.lower().split()
    words = [word.strip('.,!?;()[]') for word in words]
    
    # Convert target word to lowercase
    target_word = target_word.lower()
    
    # Count occurrences of the target word
    occurrences = words.count(target_word)
    
    return occurrences

# Example text
text = read_file('resources.txt')
target_word = "quick"

# Count the number of unique words
unique_word_count = count_unique_words(text)
print("Number of unique words:", unique_word_count)

# Find the longest word
longest_word = find_longest_word(text)
print("Longest word:", longest_word)

# Count occurrences of the target word
word_occurrences = count_word_occurrences(text, target_word)
print(f"Occurrences of the word '{target_word}':", word_occurrences)

# Excerise 4
def percentage_long_words(content):
    words = content.split()
    avg_length = average_word_length(content)
    long_words = [word for word in words if len(word) > avg_length]
    return (len(long_words) / len(words)) * 100
print("percentages:", percentage_long_words(content))
