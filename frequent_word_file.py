from collections import Counter
import string

def most_frequent_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower().translate(str.maketrans("", "", string.punctuation))
            word_counts = Counter(text.split())
            return word_counts.most_common(10)
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

if __name__ == "__main__":
    results = most_frequent_words('sample.txt')
    if results:
        print("The top 10 most frequent words are:")
        for word, count in results:
            print(f"'{word}' with a count of {count}")
    else:
        print("An error occurred while processing the file.")

"""
ALGORITHM:
1. Read the entire file content
2. Convert text to lowercase for case-insensitive counting
3. Remove punctuation using string translation
4. Split text into individual words
5. Use Counter to count word frequencies
6. Return top 10 most common words with their counts

EXAMPLE OUTPUT:
The top 10 most frequent words are:
'the' with a count of 15
'and' with a count of 12
'to' with a count of 10
'of' with a count of 8
'a' with a count of 7
'in' with a count of 6
'that' with a count of 5
'is' with a count of 5
'for' with a count of 4
'with' with a count of 3

Time Complexity: O(n) where n is the number of words
Space Complexity: O(k) where k is the number of unique words
Requires: sample.txt file in the same directory
"""
