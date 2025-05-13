def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents
def word_count(book_text):
    #counts the word in the book
    word_count = book_text.split()
    return len(word_count)
def get_caracter_count(book_text):
    #counts the character in the book
    lowercase_charater = book_text.lower()
    character_count = {}
    for character in lowercase_charater:
        if character in character_count:
            character_count[character] += 1
    else:
        character_count[character] = 1
    return len(character_count)