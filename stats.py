def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents
def word_count(book_text):
    #counts the word in the book
    word_count = book_text.split()
    return len(word_count)