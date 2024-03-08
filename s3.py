#Given a Python List [10,501,22,37,100,999,87,351] Find out how many numbers are there in the given Python List
# which are Happy numbers?
a = [10,501,22,37,100,999,87,351]
b = []
def is_happy(a):
    for i in range (len(a)):
        sum = a[i]
        while sum!=1 and sum !=4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2   
            sum = tempsum
        if sum == 1:
            b.append(a[i])
    return b
print(is_happy(a))