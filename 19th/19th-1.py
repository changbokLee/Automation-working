datafile = open('data.txt', 'r', encoding= 'UTF-8')

line = 'init'
while line:
    line = datafile.read()
print(line)