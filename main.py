from stats import word_count
from stats import get_book_text
from stats import char_stats
from stats import sorted_stats

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
word_count()
print("--------- Character Count -------")
stat_dict = char_stats()
entries = sorted_stats(stat_dict)
for item in entries:
    print(f"{item['char']}: {item['count']}")
print("============= END ===============")