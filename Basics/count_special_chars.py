def count_char_types(str):
    special_chars=0
    digits=0
    alphabets=0
    for s in str:
        if s.isalpha():
            alphabets+=1
        elif s.isdigit():
            digits+=1
        else:
            special_chars+=1
    return special_chars,digits,alphabets

s="Hello@123!"
a,b,c=count_char_types(s)
print(a,b,c)
