import csv
import datetime
import locale
locale.setlocale(locale.LC_ALL, '') #siparis tarihinin turkce gozukmesi icin

# menuyu olusturmak icin gerekli olan method
def menuyu_olustur():
    olustur = open("Menu.txt", "w", encoding="Utf-8")
    olustur.write("*Lütfen bir Pizza tabani seçiniz:\n 1: Klasik\n 2: Margarita\n 3: Türk Pizza\n 4: Sade Pizza\n*ve sececeginiz sos:\n 11: Zeytin\n 12: Mantarlar\n 13: Keçi Peyniri\n 14: Et\n 15: Soğan\n 16: Misir\n *Tesekkür ederiz!\n")
    olustur.close()

# menuyu okumak icin gerekli olan method
def menuyu_oku(baslangic=""):
    with open("Menu.txt", "r",encoding="Utf-8") as x:
        if baslangic == "":
            sayac = 0
            x.seek(96)
            while sayac < 13:
                icerik = x.readline()
                print(icerik, end="")
                sayac += 1
        else:
            sayac = 0
            while sayac < 5:
                icerik = x.readline()
                print(icerik, end="")
                sayac += 1

# ana class'imiz. Pizza
class Pizza:
    # tanımlamaları yapıyoruz. Fiyat ve tanım bilgisi istiyoruz
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    # bu fonksiyon ile gelen tanım bilgisini döndürüyoruz return ile
    def get_description(self):
        return self.description

    # bu fonksiyon ile de gelen fiyat bilgisini döndürüyoruz return ile
    def get_cost(self):  
        return self.cost

# pizza sınıfından oluşturulan alt sınıflar
class Klasik_Pizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 20.99)

class Margherita(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza", 25.99)

class Turk_Pizzasi(Pizza):
    def __init__(self):
        super().__init__("Turk Pizzasi", 29.99)

class Dominos_Pizza(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza", 36.99)

# burada ise “Decorator” sınıfını olusturuyoruz bu da sosların kalıtım aldığı ana sınıf olacak.
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    #burada hem sosların(zeytin,peynir vs) gibi seylerin fiyatlarını ve pizza'nin fiyatlarını topluyor. kapsülleme burada yapmıs oluyoruz
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    #burada da hem sosların hem de pizzanın aciklamalarını alıyoruz.
    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

# Decorator ust sınıfını kullanarak(kalıtım alarak) olusturdugumuz class'lar
class Zeytin(Decorator):
    def __init__(self, Pizza):
        super().__init__(Pizza)
        self.description = "Zeytin"
        self.cost = 3.00

class Mantar(Decorator):
    def __init__(self, Pizza):
        super().__init__(Pizza)
        self.description = "Mantar"
        self.cost = 4.00

class Keci_Peyniri(Decorator):
    def __init__(self, Pizza):
        super().__init__(Pizza)
        self.description = "Keci Peyniri"
        self.cost = 5.00

class Et(Decorator):
    def __init__(self, Pizza):
        super().__init__(Pizza)
        self.description = "Et"
        self.cost = 9.00

class Sogan(Decorator):
    def __init__(self, Pizza):
        super().__init__(Pizza)
        self.description = "Sogan"
        self.cost = 5.00

class Misir(Decorator):
    def __init__(self, Pizza):
        super().__init__(Pizza)
        self.description = "Misir"
        self.cost = 4.00

##main##
def main():
    menuyu_olustur()

    # pizza seciminin yapılması
    menuyu_oku(5)
    pizza_secim = input("Lutfen istediginiz pizzayi seciniz: ")
    if pizza_secim == "1":
        Pizza = Klasik_Pizza()  # secimlere gore pizza nesneleri olusturuluyor
    elif pizza_secim == "2":
        Pizza = Margherita()
    elif pizza_secim == "3":
        Pizza = Turk_Pizzasi()
    elif pizza_secim == "4":
        Pizza = Dominos_Pizza()
    else:
        print("Yanlis secim yaptiniz. Tekrar deneyiniz. ")
        return

    # sos secimlerinin yapılması
    menuyu_oku() #menuyu ekranda gosteriyoruz
    sos_secimleri = [] #secilen sosları tutacak olan dizi
    while True:
        sos_Secim = input("Lütfen bir sos secin(q ile cikis): ")
        if sos_Secim.lower() == "q": #q'ya bastıysak cikis yapsin
            break
        elif sos_Secim == "11": #11 yazdiysak 
            Pizza = Zeytin(Pizza) #zeytin class'i olusturulsun
        elif sos_Secim == "12": #12 yazdiysak
            Pizza = Mantar(Pizza) #mantar class'i olusturulsun
        elif sos_Secim == "13":
            Pizza = Keci_Peyniri(Pizza)
        elif sos_Secim == "14":
            Pizza = Et(Pizza)
        elif sos_Secim == "15":
            Pizza = Sogan(Pizza)
        elif sos_Secim == "16":
            Pizza = Misir(Pizza)
        else:
            print("Lütfen geçerli bir sos seçin.")
            return
            
        sos_secimleri.append(int(sos_Secim))#sos secimlerini append fonksiyonu ile sos secimleri dizisinin icine atıyoruz
         
    # Toplam fiyat hesaplanmasi
    total_cost = Pizza.get_cost()
    print("Toplam Fiyat: ", round(total_cost,2))

    # Pizza ve sos seciminin belirlenmesi
    order_description = Pizza.get_description()
    print("Detaylar:", order_description)
    
    # Kullanici bilgilerinin alınmasi ve csv dosyasına kaydedilmesi
    isim = input("Adiniz: ")
    soyisim = input("Soyadiniz: ")
    tc = input("Tc Numaraniz: ")
    kredi_karti_numarasi = input("Kredi karti numaraniz: ")
    kredi_karti_sifreniz = input("Kredi karti sifreniz: ")
    siparis_zamani = datetime.datetime.now().strftime("%c") #tam tarihi alabilmek icin strftime hazir fonksiyonunu kullanıyoruz. 
    
    # musteri bilgilerini veritabanina kaydediyoruz.
    with open("Orders_Database.csv","a",newline='',encoding="Utf-8") as dosyaad:
        write = csv.writer(dosyaad)
        write.writerow([isim, soyisim, tc, kredi_karti_numarasi, kredi_karti_sifreniz, siparis_zamani, order_description,round(total_cost,2)])
    print("Siparişiniz başarıyla kaydedilmistir. Afiyet olsun.")   
if __name__ == "__main__":
    main()