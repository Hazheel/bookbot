def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    # print(file_contents)

    print(f"--- Begin report of {book} ---")

    print(f"{count_words(file_contents)} words found in the document")
    char_count = count_characters(file_contents)
    char_count = dict(sorted(char_count.items(), reverse = True, key=lambda item: item[1]))
    
    for item in char_count:
        if item.isalpha():
            print(f"The '{item}' character was found {char_count[item]} times")


    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered_text = text.lower()
    characters = {}
    for char in lowered_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1   
    return characters

def book_report(text):
    word_count = count_words(text)
    character_count = count_characters(text)

main()
