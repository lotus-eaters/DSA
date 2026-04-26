from collections import Counter

def non_repeating_char(s):
    frequency = Counter(s)
    for c in s:
        if frequency[c]==1:
            return c

print(non_repeating_char('sssiioonnhoooiiuytyy'))