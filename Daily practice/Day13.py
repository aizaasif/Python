# # Functions

# def cal_sum(a,b):
#     return a+b

# sum=cal_sum(5,4)
# print(sum)
# sum=cal_sum(2,12)
# print(sum)

# # avg of 3 nums
# def cal_avg(a,b,c,d,e):
#     return (a+b+c+d+e)/5
# avg=cal_avg(1,2,3,4,5)
# print(avg)

# def calc_len(list):
#     print(len(list))
# list=["aiza asif"]
# calc_len(list)

# list=["aiza","asif"]
# def func(list):
#     for items in list:
#         print(items)

# func(list)

# # funct to find the factorial
# def calc_fact(n):
#     fac=1
#     for i in range(1,n+1):
#         fac*=i
#     print(fac)

# calc_fact(5)
# calc_fact(3)
# calc_fact(2)

# # fun to convert URD to PKR
# def convertor(urd):
#     pkr=urd*300
#     print(urd,"urd = ",pkr,"pkr")

# convertor(2)

# # func to check even or odd
# def checker(n):
#     if(n%2==0):
#         print("Number is even ")
#     else:
#         print("Number is odd ")

# checker(2)
# checker(3)
# checker(15)
# checker(100)

# # Recursive function
# def func(n):
#     if(n==0):
#         return
#     func(n-1)
#     print(n)
# func(10)

# # recursive function to calculate a factorial
# def calc_fac(n):
#     if(n==1 or n==0):
#         return
#     ans=calc_fac(n-1)*n
#     print(ans)

# # recursive function to calculate the sum of 1st n natural no

# def func(n):
#     if(n==0):
#         return 0
#     return func(n-1)+n
    
# ans=func(5)
# print(ans)

# # print a list using recursive function
# list=[1,2,3,4,5]
# def func(list,index):
#     if(index==len(list)):
#         return
#     print(list[index],end=" ")
#     func(list,index+1)

# (func(list,0))
def func(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return func(n-1)+func(n-2)
ans=func(6)
print(ans)

    






