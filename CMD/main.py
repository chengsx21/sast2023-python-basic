import argparse
import json
import os
import pyperclip
import random
import sys

def parser_data():
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", type=str, help="Game File", required=True)
    parser.add_argument("-r", "--random", type=str, help="Article Index", required=True)
    args = parser.parse_args()
    return args

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        for item in data:
            if item["language"] == "en":
                en_articles = item["articles"]
            if item["language"] == "zh":
                zh_articles = item["articles"]
    return en_articles, zh_articles

def read_random_article():
    if random.randint(0, 1) == 1:
        return random.choice(en_articles)
    else:
        return random.choice(zh_articles)

def read_specific_article(lang, index):
    if lang == "en":
        return en_articles[index - 1]
    else:
        return zh_articles[index - 1]

def get_inputs(hints):
    keys = []
    for i, hint in enumerate(hints):
        color_print(f"Word {i + 1}", "\033[43m")
        color_print(f"Hint. {hint}:", "\033[33m")
        keys.append(input())
        clear_error()
    return keys

def replace(article, keys):
    for i, key in enumerate(keys):
        article = article.replace(f"{{{{{i+1}}}}}", key)
    return article

def clear_error():
    print("\033[F\033[J", end="")
    print("\033[F\033[J", end="")
    print("\033[F\033[J", end="")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def reset_screen():
    print("\033[0m")

def color_print(text, color_code):
    print(f"{color_code}{text}\033[0m")

if __name__ == "__main__":
    try:
        clear_screen()
        args = parser_data()
        en_articles, zh_articles = read_file(args.file)
        if args.random == "random":
            article = read_random_article()
        elif args.random == "specific":
            color_print("Please choose your language.\n", "\033[43m")
            while True:
                color_print("Enter 'en' for English, 'zh' for Chinese.", "\033[33m")
                lang = input()
                if lang == "en":
                    articles = en_articles
                    break
                elif lang == "zh":
                    articles = zh_articles
                    break
                else:
                    clear_error()
                    color_print("Please check your input!", "\033[33m")
            color_print(f"\nPlease choose an article - {len(articles)} in total.\n", "\033[43m")
            while True:
                color_print(f"Enter an integer from 1 to {len(articles)}.", "\033[33m")
                try:
                    index = int(input())
                    if index >= 1 and index <= len(articles):
                        break
                    else:
                        clear_error()
                        color_print(f"Please enter a number from 1 to {len(articles)}!", "\033[33m")
                except ValueError:
                    clear_error()
                    color_print("Please enter a valid number!", "\033[33m")
            article = read_specific_article(lang, index)
        else:
            print("[Error]: Mode selection must be <random> or <specific>!")
            sys.exit(1)

        color_print("\nYou choose the article:", "\033[43m")
        print(f"{article['title']}\n")
        color_print("Here's the article:", "\033[43m")
        print(f"{article['article']}\n")
        keys = get_inputs(article['hints'])
        filled_article = replace(article['article'], keys)
        color_print("You've finished the game! Here's the article:", "\033[43m")
        print(f"{filled_article}\n\n")
        while True:
            color_print("Enter 'y' to copy the article and exit, 'q' to exit directly.", "\033[43m")
            choice = input()
            if choice == "y":
                pyperclip.copy(filled_article)
                break
            elif choice == "q":
                break
            else:
                clear_error()
                print("Please check your input!")
        sys.exit(0)

    finally:
        reset_screen()
