# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band2))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# List of key value pairs as tuples
print(band.items())

# Verify a key exists
print("guitar" in band)
print("madagascar" in band)

# Change values
band["guitar"] = "Coverme"
band.update({"name": "Benjamin"})

print(band)

# Remove items
print(band.pop("name"))  # return value of item removed
print(band)

band["drum"] = "bonham"
print(band)

print(band.popitem())  # return a tuple of item removed
print(band)

band["drum"] = "bonham"
del band["drum"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries
band2 = band  # create a reference (bad way of copying dicts)
print("Bad copy")
print(band2)
print(band)

band2["drum"] = "Michael"
print(band)

del band2

# best way of copying dicts
print("good way")
band2 = band.copy()  # good way of copying dict

band2["drum"] = "David"
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)


# Nested dictionaries

member1 = {
    "name": "Ben",
    "instrument": "vocals"
}

member2 = {
    "name": "Pagen",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band.get("member1"))
