def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    #print(f"{num_words} words found in the document")
    #print(f"The occurrance of letters in the text is as follows: {num_letters}")
    #print(num_letters)
    list_of_dicts = dict_to_list(num_letters)
    print_report(list_of_dicts,book_path,text)
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_letters(text):
    letter_dict = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
           letter_dict[char] += 1
    
    return letter_dict

def sort_on(dict):
    return dict["num"]

def dict_to_list(dict):
    dict_list = []
    for char in dict:
        dict_list.append({"char": char, "num": dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def print_report(list, path_to_book,text):
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{get_num_words(text)} words found in the document")
    print(" ")
    for item in list:
        if item["char"].isalpha():
            print(f"The '{item["char"]}' character was found {item["num"]} times")
    print ("--- End report ---")

main()