#  suffix trie construction
class SuffixTrie:
    def __init__(self, string):
        self.root = {} # hashtable
        self.endSymbol = "*" # for ending
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrie(self, string):
        for i in range(len(string)):
            self.insert(i, string)

    def insert(self, i , string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[i]
            if letter  not in node:
                node[letter] = {}

            node = node[letter]
        node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False

            node = node[letter]
        return self.endSymbol in node

