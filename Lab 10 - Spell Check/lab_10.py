import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def read_in_file(file_name):
    my_file = open(file_name)
    line_list = []
    for line in my_file:
        line = line.strip()
        line_list.append(line)
    my_file.close()
    return line_list

def linear_search(word, dictionary):
    current_position_in_dictionary = 0
    while current_position_in_dictionary < len(dictionary) and dictionary[current_position_in_dictionary] != word:
        current_position_in_dictionary += 1

    return current_position_in_dictionary < len(dictionary)

def binary_search(word, dictionary):
    lower_bound = 0
    upper_bound = len(dictionary) - 1
    found = False

    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2

        if dictionary[middle_pos] < word:
            lower_bound = middle_pos + 1
        elif dictionary[middle_pos] > word:
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
        return True
    else:
        return False

def main():
    dictionary_words = read_in_file("dictionary.txt")
    chapter_lines = read_in_file("AliceInWonderLand200.txt")

    print("----Linear Search")
    for i in range(len(chapter_lines)):
        words = split_line(chapter_lines[i])
        for word in words:
            if not linear_search(word.upper(), dictionary_words):
                print(f'The word \'{word}\' is not in the dictionary')
                print(f'This word is found on line {i + 1}.')

    print("----Binary Search")
    for i in range(len(chapter_lines)):
        words = split_line(chapter_lines[i])
        for word in words:
            if not binary_search(word.upper(), dictionary_words):
                print(f'The word \'{word}\' is not in the dictionary')
                print(f'This word is found on line {i+1}.')

main()


