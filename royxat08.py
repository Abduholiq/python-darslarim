cars = ["audi", 'mersades benz', 'daevo', 'tesal']
cars.sort() #sort bu funksiya alvbo ketmaketkigi boyicha taxlaydi AGAR Bir element kata xarf bilan yozilsa shu element oldinga chiqadi
# print(cars)

cars = ["audi", 'mersades benz', 'daevo', 'tesal']
cars.sort(reverse=True) #bu metod teskari alifbo ketmaketligida taxlaydi
# print(cars)
 

"""SORTED bu metod asil royxatga tegmagan xolda alfbo ketmaketligi yoki teskari korinishda chiqradi"""
cars.reverse() #bi funksiya royxatni teskari aylantiradi 

# print(len(cars)) #bu funksiya royxat icida qancha element bor yoqligini aniqlaydi

son = list(range(1,10)) #bu funksiya sonlar tuzib beradi 
# print(son)

toq_sonlar = list(range(0,21,2)) #Renge fuksiyasi qorqali qadam boyicha son ciqarish usuli
sanash = list(range(0,100,10))
# print(sanash)
# print(toq_sonlar)

narxlar = [1200, 2000, 4500, 6000, 8600, 3200]
# print(min(narxlar)) #min yani eng kichik sonni aniqlaydi
# print(max(narxlar)) #max bu fuksiya eng katta sonni aniqlaydi
# print(sum(narxlar)) #sum bu fuksiya royxatdagi xamma qoshilgan summalarni natijasini chiiqaradi 


# print(f"eng arzon narx {min(narxlar)}. Eng qimmat narx {max(narxlar)}. Jami narx {sum(narxlar)}.")

# print(cars[0:3]) #royxat ichidagi elementlarni kesib chiqarish

my_cars = cars[:] #royxatdan nusxa olish 
my_cars.append("hyunday")
# print(cars)
# print(my_cars)

#TUPLE Ozgarmas royxat
toys = ('bus', 'car', 'bar', 'dino', 'snake')
toys = list(toys) #royxatga aylantirib uzgarish kritish 
toys.append("tediy")
toys = tuple(toys) #yana uzgarmas royxat qilish


#AMALIYOT
davlatlar = ['kzazkhstan', 'uzbekistan', 'rossiya', 'amerika', 'vetnam', 'malaysia']
# print(len(davlatlar))
# print(davlatlar)
# davlatlar.sort()
davlatlar.sort(reverse=True)
# print(davlatlar)

juft_sonlar = list(range(120,1201,2))
# print(min(juft_sonlar))
# print(max(juft_sonlar))
# print(sum(juft_sonlar))


taomlar = ["manti", 'palov', 'shorva', 'shashlik', 'chuchvara']
nonushta = taomlar[:]
del nonushta[2:5]
# print(nonushta)
# print(taomlar)

nonushta = list(nonushta)
nonushta[0] = "qaymoq va non"
print(nonushta)











