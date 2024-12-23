"""
Count Word Frequency
Define a function to count the frequency of words in a given list of words.

Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 

Output: {'apple': 3, 'orange': 2, 'banana': 1}
"""

def count_word_frequency(words):
    word_frequency = dict()
    for word in words:
        word_frequency.setdefault(word, 0)
        word_frequency[word] += 1
    return word_frequency

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words)) # {'apple': 3, 'orange': 2, 'banana': 1}

"""
Time complexity:
The time complexity of this exercise is O(n), where n is the number of words in the input list. The loop iterates through each
word in the list once, and the dictionary operations (setdefault and update) take constant time, O(1), on average.

Space complexity:
The space complexity of this exercise is also O(n), where n is the number of unique words in the input list. In the worst 
case, all words are unique, and the word_count dictionary will have n entries.
"""