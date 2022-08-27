def largestNum(x):
    #Firstly, we convert a list into a string array 
    for i in range(len(x)):
        x[i]=str(x[i])
    #After that we find the largest element by swapping.
    for i in range(len(x)):
        for j in range(1+i,len(x)):
            if x[j]+x[i]>x[i]+x[j]:
                x[i],x[j]=x[j],x[i]
    result=''.join(x)
    #Edge Case: If all elements are 0, answer must be 0
    if(result=='0'*len(result)):
        return '0'
    else:
        return result
         
#input value that I will make the list what you want and attend on gap between number that will split each indexes
num = list(map(int, input("Type number with space: ").split()))
print('list: ', num)
print("The largest number is",largestNum(num))