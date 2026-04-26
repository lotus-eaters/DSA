def is_anagram(s1,s2):
    return sorted(s1.replace(" ","").lower()) == sorted(s2.replace(" ","").lower())

s1 = "listen"
s2 = "silent"
print(is_anagram(s1,s2))