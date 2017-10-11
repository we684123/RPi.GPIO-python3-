import time
import RPi.GPIO as GPIO

#clear surroundings
GPIO.cleanup()
#set GPIO to BCM mode
GPIO.setmode(GPIO.BCM)

GPIO.setup(5,GPIO.OUT)#e
GPIO.setup(6,GPIO.OUT)#d
GPIO.setup(13,GPIO.OUT)#c
GPIO.setup(19,GPIO.OUT)#p
GPIO.setup(12,GPIO.OUT)#g
GPIO.setup(16,GPIO.OUT)#f
GPIO.setup(20,GPIO.OUT)#a
GPIO.setup(21,GPIO.OUT)#b
#========================================================
#set to pin mode(out or in)
def ctrlLED(y):
	if (y == 'a'):
		GPIO.output(20,1)
	elif (y == 'b'):
		GPIO.output(21,1)
	elif (y == 'c'):
		GPIO.output(13,1)
	elif (y == 'd'):
		GPIO.output(6,1)
	elif (y == 'e'):
		GPIO.output(5,1)
	elif (y == 'f'):
		GPIO.output(16,1)
	elif (y == 'g'):
		GPIO.output(12,1)
	elif (y == 'P'):
		GPIO.output(19,1)
	else :
		print("bug.....")
	return 0
#========================================================
def FORR(x):
	l = len(x)
	for i in range(l):
		ctrlLED(x[i])
	return 0
#========================================================
def clsA():
	GPIO.output(20,0)
	GPIO.output(21,0)
	GPIO.output(13,0)
	GPIO.output(6,0)
	GPIO.output(5,0)
	GPIO.output(16,0)
	GPIO.output(12,0)
	GPIO.output(19,0)
	return 0
#========================================================
def x16(char):
	#0~9+a~f+'P'
	clsA()
	if char == 0 :
		r = ['a','b','c','d','e','f']
		FORR(r)
	elif char == 1 :
		r = ['b','c']
		FORR(r)
	elif char == 2 :
		r = ['a','b','d','e','g']
		FORR(r)
	elif char == 3 :
		r = ['a','b','c','d','g']
		FORR(r)
	elif char == 4 :
		r = ['b','c','f','g']
		FORR(r)
	elif char == 5 :
		r = ['a','c','d','f','g']
		FORR(r)
	elif char == 6 :
		r = ['a','c','d','e','f','g']
		FORR(r)
	elif char == 7 :
		r = ['a','b','c']
		FORR(r)
	elif char == 8 :
		r = ['a','b','c','d','e','f','g']
		FORR(r)
	elif char == 9 :
		r = ['a','b','c','d','f','g']
		FORR(r)
	elif char == 10 :
		r = ['a','b','c','e','f','g']
		FORR(r)
	elif char == 11 :
		r = ['c','d','e','f','g']
		FORR(r)
	elif char == 12 :
		r = ['d','e','g']
		FORR(r)
	elif char == 13 :
		r = ['b','c','d','e','g']
		FORR(r)
	elif char == 14 :
		r = ['a','d','e','f','g']
		FORR(r)
	elif char == 15 :
		r = ['a','e','f','g']
		FORR(r)
	elif char == 16 :
		r = ['P']
		FORR(r)
	elif char == 17 : #h
		r = ['c','e','f','g']
		FORR(r)
	elif char == 18 : #p
		r = ['a','b','e','f','g']
		FORR(r)
	elif char == 19 : #y
		r = ['b','c','f','g']
		FORR(r)
	elif char == 20 : #i
		r = ['e','f']
		FORR(r)
	elif char == 21 : #r
		r = ['a','e','f']
		FORR(r)
	elif char == 22 : #t
		r = ['d','e','f','g']
		FORR(r)
	else:
		print('WTF hava a debug...')
	return 0
#======================================================== start
while True:
	hb = [17,10,18,18,19,11,20,21,22,17,14,10,19]
	for x range(1,13):
		#char = int(input("pleas key a chat from \n(0~9 or a~f(10~22) or 'P'(30) or 'S'(31)):"))
		char = hb[x]
		if (char >= 0 and char <= 9 ) :
			x16(char)
			print("0~9")
		elif(char >= 10 and char <= 22 ) :
			x16(char)
			print("a~z")
		elif (char == 30) :
			x16(16)
			print("P")
		elif (char == 31) :
			clsA()
			print("S")
		elif (char == 40) :
			for i in range(17) :
				x16(i)
				time.sleep(0.2)
		else:
			print("whar are you Fxxx doing?")
		time.sleep(0.4)
#========================================================
