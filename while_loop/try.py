num = 1000
count = 0
while count <= 10000:
    if num % 9==0:
        print(num, end=" ")
        count = count + 1

        if count % 10 == 0:
            print()
    num=num+1
            
