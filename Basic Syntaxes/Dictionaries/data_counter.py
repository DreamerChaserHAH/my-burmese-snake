# List is square brackets
#dictionary is curly brackets

counts = dict()
names = ["Jack", "Mark", "Mark", "Jack"]
for name in names:
        counts[name] = counts.get(name, 0) + 1 #Simplify a lot of things
print(counts)
