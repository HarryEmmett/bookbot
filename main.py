def main(file_path, file):
    with open(file_path) as f:

        file_contents = f.read()
        word_count = get_word_count(file_contents)
        print(f"The file {file} has {word_count} words")

def get_word_count(book_text):
    return len(book_text.split())

main("books/frankenstein.txt", "frankenstein")