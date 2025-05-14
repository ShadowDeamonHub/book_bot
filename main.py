def main():
    from stats import get_book_text, word_count, get_character_count, sorting 
    book_text = get_book_text("/home/patri/Boot_Dev_clourses/book_bot/books/frankenstein.txt")
    num_words = word_count(book_text)
    num_characters =get_character_count(book_text)
    num_characters.sort(reverse=True, key=sorting)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    for i in num_characters:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

main()
