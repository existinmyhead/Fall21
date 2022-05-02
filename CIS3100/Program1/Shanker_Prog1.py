# Nitya Shanker
# September 28, 2021
# ECE 3100
# Program 1

# TASK 2
myNum = 50
myStr = "hi"
myList = [1, 2, 3]

print(myNum, myStr, myList)  # 50 hi [1, 2, 3]
print(myNum, myStr, myList, sep=":")  # 50:hi:[1, 2, 3]
print("myNum: " + str(myNum) + " myStr: " + myStr)  # myNum: 50 myStr: hi
print("myNum: %-4d y: % -5.2f" % (myNum, myNum))  # myNum: 50 y: 50.00

myStr = "ABC"
myStr1 = "ABCABC"
myStrlen = "myStr length ="

print(myStrlen, len(myStr))
myStr1len = "myStr length ="
print(myStr1len, len(myStr1))

myStr = "ABC"
print('A' in myStr)
print('AB' in myStr)
print('AC' in myStr, "\n")

# TASK 3
A = {"a", "b", "c"}
B = {"a", "b", "c", "d", "a", "c", "e"}
C = {"a", "b", "c", "b"}

# 1) Set Cardinality
setsize = "size of set"

print(setsize, "A =", len(A))
print(setsize, "B =", len(B))
print(setsize, "C =", len(C), "\n")

# 2) Subset (x1 and x2 in A, B, C)
x1 = {"a"}
x2 = {"d"}
subsetof = "is a subset of"

print("x1", subsetof, "A is", x1.issubset(A))
print("x1", subsetof, "B is", x1.issubset(B))
print("x1", subsetof, "C is", x1.issubset(C), "\n")
print("x2", subsetof, "A is", x2.issubset(A))
print("x2", subsetof, "B is", x2.issubset(B))
print("x2", subsetof, "C is", x2.issubset(C), "\n")

# 3) Subset (x in A, B, C)
x = {"a", "d"}

print("x", subsetof, "A is", x.issubset(A))
print("x", subsetof, "B is", x.issubset(B))
print("x", subsetof, "C is", x.issubset(C), "\n")

# 4) Set Equality
print("A = B is", A==B)
print("A = C is", A==C, "\n")

# TASK 4
X1 = {"A", "B", "C", 2, 3, 5}
X2 = {3, 5, 7, "B", "D"}

# 1) Set Union
print("Union of X1 and X2 is", X1.union(X2))

# 2) Set Intersection
print("Intersection of X1 and X2 is", X1.intersection(X2))