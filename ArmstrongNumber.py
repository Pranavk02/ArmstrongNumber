def digitCount(n):
    counter = 0;
    while n > 0:
        n = n // 10;
        counter = counter + 1;
    return counter

def checkNumber(n):
    temp = n;
    digit = digitCount(n);
    result = 0;

    while temp > 0:
        result = result + pow(temp%10, digit);
        temp = temp // 10;

    if n == result:
        print("Number is Armstrong");
    else:
        print("Number is not Armstrong");

checkNumber(153);