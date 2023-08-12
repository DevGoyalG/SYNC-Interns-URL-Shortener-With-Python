# SYNC Interns - Task 3 - URL Shortener With Python 

import string
import random

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def generate_short_alias(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))

    def shorten_url(self, long_url):
        short_alias = self.generate_short_alias()
        self.url_mapping[short_alias] = long_url
        return short_alias

def main():
    url_shortener = URLShortener()

    while True:
        print("Press 1 to Shorten URL")
        print("Press 2 to Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            long_url = input("Enter the URL to shorten: ")
            short_alias = url_shortener.shorten_url(long_url)
            print(f"Shortened URL: https://shortlink.com/{short_alias}")

        elif choice == "2":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
