def main():
    book_path = "books/frankenstein.txt"
    print(f"---- Begin report of {book_path} ----\n")
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    print(f"The total word count is {word_count} words.\n")
    tally = tally_letter_usage(book_text)
    print_tally(tally)
    print("---- End Report ----")

def count_words(string):
    words = string.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def tally_letter_usage(string):
    char_tally = {}
    for char in string:
        current_char = char.lower()
        ascii_value = ord(current_char)
        if ascii_value >= 97 and ascii_value <= 122:
            if current_char in char_tally:
                char_tally[current_char] += 1
            else:
                char_tally[current_char] = 1
    return char_tally

def print_tally(tally):
    sort_list = []
    for letter in tally:
        sort_list.append({'letter':letter, 'num': tally[letter]})
    sort_list.sort(reverse=True, key=sort_on)
    for item in sort_list:
        print(f"The '{item['letter']}' character was found {item['num']} times")

def sort_on(dict):
    return dict["num"]

main()