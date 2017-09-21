import telepot
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,False)
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command

    if(command == "ping"):
        bot.sendMessage(chat_id,"pong")
        print"pong"
    if(command == 'pic'):
        bot.sendPhoto(chat_id,open('NIRMITHY.jpg'))
    if(command == "ledon"):
    	GPIO.output(2,True)
	bot.sendMessage(chat_id,"LED is ON now")
    if(command == "ledoff"):
    	GPIO.output(2,False)
	bot.sendMessage(chat_id,"LED is OFF now")
bot = telepot.Bot('321092089:AAG3-sqps6MPk9wR4YRdiWgEdR65cYJYr4Y')
bot.message_loop(handle)


while 1:
     time.sleep(10)
GPIO.cleanup()

