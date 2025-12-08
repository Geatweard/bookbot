#Takes file path of book.txt and returns book as string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

#prints word count of book
def word_count():
    frank_path = "./books/frankenstein.txt"
    frankenstein = get_book_text("./books/frankenstein.txt")
    word_count = len(frankenstein.split())
    print(f"Found {word_count} total words")

def char_stats():
    frankenstein = get_book_text("./books/frankenstein.txt")
    stat_dict = {}
    for char in frankenstein:
        char_lower = char.lower()
        if char_lower in stat_dict:
            stat_dict[char_lower] += 1
        else:
            stat_dict[char_lower] = 1
    return stat_dict

def sorted_stats(stat_dict):
    
        


