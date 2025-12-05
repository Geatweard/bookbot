#Takes file path of book.txt and returns book as string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

#prints book text
def main():
    frankenstein = get_book_text("./books/frankenstein.txt")
    word_count = len(frankenstein.split())
    print(f"Found {word_count} total words")
    
    ###print(frankenstein)

main()
