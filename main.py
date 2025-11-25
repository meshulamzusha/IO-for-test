import sys

import loader
import processor


def print_menu() -> None:
    print(
        "1. Load file and display how many lines are loaded."
        "2. Show the number of lines in file."
        "3. Show the number of words in file."
        "4. Show the number of vowels in file."
        "5. Print lines whose length is greater than given parameter."
        "6. search a word in a file"
        "7. Exit"
    )


def handle_user_choice() -> None:
        choice = input("Choose: ")
        path = input("Enter the path to file: ")

        match choice:
            case "1":
                num_of_lines = len(loader.load_lines(path))
                print(f'num lines: {num_of_lines}')
            case "2":
                print(f'num lines: {loader.count_lines(path)}')
            case "3":
                sum_words = 0
                for line in loader.load_lines(path):
                    sum_words += processor.count_words(line)
                print(f'num of words in file: {sum_words}')
            case "4":
                sum_vowels = 0
                for line in loader.load_lines(path):
                    sum_vowels += processor.count_vowels(line)
                print(f'sum of vowels in file: {sum_vowels}')
            case "5":
                min_length = input("Enter the minimum line length: ")
                print(loader.load_long_lines(path, min_length))
            case "6":
                is_in = False
                keyword = input("Enter a keyword to search: ")
                for line in loader.load_lines(path):
                    if processor.has_keyword(line, keyword):
                        is_in = True
                print(is_in)
            case "7":
                sys.exit()


