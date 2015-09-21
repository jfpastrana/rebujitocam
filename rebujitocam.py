#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#  Version 1
#  WEB: www.hackaffeine.com
#  Author: Javi
#  Created on: 25/08/2015
#

#!/usr/bin/python
import tweepy
import time
import random
from subprocess import call
from datetime import datetime
from PIL import Image

date = datetime.now()


#Coloca dentro de las comillas tus claves...
CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'
ACCESS_KEY = 'ACCESS TOKEN KEY'
ACCESS_SECRET = 'ACCESS TOKEN SECRET'

#En esta parte nos identifica para poder realizar operaciones
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
auth.secure = True


#Dependiendo de la hora del dia se generan unas frases de forma  aleatoria u otras
#las frases estan escritas en cada uno de los correspondientes ficheros
def random_tweet():
	global phrase
	list = []
	date = int(time.strftime("%H%M"))
	if date >= 1300 and date <= 1759:
        	file = open("/home/pi/Proyectos/rebujitocam/randomText/comida.txt","r")
	if date >= 1800 and date <= 2059:
        	file = open("/home/pi/Proyectos/rebujitocam/randomText/tarde.txt","r")
	if date >= 2100 and date <= 2359:
        	file = open("/home/pi/Proyectos/rebujitocam/randomText/cena.txt","r")
	else:
		file = open("/home/pi/Proyectos/tweetAndalucia/randomText/resto.txt","r")
	for line in file.readlines():
		list.append(line)
	phrase = random.choice(list)

#Hace la foto original
def take_photo():
        global imagen
	global date
	date = time.strftime("%Y_%m_%d_%H_%M_%S")
	path = '/home/pi/Proyectos/rebujitocam/photoOriginal/'
	imagen = path + date + '.jpg'
        print('Taking photo...' + date)
	print('Path...' + imagen)
	cmd = 'raspistill -t 500 -w 2592 -h 1944 -vf -hf -q 100 -ex auto -awb auto -o '  + imagen
	call ([cmd], shell=True)

#Superpone la foto original con la marca de agua, en este caso hackaffeine.com
def merge_logo():
	global f_imagen
	path = '/home/pi/Proyectos/rebujitocam/toSend/'
        f_imagen = path + date + '.jpg'
	background = Image.open(imagen)
	foreground = Image.open('/home/pi/Proyectos/rebujitocam/logo/agua.png')
	background.paste(foreground, (0, 0), foreground)
	background.save(f_imagen)


#MAIN FUNCTION
#update_status('mensaje' o variable) es para actualizar nuestro estado
api = tweepy.API(auth)

random_tweet()
tweet = phrase + date.strftime('%H:%M:%S')

take_photo()
merge_logo()

print(f_imagen)
#Sube el tweet a Twitter
api.update_with_media(filename = f_imagen,status = tweet)

