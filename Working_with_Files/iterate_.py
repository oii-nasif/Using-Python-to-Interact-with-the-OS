with open("/home/nasif/Dropbox/GitHub/Using Python to Interact with the OS(Linux)/Working_with_Files/spider.txt") as file:
    for line in file:
        print(line.strip().upper())