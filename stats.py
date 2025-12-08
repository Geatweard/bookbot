#Takes file path of book.txt and returns book as string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

#prints word count of book
def word_count(path):
    book_text = get_book_text(path)
    word_count = len(book_text.split())
    print(f"Found {word_count} total words")

def char_stats(path):
    book_text = get_book_text(path)
    stat_dict = {}
    for char in book_text:
        char_lower = char.lower()
        if char_lower in stat_dict:
            stat_dict[char_lower] += 1
        else:
            stat_dict[char_lower] = 1
    return stat_dict

#Return a sorted list of dicts from `stat_dict`.
    #- If `alpha_only` is True, exclude keys where `key.isalpha()` is False.
    #- Returned list items are `{'char': key, 'count': value}` sorted by
    #  count descending then key ascending.
def sorted_stats(stat_dict):
    items = ((k, v) for k, v in stat_dict.items() if k.isalpha())
    entries = [{'char': k, 'count': v} for k, v in items]
    entries.sort(key=lambda d: (-d['count'], d['char']))
    return entries




