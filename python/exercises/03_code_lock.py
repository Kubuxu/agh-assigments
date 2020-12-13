import os

filepath = "code.txt"
if not os.path.exists(filepath):
    print("Enter new code:")
    code = input()
    with open(filepath, "w") as f:
        f.write(code)

else:
    with open(filepath, "r") as f:
        code = f.read()

    print("Enter Code:")
    entry = input()
    if entry == code:
        print("You are in!")
    else:
        print("Bad code.")


