datafile = open('data.csv', 'r', encoding= "UTF-8")

for line in datafile.readlines():
    data = line.strip().split(',')
    print(data[0])
    print(data[1])
    print(data[2])
    print('-'*10)