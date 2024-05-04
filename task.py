# tasks for define function 
#! 1.) 
 #verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında
# yazıb və listin içərisində ekrana çıxarın. 
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]
#*  2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:
#  input:[-1,1,2,2,6,7,7,'say']
#* 3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın
#* 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın
#! 5)
# Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın 
# və bunu comprehension ilə edin və alınan listi print etdirin.
# mənim listim
# mylist=['may','iyun','iyul']
# bu şəkildə olacaq
# {'may': 3, 'iyun': 4, 'iyul': 4}
#* 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#  verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin
#  (əlavə olaraq funksiya da  istifadə edəbilərsiz).
# ['rick', 'morty', 'summer', 'jerry', 'beth']
#* 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# results=[ 2.5, 3.5, 4.5] 

# ! Task - 1
mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]

def myfunc():
     result=[i  for i in mylist if i % ]
     return result
    # for i in mylist:
    #   if type(pow(i,0.5)) == int: 
    #       result.append(i)
    #   else: 
    #      continue
print(myfunc())


# ! Task - 2
# list= [-1,1,2,2,6,7,7,'say']
# def my_func(list):
#   return [ i for i in list if list.count(i) == 1]           
# print(my_func(list))


# Task - 3
# def my_func():
#   result=1
#   for i in input("eded daxil edin:"):
#     result*=int(i)
#   return result
# print(my_func())


# * Task - 4

# def my_func():
#   eded=int(input("eded daxil edin:"))
#   return [i for i in range(1,eded+1) if eded % i == 0]
# print(f"{my_func()}")


# ! Task - 5


# * Task - 6
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# print([ i.split(" ")[0].lower() for i in names])
 #['rick', 'morty', 'summer', 'jerry', 'beth']

# * Task - 7
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# print([ (nums1[i]+nums2[i])/2 for i in range(len(nums1))])
