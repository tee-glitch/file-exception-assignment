# main.py
try:
    # Ask user for filename
    filename = input("Enter the filename to read: ")

    # Open the file for reading
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (example: make it uppercase)
    modified_content = content.upper()

    # Write to a new file
    with open("output.txt", "w") as new_file:
        new_file.write(modified_content)

    print("✅ File has been read and modified successfully. Check 'output.txt'.")

except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
