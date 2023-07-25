import sys

def get_author_info():
    return 'author - Ali'


if __name__  == "__main__":
    while True:
        print("0.exit")
        print("1.info")
        choice = input("Your chose: ")
        if choice == "0":
            sys.exit(0)
        elif choice =="1":
            print(get_author_info())
        else:
            print("Incorrect data")