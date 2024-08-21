


def main():
    x = int(input("whaths x? "))
    if is_even(x):
       print("Evint")
    else:
        print("Odd")


def is_even(num):
    return True if num %2 == 0 else False

main()



