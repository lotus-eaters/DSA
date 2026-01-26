def reverse_words_brute(str):
    words=[]
    word=""
    for ch in str:
        if ch!=" ":
            word+=ch
        else:
            words.append(word)
    return words.reverse()
# Time Complexity: O(N),We traverse the string once to collect words (O(N)) and once more to reverse and join them (O(N)). Hence total time is O(N).

# Space Complexity: O(N),We store all words in a separate list/array, requiring extra space proportional to the number of characters.
def reverse_words_optimal(str):
    i=len(str)-1
    result=""
    while i>=0:
        while i >=0 and str[i]==' ':
            i-=1
        if i<0:
            break
        end=i
        while i>=0 and str[i]!='':
            i-=1
        word=str[i+1:end+1]

        if result!="":
            result+=" "
        
        result+=word
    return result