

alphabet = {'A':3,'B':2, 'C':1, "D":2,'E':4,
            'F':3, 'G':1,'H':3,'I':1,'J':1,
            'K':3, 'L':1,'M':3, 'N':2, 'O':1,
            'P':2, 'Q':2,'R':2,'S':1, 'T':2,
            'U':1, 'V':1, 'W':1, 'X':2, 'Y':2,
            'Z':1}

def nameCalc(arr):
    resArr = []
    if len(arr) < 3:
        return arr[0] * 10 + arr[1]
    else:
        for i in range(len(arr)-1):
            k = arr[i]+ arr[i + 1]
            if k >=10:
                resArr.append(k%10)
            else:
                resArr.append(k)
        return nameCalc(resArr)

n, m = map(int, input().split())
a , b = input().split()

bigNum = max(n, m)
minNum = min(n, m)
i = 0
array = []




while(i < minNum):

    array.append(alphabet[a[i]])
    array.append(alphabet[b[i]])
    i +=1

while(i < bigNum):
    if n > m:
        array.append(alphabet[a[i]])
    else:
        array.append(alphabet[b[i]])
    i +=1

print(nameCalc(array),'%',sep='')