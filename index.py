import requestTest
print(requestTest.r.text)
filename = 'index.html'
with open(filename, 'w') as file_object:
    file_object.write(requestTest.r.text)