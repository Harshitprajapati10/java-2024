# Lc 58
# find the length of last word

def length_of_last_word(s):
    return len(s.split()[-1])

s = "   fly me   to   the moon  "
print(length_of_last_word(s))
print(length_of_last_word("luffy is still joyboy"))
print(length_of_last_word("Hello World"))