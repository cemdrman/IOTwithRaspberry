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
    api_key = "Sizin Key'iniz" #twitter icin kullanilacak API
    veriler = {"api_key":api_key,"status":tweetIcerigi}
    istek = requests.post("https://api.thingspeak.com/apps/thingtweet/1/statuses/update",data = veriler)
    print ("Tweet Gonderildi!")
    #Request Nedir?
    #Bu islem bir web-sitesine girme islemi islemi olarak düsünebiliriz. Ornegin facebook.com yazıp girdigimizde
    #bu siteye bir Request(istek) yapmis oluruz ve sitenin bize bir responce(cevap) vermesini bekleriz.

    #Post Nedir?
    #Yukarıdaki islemde requests.post() isimli bir fonksiyon cagrilmistir. Buradaki Post http protokolünün bize sagladigi
    #bir islemdir. Bunun gibi bu protokol bizler;
    # Post
    # Get
    # Delete gibi islemleri sunmustur.Detaylı bilgi http://bcakir.com/get-ve-post-metodu ve benzer bloklardan yararlanabilirsiniz!



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




#Program Aciklamasi

#Uygulamanin amaci: RaspberryPi ile olcülen degeri thingspeak.com da olusturdugumuz field'lara yazmak ve yine thingspeak kullanarak
#tweet atma islemi. olusturulan field'lara thingSpeakeSicaklikVeNemYaz(sicaklik,nem) fonksiyonu ile veri yazabilirsiniz.
#fonksiyon icinde tanimlanmis api_key kismini degistirerek sizler de deneyebilirsiniz yada benim olusturdugum alana direkt deneyebilirsiniz.
#Tweet atma isleminde ise biz direk olarak Twitter API kullanmıyoruz. Cunku bu asamada bu api'yi kullanmak zor olacaktir.
#thingspeak araciligi ile tweet atma islemini gerceklestirdik.


#Neden Fonksiyon Kullanmaliyiz?

#Karmasik problemler fonksiyonlar ile;

#daha kolay yonetilir
#problem daha iyi analiz edilir
#hata karsisinda sorunun tespiti daha hizlidir.
#cozum adim adim yapilmis olur.
#kod okunurlugu artmis olur.(ana programa baktigimizda sadece 8 satirlik kod bulunmaktadir.Kodun anlasilabilirligi artmistir.)
