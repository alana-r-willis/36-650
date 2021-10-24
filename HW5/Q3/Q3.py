def one_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1: 
        return False
    count = 0
    index1 = 0
    index2 = 0
    while index1 <len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            count += 1
            index1, index2 = (index1+1, index2) if len(str1) > len(str2) else (index1, index2+1) if len(str2) > len(str1) else (index1+1, index2+1)
        else:
            index1 +=1;index2 +=1
    count = count+1 if index1 <len(str1) or index2 < len(str2) else count
    return count <= 1
    

print(one_away("pale","ple"))
print(one_away("pales","pale"))
print(one_away("pale","bale"))
print(one_away("pale","bake"))