def main():
    from stats import get_book_text, word_count, get_character_count, dict_sorted
    book_text = get_book_text("/home/patri/Boot_Dev_clourses/book_bot/books/frankenstein.txt")
    num_words = word_count(book_text)
    num_characters =get_character_count(book_text)
    character_ordered = dict_sorted(num_characters)
    ussorted_character_count = list(character_ordered)
    character_sorted = ussorted_character_count.sort(reverse= True, key = dict_sorted)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found a books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"{num_words} words found in the document")
    print("----------- Character Count -----------")
    print(character_sorted)


main()
