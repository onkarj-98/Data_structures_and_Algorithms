import string


def canConstruct(target, wordBank):
    if target == "":
        return True
    for word in wordBank:
        if target.index(word) == 0:
            length = len(word)
            suffix =  target[length:]
        if canConstruct(suffix, wordBank):
            return True
    return False


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
