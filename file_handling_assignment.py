# Task 1: File Creation
try:
    # Create and open a new file in write mode
    with open('my_file.txt', 'w') as file:
      # Writing lines with a mix of strings and numbers
            file.write("Exploring file operations with Python!\n")
            file.write("The current year is 2024.\n")
            file.write("Here's a statement that includes a number: 87.\n")
except (FileNotFoundError, PermissionError) as error:
        print(f"Error during file creation and writing: {error}")
finally:
        print("File creation and writing complete.")

# Task 2: File Reading and Display
try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("Current File Content:")
            print(content)
except (FileNotFoundError, PermissionError) as error:
        print(f"Error during file reading: {error}")
finally:
        print("File reading complete.")

# Task 3: File Appending
try:
    with open('my_file.txt', 'a') as file:
        file.write("Appending a new line to the file.\n")
        file.write("Here's another line with a different number: 77.\n")
        file.write("This line concludes the new additions.\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred: {e}")
finally:
    print("File appending complete.")

# Reading and Displaying Files (Again)
try:
    with open('my_file.txt', 'r') as file:
        contents = file.read()
        print("Updated file contents:")
        print(contents)
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred: {e}")
finally:
    print("File reading complete.")