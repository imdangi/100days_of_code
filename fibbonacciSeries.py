#Program to find the fibbonacci series

def getFibboSeries(num):
    num1 =0
    num2=1
    i=0
    while i<num:
        print(num1)
        temp=num1
        num1=num2
        num2=num2+temp
        i+=1


num = int(input("Enter the number of fibonacci series you want : "))
getFibboSeries(num)

#
# def getFibboSeries(num):
#     num1 =0
#     num2=1
#     i=0
#     for i in range(num):
#         print(num1)
#         temp=num1
#         num1=num2
#         num2=num2+temp
#
#
# num = int(input("Enter the number of fibonacci series you want : "))
# getFibboSeries(num)
#
