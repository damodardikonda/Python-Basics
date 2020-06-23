import numpy as np

my_lst=[1,2,3,4,5]

arr=np.array(my_lst)

print(arr)

type(arr)

print(numpy.ndarray)


my_lst1=[1,2,3,4,5]
my_lst2=[2,3,4,5,6]
my_lst3=[9,7,6,8,9]

arr=np.array([my_lst1,my_lst2,my_lst3])
print(arr)

array([[1, 2, 3, 4, 5],
       [2, 3, 4, 5, 6],
       [9, 7, 6, 8, 9]])

print(type(arr))

print(numpy.ndarray)


print(arr.shape)



print(arr)
array([1, 2, 3, 4, 5])
print(arr[3])



print(arr1)

array([[1, 2, 3, 4, 5],
       [2, 3, 4, 5, 6],
       [9, 7, 6, 8, 9]])

print(arr1[1:,:2])

array([[2, 3],
       [9, 7]])
print(arr1[:,3:])

array([[4, 5],
       [5, 6],
       [8, 9]])

print(arr)

array([1, 2, 3, 4, 5])
arr[3:]=100

print(arr)

array([  1,   2,   3, 100, 100])
### Some conditions very useful in Exploratory Data Analysis

val=2

print(arr[arr<3])

array([1, 2])

## Create arrays and reshape

np.arange(0,10).reshape(5,2)

array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])

arr1=np.arange(0,10).reshape(2,5)

arr2=np.arange(0,10).reshape(2,5)

arr1*arr2

array([[ 0,  1,  4,  9, 16],
       [25, 36, 49, 64, 81]])

np.ones((2,5),dtype=int)

array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])

## random distribution
np.random.rand(3,3)

array([[0.80892282, 0.71540909, 0.61908994],
       [0.47289906, 0.81495189, 0.37922198],
       [0.98095096, 0.17323863, 0.6673249 ]])

arr_ex=np.random.randn(4,4)

print(arr_ex)

array([[-0.12422209, -0.23846556,  0.67763672, -0.43058943],
       [ 0.5030507 , -2.00972442, -0.38910531, -0.24660958],
       [ 0.67723849, -0.8381806 ,  1.21662791,  0.06588597],
       [ 0.90490645,  0.54938933,  0.85750544, -0.56762178]])

import seaborn as sns
In [68]:
sns.distplot(pd.DataFrame(arr_ex.reshape(16,1)))

np.random.randint(0,100,8).reshape(4,2)

array([[77, 45],
       [79, 55],
       [40, 35],
       [55, 53]])

np.random.random_sample((1,5))

array([[0.07005997, 0.98540348, 0.98450756, 0.65948775, 0.34944308]])
