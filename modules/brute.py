from .obfuscator import Obfuscator

class BruteForce:
    def __init__(self, file_path: str, compare: str, method="sha256"):
        self.file_path = file_path
        self.compare = compare
        self.method = method
        self.words = self.load_words()

    def load_words(self):
        try:
            with open(self.file_path, 'r') as file:
                words = file.read().splitlines()
            return words
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' does not exist.")
            return []
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return []

    def compare_hash(self):
        print('@ In case no method select it will be : SHA256 ')
        for word in self.words:
            hashed_word = Obfuscator(word, self.method).hash()
            print(f'@HashCompare [TESTING] -> {word} got : {hashed_word}', end='\r')
            if hashed_word == self.compare:
                print(f"Matching '{word}'")
                return word
        print("\nFind new list word !")
        return None
