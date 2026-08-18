# There are few methods in opening a file w - read, r - write, a - append, x - write(no existing file should be there)
# r+ - read and write (It writes on top of existing elements character by character),
# w+ - write and read, a+ - read and append, x+ - write and read
 
f = open('workfile', 'w', encoding="utf-8")
f.write('Hello Udhai\nHow are you ?\n')
f.close()
 
f = open('workfile', 'r', encoding="utf-8")
print(f.read())
f.close()
 
f = open('workfile', 'a+', encoding="utf-8")
f.write("Meow")
f.seek(0)
print(f.read())
print('Before closing', f.closed)
f.close()
print('After closing', f.closed)
 
with open('workfilex', 'a+', encoding="utf-8") as f:
    f.write('Hello Vinay\nHow are you ?\n')
    f.seek(0)
    print(f.readline())
    print(f.readline())
    # print(f.read())
 
print("Checking does open closes automatically: ", f.closed)
 
with open('jsonfile', 'w', encoding="utf-8") as f:
    import json
    x = [1, 'simple', 'list']
    f.write(json.dumps(x))
 
with open('jsonfile', 'r', encoding="utf-8") as f:
    print(json.load(f))