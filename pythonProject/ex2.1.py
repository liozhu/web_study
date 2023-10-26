names=['liozhu','cat','dog','pig']
names.insert(0,'qiang')
names.append('hong')
print(names)
print("only two")
first=names.pop(1)
print(f"sorry,{first},you will not be inxited.")
print(names)
second=names.pop(1)
third=names.pop(1)
forth=names.pop(1)
print(f"sorry,{second},{third},{forth},you will not be invited")
print(names)
print(f"{names[0]},{names[1]},you still will be invited")
del names[0]
del names[0]
print(names)
