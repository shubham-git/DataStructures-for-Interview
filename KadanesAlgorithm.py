n = int(input("Enter the size of array"))

a = []
for i in range(0, n):
    a.append(int(input()))

max_so_far = max_ending_here = 0


def kadanesalgo(a, size):
    for i in range(0, n):
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


for i in range(0,n):
    if a[i]>0:
        print(kadanesalgo(a,n))
        break
else:
    a.sort()
    print(a[n-1])
