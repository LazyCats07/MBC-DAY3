print(10>9)

print(10 + 2)
print(10 % 2)
print(10 * 2)
print(10 / 2)
print(10 - 2)

# Data types 
# integer .numerical = 10, 20, 100

# list [] 
mylist = ["apple", "Banana", "Durian"]
print(mylist[0])

# Menggunakan append dan insert untuk menambah element

# II. Tuple ()
thistuple = ("Apple")
print(type(thistuple))
print(thistuple)


# Merubah Tuple
thistuple = ("Apple", "durian", "Ceri")
y = list(thistuple)
y.remove("Apple")
thistuple = tuple(y)

print(thistuple)

tuple1 = ("Orange", [10,20,30], (5,15,20))

print(tuple1)

# III. Dictionaty
thisdict = {
    "brand" : "ford",
    "model" : "Mustang", 
    "year" : 1964
}

print(thisdict)