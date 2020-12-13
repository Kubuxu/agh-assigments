import random

inArr = [random.randrange(500) for _ in range(50)]
print(f"Random order: {inArr}")

outArr = inArr[:]

# bubble sort
for i in range(len(outArr)):
    for j in range(0, len(outArr)-i-1):
        if outArr[j] <= outArr[j+1]:
            outArr[j], outArr[j+1] = outArr[j+1], outArr[j]

print(f"After sort: {outArr}")
inArr.sort(reverse = True)
if inArr == outArr:
    print("Good sort")
else:
    print("Bad sort")

