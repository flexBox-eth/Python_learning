# File Read & Write with Error Handling

# Ask the user for a filename
filename = input("Enter the filename to read: ")
output_file = "modified_" + filename

try:
    # Open the file for reading
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (example: uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open(output_file, "w") as file:
        file.write(modified_content)

    print(f"Success! Modified content written to '{output_file}'.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read/write '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
