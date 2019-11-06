datafile = open('data.txt' , 'r', encoding= 'UTF-8')

line = datafile.readline().strip()
print(line)