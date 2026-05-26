l1 = [10,20,30,50,70,80,90]
l2 = [2,4,5,6,7,80,70]
l3 = [120,23,45,65,70,80,130]
s1 = set(l1)
s2 = set(l2)
s3 = set(l3)

s4 = s1.intersection(s2)
s5 = s4.intersection(s3)

print(s5)
