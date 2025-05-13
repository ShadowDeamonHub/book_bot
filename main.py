def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents
def main():

    book_text = get_book_text("/home/patri/Boot_Dev_clourses/book_bot/books/frankenstein.txt")
    print(book_text)



main()
