## **Prompt:**

**Create a Simple Chatbot**

**Task:**

Write a Python program that simulates a basic chatbot. The chatbot should be able to:

1. **Greet the user:** Respond with a greeting (e.g., "Hello there!") if the user enters a greeting (e.g., "hi", "hello").
2. **Respond to specific questions:** Provide predefined responses to certain questions (e.g., "How are you?").
3. **Handle unknown inputs:** If the chatbot doesn't understand the user's input, it should respond with a generic message (e.g., "I'm not sure how to respond to that.").
4. **End the conversation:** The chatbot should terminate the conversation when the user enters a farewell message (e.g., "goodbye").

**Requirements:**

* Use lists to store greeting and farewell phrases.
* Use dictionaries to store predefined responses to specific questions.
* Define a function to handle the chatbot's responses.
* Use a `while` loop to continuously prompt the user for input until the conversation ends.

**Example Usage:**

```
Enter your message: hi
Hello there!
Enter your message: how are you
I'm doing well, thanks for asking!
Enter your message: goodbye
Goodbye!
```

**Explanation:**

The provided code demonstrates how to create a simple chatbot using Python. It defines a function `create_chatbot_response` that takes the user's input as a parameter and returns an appropriate response. The function uses lists and dictionaries to store greeting, farewell, and response phrases. It checks if the user's input matches any of these phrases and returns the corresponding response. If the input is not recognized, it returns a generic response.

The `while` loop continuously prompts the user for input until a farewell message is entered. The chatbot's response is then printed to the console.
