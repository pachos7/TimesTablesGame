import random as rd
from playsound import playsound

lives = 5
points = 0

#file = open('maxpoints.txt','w+')
maxPointsFile = open('maxpoints.txt','r')
maxP = int(maxPointsFile.readline())
maxPointsFile.close()

print('\n Your previous record was %s points.\n' % maxP)

while True:

	if lives == 0:
		print(' GAME OVER !!!')
		print(' Your record was %s points.' % points)
		if points > maxP:
			print(' Congratulations, This is a NEW RECORD!!!!')
			maxPointsFile = open('maxpoints.txt', 'w')
			maxPointsFile.write(str(points))
		playsound('Dead.wav')
		exit(0)

	print(' You have ' + str(lives) + ' lives.')
	a = int(rd.random() * 13)
	b = int(rd.random() * 13)
	inputData = input(str(a) + ' x ' + str(b) + ' ? ')

	if inputData.isnumeric():
		c = int(inputData)

		if c == (a * b):			
			points += 1
			print('Points:%s' % points)
		else:
			print('Gotcha!. The answer was ' + str(a * b))
			lives -= 1
			playsound('lose_a_live.wav')

	else:
		print('Your data makes no sense:' + inputData + '. The answer was ' + str(a * b))
		lives -= 1
		playsound('lose_a_live.wav')

