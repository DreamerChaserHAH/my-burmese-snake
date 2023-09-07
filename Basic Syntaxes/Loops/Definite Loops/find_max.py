max = None
print("At the start", max)
for num in [10, 20, 5, 2, 5]:
    if max is None or num > max:
        max = num
print("At the end", max)