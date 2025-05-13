def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents
def word_count(book_text):
    #counts the word in the book
    word_count = book_text.split()
    return len(word_count)
def main():

    book_text = get_book_text("/home/patri/Boot_Dev_clourses/book_bot/books/frankenstein.txt")
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")



main()
