def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents
def word_count(words):
    #counts the word in the book
    word_count = words.split()
    return len(word_count)
def get_character_count(characters):
    #counts the character in the book
    lowercase_charater = characters.lower()
    character_count = {}
    for character in lowercase_charater:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    char_list = []
    for char, num in character_count.items():
        char_list.append({"char": char, "num": num})
    return char_list




#def sorting(character_count):
 #   return character_count[???]