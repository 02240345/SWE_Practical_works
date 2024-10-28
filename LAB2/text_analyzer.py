def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
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
analyze_text('sample.txt')





# Exercises

# 1.Counting the number of unique words in the text.

def count_unique_words(content):
    unique_words = set(content)
    return len(unique_words)

# Test the function
num_unique_words = count_unique_words(content)
print(f"Number of unique words: {num_unique_words}")



# 2.Finding the longest word in the text.

def find_longest_word(content):
    words = content.split()
    longest_word = max(words, key=len)
    return longest_word

# Test the function
longest_word = find_longest_word(content)
print(f"Longest word: '{longest_word}'")




# 3.Counting the occurrences of a specific word (case-insensitive).

def count_word_occurrences(content, target_word):
    words = content.lower().split()
    target_word = target_word.lower()
    return words.count(target_word)

# Test the function
target_word = "python"  
occurrences = count_word_occurrences(content, target_word)
print(f"Occurrences of '{target_word}': {occurrences}")




# 4.Calculating the percentage of words that are longer than the average word length.

def percentage_longer_than_average(content):
    words = content.split()
    average_length = sum(len(word) for word in words) / len(words)
    longer_than_avg_count = sum(1 for word in words if len(word) > average_length)
    percentage = (longer_than_avg_count / len(words)) * 100
    return percentage

# Test the function
percentage_longer = percentage_longer_than_average(content)
print(f"Percentage of words longer than average: {percentage_longer:.2f}%")


