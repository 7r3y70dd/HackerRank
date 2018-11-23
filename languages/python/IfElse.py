N = int(input())
evenTest = N % 2

if evenTest == 0 and N >= 2 and N <= 5:
        print("Not Weird")
elif evenTest == 0 and N >= 6 and N <= 20:
    print("Weird")
elif evenTest == 0 and N > 20:
    print("Not Weird")
elif evenTest != 0:
    print("Weird")