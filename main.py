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


def main():
    frankenstein = Book("books/frankenstein.txt")

main()
