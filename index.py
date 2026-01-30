# 1 - masala
son1 = int(input('birinchi sonni kiriting: '))
son2 = int(input('ikkinchi sonni kiriting: '))
if son2 < son1:
  print(son1 * son2)
else:
  print(son1  + son2)
# 2 - masala
talaba_bahosi = int(input('Talaba bahosini kiriting: '))
if talaba_bahosi >= 85:
  print("A;lochilik")
elif talaba_bahosi >= 70:
  print('Yahshi')
else:
  print('Yetarli emas')
# 3 - masala
mahsulot_narxi = int(input('Mahsulot narxini kiriting: '))
mijoz_yosh = int(input('Mijoz yoshini kiriting: '))
if mijoz_yosh >= 60:
  summa = mahsulot_narxi * 0.8
  print(summa)
else:
  print(mahsulot_narxi)

# 4 - masala
number1 = float(input('birinchi sonni kiriting: '))
number2 = float(input('ikkinchi sonni kiriting: '))
if number1 %2 == 0 and number2 % 2 == 0:
  print(number1 ** 2 + number2 ** 2)
else:
  print(number1**3 - number2**3)

# 5 - masala
harorat = int(input('Harorat ni kiriting: '))
if harorat > 30:
  frengeyt = (harorat * 1.8) + 32
  print('Issiq kun', frengeyt)
else:
  print('Normal kun')

# 6 - masala
son1 = int(input('birinchi sonni kiriting: '))
son2 = int(input('ikkinchi sonni kiriting: '))
son3 = int(input('uchunchi sonni kiriting: '))
if son1 > 0 and son2 > 0 and son3 > 0:
  ortacha = (son1 + son2 + son3) / 3
  print(ortacha)
else:
  print(max(son1, son2, son3))

# 7 - masala
xodimning_ish_staj = int(input('Xodimning ish stajini kiriting: '))
oylik_moash = int(input('oylik moashini kiriting: '))
if xodimning_ish_staj > 5:
  ustama = oylik_moash / 0.15
  yangi_moash = oylik_moash + ustama
  print(yangi_moash)
else:
  aa =  oylik_moash * 0.08
  print(oylik_moash + aa)

# 8 - masala
turtburchak_uzunligi = int(input('To\'rtburchak uzunligini kiriting: '))
turtburchak_kengligi = int(input('To\'rtburchak kengligini kiriting: '))

if turtburchak_uzunligi == turtburchak_kengligi:
    yuza = turtburchak_uzunligi * turtburchak_kengligi
    print(f"Bu kvadrat. Yuzasi: {yuza}")
else:
    yuza = turtburchak_uzunligi * turtburchak_kengligi
    perimetr = 2 * (turtburchak_uzunligi + turtburchak_kengligi)
    print(f"To'rtburchak yuzasi: {yuza}, Perimetri: {perimetr}")
