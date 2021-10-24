x = [[10,8],
     [2, 4],
     [1,7]]

output = [[0, 0, 0], 
          [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        output[j][i] = x[i][j]
        
for o in output:
    print(o) 