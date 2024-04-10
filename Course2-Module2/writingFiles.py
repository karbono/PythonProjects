import os

texto = open("./testingNumber20.txt", "w")
texto.write("Esto es una prueba")
texto.close()
texto = open("./testingNumber20.txt")
print(texto.readline())
texto.close()

os.remove("./testing.txt")

os.listdir()

os.rename("./testMove.txt", "")

os.rmdir("testDir")
os.mkdir("testDir")
os.mkdir("./testDir2")
os.mkdir("../testDir3")

os.rmdir("../testDir3")

os.mkdir("test")
os.getcwd()
os.listdir()

os.chdir("Course2-Module2")
os.getcwd()
os.mkdir("test")
os.listdir()
os.rmdir("test")

os.path.getsize("cpu_checker.py")
os.path.exists("Course2-Module2")

e = open("CSVfiles.py", "w")
e.close()

import os
os.rename("CSVfiles.py", "./CSVfiles.py")