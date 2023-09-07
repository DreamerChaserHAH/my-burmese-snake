hello = "world "
print(dir(hello))
print(hello.lower())
print(hello.upper())
print(hello.removeprefix("wo"))

email = "contact@htetaung.com Htet Aung Hlaing"
start = email.find('@')
end = email.find(' ', start)
print(email[start + 1:end])

word="banana"
print(word.find("na"))