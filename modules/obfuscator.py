import hashlib

class Obfuscator:
    def __init__(self,word:str, method="sha256"):
        self.method = method
        self.word = word
    def hash(self) -> str:
        input_bytes = self.word.encode('utf-8')
        if self.method == "sha256":
            return hashlib.sha256(input_bytes).hexdigest()
        elif self.method == "md5":
            return hashlib.md5(input_bytes).hexdigest()
        elif self.method == "sha1":
            return hashlib.sha1(input_bytes).hexdigest()
        else:
            raise ValueError(f"No method  '{self.method}' in here , wait for update ")



