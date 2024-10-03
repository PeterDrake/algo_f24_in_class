def str_match(text, pattern):
    for i in range(len(text)):
        if text[i:len(pattern)+i] == pattern:
            return i
    return -1