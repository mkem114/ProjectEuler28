sum = 1
DIMENSIONS = 2;
incrementer = 2;
count = 1;
for i in range(500): #does n*2 +1 spiral sum
    for j in range (4):
        count += incrementer
        sum += count
    incrementer += DIMENSIONS
print(sum)