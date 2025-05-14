def main():
    from stats import get_book_text, word_count, get_character_count, dict_sorted
    book_text = get_book_text("/home/patri/Boot_Dev_clourses/book_bot/books/frankenstein.txt")
    num_words = word_count(book_text)
    num_characters = dict_sorted(sorted_character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found a books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"{num_words} words found in the document")
    print("----------- Character Count -----------")
    print(num_charaters)




main()
