
file = open("sample.txt", "w")
file.write("My name is Ella")
file.close()
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
