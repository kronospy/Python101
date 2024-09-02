## Prompt:

**Create a Python function that counts the occurrences of each word in a given text.**

### Explanation:

**Task:**
* **Input:** A text string.
* **Output:** A dictionary where keys are words from the text and values are their corresponding frequencies.

**Steps:**
1. **Initialize a dictionary:** Create an empty dictionary to store word counts.
2. **Split the text:** Break down the text into individual words using the `split()` method.
3. **Iterate through words:** For each word in the list of words:
   * **Check if the word exists:** If the word is already in the dictionary:
     * **Increment the count:** Increase the corresponding value (count) by 1.
   * **Add the word:** If the word is not in the dictionary:
     * **Set the count:** Add the word as a key and set its value to 1.
4. **Return the dictionary:** After processing all words, return the dictionary containing word frequencies.

**Example Usage:**
```python
text = "This is a sample text. This text has some repeated words."
word_count = count_words(text)
print(word_count)
```

This code will output a dictionary like:
```python
{'This': 2, 'is': 2, 'a': 1, 'sample': 1, 'text': 2, 'has': 1, 'some': 1, 'repeated': 1, 'words': 1}
```
