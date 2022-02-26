n = input()
left=0
right=0
for i in range(len(n)//2):
    left = left+int(n[i])
for i in range((len(n)//2),len(n)):
    right = right+int(n[i])
if left == right:
    print("LUCKY")
else:
    print("READY")

