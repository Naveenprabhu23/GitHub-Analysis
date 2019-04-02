import csv
reader = open("UserData.csv", "r")
lines = reader.read().split("\n")
reader.close()

writer = open("file.csv", "a",newline="")
for line in set(lines):
    writer.write(line + "\n")#
writer.close()
