List = ["Student 1", 32, 56, "School"]
print(List)

fruits = ["Mango", "Strawberry", "Pineapple", "Dragonfruit", "Orange"]
# Access the element using index
print("First Element", fruits[0])
print("Last Element", fruits[4])
print("Second Element", fruits[1])
print("List Size:", len (fruits))

fruits.append("Banana")
print("After Adding:", fruits)

fruits.sort()
print("After sorting in asc order", fruits)

fruits.reverse()
print("After sorting in desc order", fruits)

print('Multiplythe List:', fruits * 2)

print("Slicing:", fruits[:6])

fruits.clear()
print("Clearing the List:", fruits)