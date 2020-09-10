class MyClass:
  nama = "contohClass"

kelas = MyClass()
print(kelas.nama)

class person:
  def __init__(obj, name, age):
    obj.name = name
    obj.age = age
  
  def myFunc(abc):
    print("Nama saya adalah " + abc.name)
    print("Umur saya adalah " + str(abc.age))

run = person("Budi", 30)

# print(run.name)
# print(run.age)

run.myFunc()