word = input("Whats the name of your first born child? ")
count = sum(char.isalpha() for char in word)
if word == "owen":
    print("I don't want that thing")
else:
    print("I will take", count, "days to kidnap", word)