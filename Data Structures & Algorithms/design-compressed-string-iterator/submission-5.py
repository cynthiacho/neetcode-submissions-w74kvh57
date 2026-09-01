class StringIterator:
    def __init__(self, compressedString: str):
        self.compressed = compressedString
        self.ptr = 0
        self.char = ''
        self.count = 0

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        self.count -= 1
        return self.char

    def hasNext(self) -> bool:
        if self.count > 0:
            return True
        if self.ptr >= len(self.compressed):
            return False
        
        self.char = self.compressed[self.ptr]
        self.ptr += 1
        num = 0
        while self.ptr < len(self.compressed) and self.compressed[self.ptr].isdigit():
            num = num * 10 + int(self.compressed[self.ptr])
            self.ptr += 1
        self.count = num
        return True