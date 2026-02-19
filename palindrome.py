import os

def solvePalindrome(s):

    MOD = 10**9 + 7
    n = len(s)
    total = 0

    def weight(c):
        return ord(c) - ord('a') + 1

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]

            if substring == substring[::-1]:
                for c in substring:
                    total += weight(c)

    return total % MOD

if __name__ == '__main__':

    s = input("Digite a string: ")

    result = solvePalindrome(s)

    print("Resultado:", result)