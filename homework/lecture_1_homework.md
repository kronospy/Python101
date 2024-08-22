In `deep.py`, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs `42` or (case-insensitively) `forty-two` or `forty two`. Otherwise output `No`.

## Before You Begin
Log into cs50.dev, click on your terminal window, and execute cd by itself. You should find that your terminal window’s prompt resembles the below:
```bash
/workspaces/Python101 (your-repo-name) $
```
Next execute
```bash
mkdir deep
```
to make a folder called deep in your codespace.

Then execute
```bash
cd deep
```
to change directories into that folder. You should now see your terminal prompt as `deep/ $` You can now execute

```bash
code deep.py
```
to make a file called `deep.py` where you’ll write your program.

## How to Test
Here’s how to test your code manually:

- Run your program with `python deep.py`. Type `42` and press `Enter`. Your program should output:
```
Yes
``` 
- Run your program with `python deep.py`. Type `Forty Two` and press `Enter`. Your program should output:
```
Yes
```
- Run your program with `python deep.py`. Type `forty-two` and press `Enter`. Your program should output
```
Yes
```
- Run your program with `python deep.py`. Type `50` and press `Enter`. Your program should output
```
No
```
Be sure to vary the casing of your input and “accidentally” add spaces on either side of your input before pressing enter. Your program should behave as expected, case- and space-insensitively.


