def main(file_path, file):
    with open(file_path) as f:

        file_contents = f.read()
        word_count = get_word_count(file_contents)
        letter_count = get_letter_count(file_contents)
        print_report(word_count, letter_count, file_path)

def get_word_count(book_text):
    return len(book_text.split())

def get_letter_count(book_text):
    word_array = book_text.split()
    letters = {}

    # loop over each word in the array
    for word in word_array:

        # loop over each letter in the word
        for w in word:
            if w.isalpha():
                lowercase_letter = w.lower()
                if lowercase_letter in letters:
                    letters[lowercase_letter] += 1
                else:
                    letters[lowercase_letter] = 1

    return letters

def sort_key(dict):
    return dict["count"]

def sort_letter_counts(letter_counts):
    converted_counts = []

    for l, value in letter_counts.items():
        converted_counts.append({"name": l, "count": value})

    converted_counts.sort(reverse=True, key=sort_key)
    return converted_counts

def print_report(word_count, letter_count, file):
    sorted_counts = sort_letter_counts(letter_count)
    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words found in the document")
    print("")
    for s in sorted_counts:
        print(f"The {s['name']} was found {s['count']} times")
    print("--- End report ---")

main("books/frankenstein.txt", "frankenstein")