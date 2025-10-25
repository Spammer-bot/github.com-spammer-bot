import os
from datetime import datetime

print("Encrypted Diary")

File_name = "diary.txt"
key = 5

# VIBHOR = ANGMTW

while True:
    print("\n Encrypted Diary")
    print("1. Write Entry")
    print("2. Read Entry")
    print("3. Search Entry")
    print("4. Back Diary")

    choice = input("Choose an option from 1-4: ")

    if choice == "1":
        entry = input("Enter the content you want to write in the diary: \n")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text = f"[{timestamp}] {entry}\n"

        encrypted = ""
        for c in text:
            encrypted += chr(ord(c) + key)

        with open(File_name, "a") as f:
            f.write(encrypted)
        print("Entry saved successfully!")

    if choice == "2":
        if not os.path.exists(File_name):
            print("No entry found")
        else:
            with open(File_name, "r") as f:
                for line in f:
                    decrypted = ""
                    for c in line:
                        decrypted += chr(ord(c) - key)
                    print(decrypted, end="")

    if choice == "3":
        if not os.path.exists(File_name):
            print("No Entry Found!")
        else:
            keyword = input("Enter one word from the diary entry you want to search = ").lower()
            found = False
            with open (File_name, "r") as f:
                for line in f:
                    decrypted = ""
                    for c in line:
                        decrypted += chr(ord(c) - key)
                    if keyword in decrypted.lower():
                        print(decrypted,end="")
                        found = True
            if not found:
                print("No Entry Found!")

    if choice == "4":
        print("Exiting diary! See you around")
        break