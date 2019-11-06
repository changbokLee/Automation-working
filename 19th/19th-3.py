user_input = input('Input:')
datafile = open('textfile.txt', 'w', encoding="UTF-8")
datafile.wrtie(user_input+'\n')