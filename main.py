class Book:
    def __init__(self, path):
        self.path = path
        self.text_content = self.__get_text_content()
        self.word_count = len(self.text_content.split())
        self.char_counts = self.__get_char_count()
    
    def __get_text_content(self):
        with open(self.path) as f:
            text_content = f.read()
        return text_content

    def __get_char_count(self):
        char_count = {}
        for char in self.text_content:
            char = char.lower()
            if char not in  char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
        return char_count

    def print_report(self):
        print(f"--- Begin report of {self.path} ---")
        print(f"{self.word_count} words found in the book")
        char_list = self.__get_chars_as_list()
        for char in char_list:
            if char != "\n":
                print(f"The '{char}' character was found {self.char_counts[char]} times")

    def __get_chars_as_list(self):
        char_list = list(self.char_counts.keys())
        char_list.sort()
        return char_list


def main():
    frankenstein = Book("books/frankenstein.txt")
    frankenstein.print_report()

main()
