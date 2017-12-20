#--------fonksiyonlar-----

def tanimla():
    # initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    # read data using pin 14
    instance = dht11.DHT11(pin=14)

def sicaklikVeNemOku():
    # initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup
    # read data using pin 14
    instance = dht11.DHT11(pin=14)


def thingSpeakeSicaklikVeNemYaz(okunanSicaklik,okunanNem):
    api_key = "SD4CAHXAFHVUE8L8" #thingspeak'e yazmak icin olusturulan api_key kendi api_key'inizi yazabilirsiniz!
    istek = urllib.urlopen("https://api.thingspeak.com/update?api_key={}&field1={}&field2={}".format(api_key,okunanSicaklik,okunanNem))
    print ("Veriler Gonderildi!")

def tweetAt(tweetIcerigi):
    api_key = "N5M6WI76ZP9PR84V" #twitter icin kullanilacak API
    veriler = {"api_key":api_key,"status":tweetIcerigi}
    istek = requests.post("https://api.thingspeak.com/apps/thingtweet/1/statuses/update",data = veriler)
    print ("Tweet Gonderildi!")
    #Request Nedir?
    


#----------


#Ana program

#import RPi.GPIO as GPIO
#import dht11
import urllib
import requests

raspberrySicaklik = 26 # sensorden okunan sicaklik degerini temsil etmektedir.
raspberryNem = 30  # sensorden okunan nem degerini temsil etmektedir.
tweet = "#Training #IOT #T3Vakfi @T3Vakfi This tweet has been sent by #RaspberryPi sicaklik = {} ".format(raspberrySicaklik)


if raspberrySicaklik > 25:
    thingSpeakeSicaklikVeNemYaz(raspberrySicaklik,raspberryNem)
    tweetAt(tweet)
