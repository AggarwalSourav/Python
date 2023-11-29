AIM: write a program that inputs a text file, The program should print all of the unique words in the file in alphabetical order.

def extract_unique_words(file_name):
    unique_words = set()

    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Split the line into words
                words = line.split()

                # Remove punctuation and convert words to lowercase
                words = [word.strip('.,!?()[]{}\'"') for word in words]
                words = [word.lower() for word in words]

                # Add unique words to the set
                unique_words.update(words)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []

    return sorted(unique_words)

def main():
    file_name = input("Enter the file name: ")
    unique_words = extract_unique_words(file_name)

    if unique_words:
        print("Unique words in alphabetical order:")
        for word in unique_words:
            print(word)

if __name__ == "__main__":
    main()
