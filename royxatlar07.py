mevalar = ['anjir', "o'rik", "shaftoli", "tarvuz"]
narxlar = [1200, 1000, 4000, 5200, 8600, -500, 2.5]
sonlar = ["bir", "ikki", "uch", 4, 5, 6]
ismlar = []
# print(mevalar[0]) #indeks orqali royxat icidagi elementlarni chiqarish
# print(mevalar[2])
# print(mevalar[3])
# print(mevalar[-1]) #eng oxirgi elementga minus orqali murojat qilish
# print(mevalar[1].upper())
# print(mevalar[2].title())

mevalar[0] = "anor"

mevalar.append("tarvuz") #append metodi ro'uxatga matin yoki son qoshishda ishlatiladi
mevalar.append("orik")
mevalar.insert(0, 'qovun') #insert metodi boshiga oxiriga ortasiga matin qoshishda ishlatiladi
mevalar.insert(3, 'ananas')

cars = []
cars.append('Lasetti')
cars.append('Trecker')
cars.append('Nexia')
cars.append('Malibu')

del cars[0] #royxat icidan indekas orqali elementlarni ochirish
cars.remove("Malibu") #royxt ucidan nomi orqali elemnt ochirish

xayvonlar = ['mushuk', 'qoy', 'it', 'sigir', 'mushuk']
xayvonlar.remove('mushuk') 

bozorlik = ['un', 'yog', 'banan', 'choy']
maxsulot = bozorlik.pop(0) #pop metodi royxatdan birir bir elementni sugrib oladi 
# print('Men bozordan ' +  maxsulot + ' sotib oldim')


#Amaliyot
# ismlar = ['umid', 'abdullo', 'sherzod']
# print("Salom ", ismlar[1].title(), "chomilgani boramizmi")
# print('Qalaysan ', ismlar[0].title(), 'bugun choyxona bormi')
# print("Men uyga ketdim ", ismlar[2].title())

# sonlar = [10, 5.5, -56, 95]
# print(sonlar[0]+sonlar[3])
# print(sonlar[2]-sonlar[1])
# print(sonlar[0]/sonlar[3])

t_shaxslar = ["alisher navoiy", "imom buxoriy", ]
z_shaxslar = ['islon musk', 'bill gatse']
shaxs_1 = t_shaxslar.pop(0).title()
shaxs_2 = z_shaxslar.pop(0).title()
# print(f"Men tarixiy saxslardan {shaxs_1} bilan,"
#       f"zamonaviy shaxslardan {shaxs_2} bilan"
#       f"suxbat qilgim keladi")

friend = []
friend.append("Sherzod")
friend.append("Umid")
friend.append("Abdullo")
friend.append("Baxrom")
friend.append("Rozimurod")
# print(friend)
friend.remove("Baxrom")
friend.remove("Rozimurod")
# print(friend)
friend.insert(0, "Javoxir")
friend.insert(4, "Abror")
# print(friend)

mexmonlar = []
dost_1 = friend.pop(0)
dost_2 = friend.pop(1)
dost_3 = friend.pop(2)
mexmonlar.append(dost_1)
mexmonlar.append(dost_2)
mexmonlar.append(dost_3) 
# print(mexmonlar)






