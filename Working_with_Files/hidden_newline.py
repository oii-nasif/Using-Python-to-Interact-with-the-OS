file = open("/home/nasif/Dropbox/GitHub/Using Python to Interact with the OS(Linux)/Working_with_Files/spider.txt")
lines = file.readlines()
file.close()

lines.sort()
print(lines)