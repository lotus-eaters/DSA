def union_using_set(num1,num2):
    return list(set(num1).union(set(num2)))

def union_using_or(num1,num2):
    return list(set(num1)|set(num2))

def union_preserved_order(num1,num2):
    seen=set()
    for i in num1:
        if i not in seen:
            seen.add(i)
    for i in num2:
        if i not in seen:
            seen.add(i)
    return list(seen)

def union_using_dict(num1,num2):
    freq={}
    for x in num1:
        freq[x]=1
    for x in num2:
        freq[x]=1
    return list(freq.keys())

def union_using_2pointers(num1,num2):
    i,j=0,0
    n,m=len(num1),len(num2)
    result=[]
    while i<n and j<m:
        if i>0 and num1[i]==num1[i-1]:
            i+=1
            continue
        if j>0 and num2[j]==num2[j-1]:
            j+=1
            continue
        if num1[i]<num2[j]:
            result.append(num1[i])
            i+=1
        elif num1[i]>num2[j]:
            result.append(num2[j])
            j+=1
        else:
            result.append(num1[i])
            i+=1
            j+=1
    while i<n:
        if i==0 or num1[i]!=num1[i-1]:
            result.append(num1[i])
        i+=1

    while j<m:
        if j==0 or num2[j]!=num2[j-1]:
            result.append(num2[j])
        j+=1
    return result


arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

print(union_using_set(arr1, arr2))
#Output (order not guaranteed):
print(union_using_or(arr1, arr2))
print(union_preserved_order(arr1, arr2))
print(union_using_dict(arr1, arr2))
print(union_using_2pointers(arr1, arr2))