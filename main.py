#python 3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
        elif next in ")]}":
            if not opening_brackets_stack:
                return i+1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i+1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return "Success"

def main():
    input_type = input("Enter F to use test files, or I to input brackets: ")
    if input_type == "F":
        file_number = input("Enter file number: ")
        input_file_name = f"test/{file_number}"
        output_file_name = f"test/{file_number}.a"
    elif input_type == "I":
        text = input("Enter brackets: ")
        mismatch = find_mismatch(text)
        print(mismatch)
        return
    else:
        print("Invalid input type.")
        return
    with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
        text = input_file.read().strip()
        mismatch = find_mismatch(text)
        output_file.write(str(mismatch) + "\n")
        print(mismatch)

if __name__ == "__main__":
    main()