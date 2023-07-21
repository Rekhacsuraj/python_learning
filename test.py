# subjects=['english','hindi','maths','science']
# print(subjects[0:4])
# subjects.append('evs')
# print(subjects)
# print(subjects[0])
# print(subjects[1])
# print(subjects[3])
# print(subjects[2:5])
# print(len(subjects))
# print(subjects[0:3])

# person = {'name':'qazi',
#         'shirt':'black',
#         'laptop':'apple'
#         }
# print(person['laptop'])

# plants = ["zzplant","pothos","jasmine","draceana","rose"]
# print (len(plants))
# plants.append("oleander")
# print(plants)
# print(len(plants))

# def introducer():
# person = { 'name': 'rekha',
        #   'age': '35',
        #   'job': 'home maker'
        #   }
#  print (f'hi, i am {person["name"]}. \ni am {person["age"]} years old.\ni am a {person["job"]}')
# introducer()
# print(person.values())      
# print(person.keys())     

# def sum(a,b):
#  return a+b

# sum1= lambda a,b:(a+b)
# print(sum(6,9))

# list1=[1,2,3,4]
# list2=[1,4,5,3]
# sum=set( list1+list2)

# print(sum)
# print (4 in sum)
# print( 1 in sum)
# print(8 in sum)


# def unique(fruits):
#  return set(fruits)

# print(unique(['apple','orange','apple','banana','pear','banana']))


# def unique(marks):
#  return set(marks)

# print(unique([50,45,48,50,50,43]))

# def unique(plants): 
#         return list(set(plants))

# # unique=lambda plants:(['pothos','zz plant','draceana','draceana','pothos','adenium','petunia','draceana'])
# print(unique(['pothos','zz plant','draceana','draceana','pothos','adenium','petunia','draceana']))


# plants= ['pothos','zz plant','adenium','petunia','draceana']
# print(len(plants))
# for plant in (plants):
#  print('plant:',plants)


# marks =[50,45,48,50,50,43]
# for mark in marks:
#         print(mark)
# enumerate(marks)

# for number in range (5):
#         print(number)
             
# for _ in range (7):
#         print("hi")


# fruits=['apple',' pear','banana','orange']
# for _ in range(10):
        
#  fruits.append('orange')
#  print(fruits)
             

# counter=0
# while counter<100:
#         print(counter)
        
#         counter=counter+1
        
# counter=0
# while counter<5:
#         print([counter])
#         counter=counter+1
        
# def double(numbers):
#         result = []
#         for number in numbers:
#                 result.append(number*2)
#         return result
# print(double([2,3,4]))

# def square(numbers):
#         result = []
#         for number in numbers:
#                 result.append(number*number)
#         return result
# print(square([2,3,4,5]))



# def count_words(phrase): return len(phrase.split())
# print(count_words('hello dear friends'))
      
      
# def countby_5(numbers):
#         result=[]
#         for number in numbers:
#                 result.append(number+5)
#         return result
# print(countby_5([5,10,15]))


# def double(numbers):
#         result=[]
#         for number in numbers:
#                 result.append(number+number)
#         return result
# # print (double([1,2,3,4,5]))

# def countwords(phrase:str)->

 
# def find_max(numbers):
#          currentmax=numbers[0]
#          for number in numbers:
#                  if number>currentmax:
#                          currentmax=number
#          return currentmax
# print(find_max([3,8,2,9,5]))


# print(list(map(lambda num: num*4, [2,3,4])))

# numbers=[1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda number: number%2==0, numbers)))


# numbers=[1,2,3,4,5,6,7,8,9]
# print([number*2 for number in numbers])
# print([number for number in numbers if number%2==0])
# print([number**3 for number in numbers if number%2!=0])


# # 
# def doublenumber(number):
#         return number*2
# print(list(map(doublenumber,[2,3,4])))


# print(list(map(lambda num:num+2,[2,3,4]))


# l=[]
# for i in range(1,100):
#         if (i%2==0) & (i%3==0):
#                 l.append(str(i))
# print(l)

# numbers=range(1,100)
# print(list(number for number in numbers if (number%2==0 )))
# x = 0
# a = 6
# b = 6
# if a > 0:
#     if b < 0: 
#         x = x + 6 
#     elif a > 6:
#         x = x + 5
#     else:
#         x = x + 4
# else:
#     x = x + 3

# print(x)

# i = 5
# while True:
#     if i%0o11 == 0:
#         break
#     print(i)
#     i += 1
#     matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

# matrix2 = []

# for submatrix in matrix:
#   for val in submatrix:
#     matrix2.append(val)

# print(matrix2[2][2])

# def get_odd_fundef my_function():
# def my_inner_function():
#     x = 20
# print(x)
# my_inner_function()

# my_function()
# numbers = [1, 2, 3, 4, 5]
# print(numbers[4:])

# matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# matrix2 = []

# for submatrix in matrix:
#   for val in submatrix:
#     matrix2.append(val)

# print(matrix2[2])

# print(2 * 3 ** 3 * 4)
# matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
# print(matrix[0][0][0])

# def my_fu
# Num = input("Enter a Number: ") 
# print (Num * 3 )

# list1 = [10, 11, 12, 13, 14]
# print(list1[::1])


# def myfunc():
#   a = 20
#   print(a)

# myfunc()

# def sum(a,b):
#   return a+b
# print(sum(2,3))

# for x in [0, 2, 1, 3]:
#     for y in [0, 4, 1, 2]:
#             print('*')
            
# def my_function(arg1, *argv): 
#     print ("First argument:", arg1) 
#     for arg in argv: 
#         print("Next argument:", arg) 

# my_function('Welcome', 'to', 'Python!')

# x = 1
# while ( x <= 5 ):
#   x += 1
# print(x)

list1=[4,4,3,2]
list1.pop(2)
print(list1)
