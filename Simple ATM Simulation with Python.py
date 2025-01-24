class Kullanici:
  def __init__(self,isim,sifre):
    self.isim = isim
    self.__sifre = sifre
    self.bakiye = 0

  def sifre_dogrula(self,girilen_sifre):
    return girilen_sifre == self.__sifre

class ATM:
  def __init__(self,kullanici):
    self.kullanici = kullanici
    self.bakiye = 1000

  def para_yatir(self,miktar):
    if miktar > 0:
      self.bakiye += miktar
      print(f"{miktar} TL para yatırıldı. Yeni bakiye: {self.bakiye} TL")
    else:
      print("Geçersiz miktar!")

  def para_transferi(self,alici,miktar):
    if miktar > 0 and miktar <= self.bakiye:
      self.bakiye -= miktar
      alici.bakiye += miktar
      print(f"{miktar} TL para transfer edildi. Yeni bakiye: {self.bakiye} TL")
    else:
      print("Geçersiz miktar veya yetersiz bakiye!")

  def para_cek(self, miktar):
    if miktar > 0 and miktar <= self.bakiye:
      self.bakiye -= miktar
      print(f"{miktar} TL para çekildi. Yeni bakiye: {self.bakiye} TL")
    else:
      print("Geçersiz miktar veya yetersiz bakiye!")


kullanici1 = Kullanici("Ahmet", "12345")

girilen_sifre = input("Şifrenizi girin: ")

if kullanici1.sifre_dogrula(girilen_sifre):
  atm = ATM(kullanici1)
  atm.para_yatir(500)
  atm.para_cek(200)
else:
  print("Hatalı şifre!")

işlem_onay = input("Para transferini onaylıyor musunuz? (E/H): ")

if işlem_onay == "E":
  alici_isim = input("Alıcı adını girin: ")

if alici_isim == "Mehmet":
  alici = kullanici1
  miktar = int(input("Transfer edilecek miktarı girin: "))
  if miktar > 0 and miktar <= atm.bakiye:
    atm.bakiye -= miktar
    alici.bakiye += miktar
    print(f"{miktar} TL para transfer edildi. Yeni bakiye: {atm.bakiye} TL")
  else:
    print("Geçersiz miktar veya yetersiz bakiye!")