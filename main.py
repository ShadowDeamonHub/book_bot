def main():
    from stats import get_book_text, word_count, get_character_count

    book_text = get_book_text("/home/patri/Boot_Dev_clourses/book_bot/books/frankenstein.txt")
    num_words = word_count(book_text)
    num_characters = get_character_count(book_text)
    print(f"{num_words} words found in the document")
    print(num_characters)



main()
