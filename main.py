import sys
from stats import word_count
from stats import get_book_text
from stats import char_stats
from stats import sorted_stats

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
word_count(book_path)
print("--------- Character Count -------")
stat_dict = char_stats(book_path)
entries = sorted_stats(stat_dict)
for item in entries:
    print(f"{item['char']}: {item['count']}")
print("============= END ===============")