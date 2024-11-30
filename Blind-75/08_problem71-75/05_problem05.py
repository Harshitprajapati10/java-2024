# problem 75

# add two numbers without using + -;
# LC:371

"""
9 + 11

a =         1 0 0 1
b =         1 0 1 1

xor   =     0 0 1 0
a&b<< =   1 0 0 1 0

xor   =   1 0 0 0 0
a&b<< = 0 0 0 1 0 0


xor   =   1 0 1 0 0 --> Ans == 16+4 = 20 ans
a&b<< = 0 0 0 0 0 0

"""


def getSum(a,b):
    while(b != 0):
        tmp = (a & b) << 1
        a = a ^ b
        b = tmp
    return a

print(getSum(9,11))
print(getSum(2,3))

"""
{JAVA}

class Solution{
    public in getSum(int a, int b){
        while(b!=a){
            int temp = (a&b) <<1;
            a = a^b;
            b = tmp;
        }
        return a;
    }
}


"""