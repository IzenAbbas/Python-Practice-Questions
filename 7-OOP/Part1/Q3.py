class Computation:
    def __init__(self):
        pass

    def factorial(self, n):
        n = abs(int(n))
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

    def naturalSum(self, n):
        n = abs(int(n))
        return (n * (n + 1)) // 2

    def testPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def testPrims(self, n, m):
        for i in range(2, min(n, m) + 1):
            if n % i == 0 and m % i == 0:
                return False
        return True

    def tableMult(self, n):
        print(f'<<-- Table of "{n}" -->>')
        for i in range(1, 11):
            print(f'{n} x {i}\t= {n * i}')
        print('<<------------------>>\n')

    def allTablesMult(self):
        for i in range(1, 10):
            self.tableMult(i)

    @staticmethod
    def listDiv(n):
        n = abs(int(n))
        Ldiv = []
        for i in range(1, n + 1):
            if n % i == 0:
                Ldiv.append(i)
        return Ldiv

    def listDivPrim(self, n):
        divisors = Computation.listDiv(n)
        prime_divisors = [d for d in divisors if self.testPrime(d)]
        return prime_divisors
    

N = Computation()

print("Factorial of 5:", N.factorial(5))
print("Sum of first 10 natural numbers:", N.naturalSum(10))
print("Is 17 prime?", N.testPrime(17))
print("Are 4 and 9 coprime?", N.testPrims(4, 9))
N.tableMult(3)
N.allTablesMult()
print("Divisors of 12:", Computation.listDiv(12))
print("Prime divisors of 84:", N.listDivPrim(84))

