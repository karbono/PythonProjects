import os

timestamp = os.path.getmtime("./guests.txt")

print(os.listdir())
os.mkdir("testDir")
os.chdir("testDir")
os.getcwd()
os.mkdir("newerDir")
os.rmdir("newerDir")

####

dirr = os.getcwd()
for name in os.listdir(dirr):
    fullname = os.path.join(dirr, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
