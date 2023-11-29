AIM: Create a text file "MYFILE.TXT" in python and ask the user to write separate 3 lines with three input statements from the user.

def main():
    file_name = "MYFILE.TXT"

    # Ask the user to enter three lines
    lines = []
    for i in range(3):
        line = input(f"Enter line {i + 1}: ")
        lines.append(line)

    # Write the entered lines to the file
    try:
        with open(file_name, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        print(f"Lines have been written to '{file_name}' successfully.")
    except IOError:
        print("Error occurred while writing to the file.")

if __name__ == "__main__":
    main()
