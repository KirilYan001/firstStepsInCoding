book_name = input()
counter = 0
Flag = False

current_book = input()
while current_book != 'No More Books':

    if book_name == current_book:
        Flag = True
        break

    counter += 1
    current_book = input()

if current_book == 'No More Books':
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
elif Flag:
    print(f"You checked {counter} books and found it.")

