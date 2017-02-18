class Quote():
    def __init__(self, person, words):
        self.peron = person
        self.words = words
    def who(self):
        return self.peron
    def says(self):
        return self.words + "."

class Questionquote(Quote):
    def says(self):
        return self.words + "??"

class ExclamationQuote(Quote):
    def says(self):
        return self.words + "!!"

class BabblingBrrok():
    def who(self):
        return "Brook"
    def says(self):
        return "Babble"

hunter = Quote("Ajhj jhh", "I am jjdsn jbb")
print(hunter.who(), "Says", hunter.says())
hunter1 = Questionquote("ABCD", "I am the one")
print(hunter1.who(), "Says", hunter1.says())
hunter1 = ExclamationQuote("EEEE", "I PP ii UU yy")
print(hunter1.who(), "Says", hunter1.says())
brook = BabblingBrrok()
print(brook.who(), "Says", brook.says())