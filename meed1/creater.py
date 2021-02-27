
en2 = input('Enter text: ')
my_file = open('meed.txt', 'w')
my_file.write(en2)
my_file.close()

com = input('Enter command: ')
while com != 'close':
	if com == 'further':
		print('1. Display text')
		print('2. Enter text')
		print('3. Delete text')
	com1 = input('Enter num: ')
	if com1 == '1':
		print(en2)
	elif com1  == '2':
		en2 = input('Enter text: ')

	com = input('Enter command: ')
exit()




input()
