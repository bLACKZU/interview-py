import math

string1 = ""
string2 = ""
product1 = 1
product2 = 1
def prime_check(n):
    for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:
            return False
    return True

def nxt_prime(n):
    candidate = n + 1
    while not prime_check(candidate):
        candidate += 1
    return candidate

mapping = {'a': 2}
first = 2
for i in range(ord('b'), ord('z') + 1):
    mapping[chr(i)] = nxt_prime(first)
    first = mapping[chr(i)]

print(mapping)
for char1 in string1:
    product1 *= mapping[char1]
print(product1)
for char2 in string2:
    product2 *= mapping[char2]
print(product2)

if product1 == product2:
    print("Anagrams")
else:
    print("Not Anagrams")
    

