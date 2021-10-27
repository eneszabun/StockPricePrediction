from Altın import Altın
from BTC import BTC
from Euro import Euro
from Sterlin import Sterlin

class Doviz:
    @staticmethod
    def initApp():      
        msg="1:Altın\n2:Euro\n3:BTC\n4:Sterlin\n5:Çıkış"
        while True:
            print(msg)
            secim=input("İncelemek istediğiniz birim: ")
            if secim=='1':
                Altın.grafik()
            elif secim=='2':
                Euro.grafik1()
            elif secim=='3':   
                BTC.grafik2()
            elif secim=='4':
                Sterlin.grafik3()
            elif secim=='5':
                break
            else:
                print("Geçersiz istekte bulundununuz!")
Doviz().initApp()