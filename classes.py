class Phrase:
    def __init__(self, word):
        self.word = word
        self.length = len(word)
        self.symbols = []
        self.display = []
        for i in word:
            self.symbols.append(i)
        for i in word:
            self.display.append("-")

    def isPresent(self, a):
        for x in range(0,self.length):
            if a == self.word[x]:
                self.display[x] = a

    def showWord(self):
        str = ""
        print(str.join(self.display))

    def isDone(self):
        flag = True
        for i in self.display:
            if i == "-":
                flag = False
        return flag