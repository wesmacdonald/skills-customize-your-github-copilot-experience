# Starter code for Python Text Processing assignment

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def count_lines(text):
    return len(text.splitlines())

def count_words(text):
    return len(text.split())

def replace_word(text, search, replacement):
    return text.replace(search, replacement)

if __name__ == "__main__":
    filename = input("Enter filename: ")
    text = read_file(filename)
    print("\nFile contents:\n", text)
    print("\nTotal lines:", count_lines(text))
    print("Total words:", count_words(text))
    search = input("Enter word to search: ")
    replacement = input("Enter replacement word: ")
    modified = replace_word(text, search, replacement)
    print("\nModified text:\n", modified)
