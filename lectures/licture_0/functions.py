# ask for user name
name = input("whats your name? ").strip().title()

# printing the hello with name
def hello(name):
    print(f"hello, {name}")

hello(name=name)