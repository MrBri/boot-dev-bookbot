def char_counts(string):
    chars = {}
    lowered = string.lower()
    words = lowered.split()
    for word in words:
        for c in word:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    print(chars)
    return chars

def count_words(string):
    words = string.split();
    return len(words)

def sorted_output(dict):
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    for item in sorted_dict:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times\n")
    print(sorted_dict)


with open('books/frankenstein.txt', 'r') as f:
    file_contents = f.read()
    words = count_words(file_contents)
    print(words)
    chars = char_counts(file_contents)
    sorted_output(chars)
