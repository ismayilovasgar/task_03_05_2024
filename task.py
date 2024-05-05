
# *Task - 1
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]
# def myfunc(list):
    # 1_Yol
    # return [ i for i in list if( i > 0 and ( i ** 0.5).is_integer()) ]

    # 2_Yol
    #   result=[]
    #   for i in list:
    #      if i>0 and pow(i,1/2).is_integer():
    #          result.append(i)
    #   return result
# print(myfunc(mylist))



# * Task - 2
# list= [-1,1,2,2,6,7,7,'say']
# def my_func(list):
#   return [ i for i in list if( list.count(i) == 1) ]   
# print(my_func(list))



# *Task - 3
# list=[2,4,6,10]
# def my_func():
#    result = 1
  #  input : 15 -> 1*5=5
#   for i in input("eded daxil edin:"):
#     result*=int(i)

  # input:[2,4,6,10]-> 2*4*6*10 =480
#    for i in list:
#       result *= i

#    return result
# print(my_func())



# * Task - 4
# def my_func():
#   eded=int(input("eded daxil edin:"))
#   return [ i for i in range(1,eded+1) if (eded % i == 0) ]
# print(my_func())



# * Task - 5
# my_list=["yanvar","fevral","mart","aprel","may","iyun","iyul","avqust","sentyabr","oktyabr"]
# def my_func(list):
#     return {x:len(x) for x in list}
# print(my_func(my_list))



# * Task - 6
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# def my_func(list):
# 1 yol
#  return([ i.split(" ")[0].lower() for i in list])

# 2 yol
#  return([ i[:i.find(" ")].lower() for i in list])
# print(my_func(names))



# * Task - 7
# nums1 = [1, 2, 3, 8, 6]
# nums2 = [4, 5, 6, 1, 2]
# def my_func():
#  return [ (nums1[i]+nums2[i])/2 for i in range(len(nums1))]

# print(my_func())
