import numpy as hehe
# print(hehe.__version__)
# my_list=[1,2,3,4,5]
# my_list=my_list*2
# print(my_list)

# array=hehe.array([1,2,3])
# print(array)
# print(type(array))
# print(array*2)
# print(array+array)
# print (array*array)
# print(array**2)
# print(hehe.sqrt(array)) 

# print(hehe.shape(array))
# array=hehe.array([[[1,2,3,4],[13,12,23,34],[51,82,83,94]],
#                    [ [5,6,7,8],[31,42,53,24],[71,82,39,74]],
#                    [[9,10,11,12],[14,25,36,49],[11,22,33,44]]])
# print (array.ndim)
# print(array.shape)
# print(array.size)
# print(array.dtype)
# print(array[0][0][0])
# print(array[2,2,3])

# array=hehe.array([[1,2,3,4],
#                  [5,6,7,8],
#                  [9,10,11,12],
#                  [13,14,15,16]])
# print(array[-2])
# print(array[1:3])

# start:end:step
# print(array[0:4:3]) 
# print(array[::-2])
# print(array[0:4:1,3])
# print(array[0:4:1,3:4])
# print(array[0:3:1,0:2:1])
# print(array[:2,:2])
# print(array[1:3, 1:3])
# print(array[1:3:1,1:3:1])

# print(hehe.pi)

# vectorized math functions

# radii= hehe.array([1, 2, 3])
# area= hehe.pi * radii ** 2
# print(area)

#  elementwise operations

# array1= hehe.array([1,2,3])
# array2= hehe.array([4,5,6])
# print(array1+array2)
# print(array1-array2)
# print(array1*array2)
# print(array1/array2)

# comparision operators

# marks=hehe.array([50,60,70,80,90])
# print(marks > 60)
# print(marks < 80)
# print(marks == 70)
# marks[marks<60]=0
# print(marks)

# Broadcasting in numpy 
# it allows numpy to prepare operations on array
# with different shapes by virtually expanding dimensions
# so they matches the larger array's shape
# basically it allows numpy to perform opeations on arrays of different shapes
# array1=hehe.array([11,12,13])
# array2=hehe.array([[1,2,3],
#                    [4,5,6],
#                    [7,8,9]])
# print(array1.shape)
# print(array2.shape)
# print(array1+array2)
# print(array1*array2)


# Aggregate Functions= summarize data and typically returns a 
#                        single value
# array=hehe.array([[1,2,3,4],
#                   [5,6,7,8,]])
# print(hehe.sum(array))
# print(hehe.mean(array))
# print(hehe.std(array))
# print(hehe.var(array))
# print(hehe.sum(array,axis=0))
# print(hehe.sum(array,axis=1))
# print(hehe.min(array))
# print(hehe.max(array))
# print(hehe.argmin(array))
# print(hehe.argmax(array))

# FILTERING= Refers to the process of selecting elements from an array
#         that match a given condition

# ages=hehe.array([[15,18,19,21,28,55,90],
#                  [32,45,19,20,38,35,69]])
# teenagers=ages[ages<20]
# adults=ages[(ages>=20)&(ages<60)]
# seniors=ages[ages>=60]
# print(teenagers)
# print(adults)
# print(seniors)

# adults=hehe.where((ages>=20)&(ages<60),ages,0)
# print(adults)

# RANDOM NUMBERS
# (low,high,size)
# rndm=hehe.random.default_rng(seed=2)
# print(rndm.integers(1,6))
# print(rndm.integers(1,6,(3,2)))

# hehe.random.seed(3)
# print(hehe.random.uniform(1,9,(3,3)))

# rndm=hehe.random.default_rng()
# array=hehe.array([1,2,3,4,5])
# rndm.shuffle(array)
# print(array)

# rndm=hehe.random.default_rng()
# Royalenfield=hehe.array(["Classic 350","Meteor 350","Hunter 350","GT 650"])
# choice=rndm.choice(Royalenfield,(3,3))
# print(choice)








