import random
# help(random)
# print(dir(random))
# print(random.__doc__)
print(random.random()) #rnadom float value dae 1 er nise. doibo choyon bole eta
print(random.uniform(5,10)) #5 theke 10 er moddhe float dae
print(random.randint(1 ,100))# 1 to 100 int value
print(random.randrange(1,100,5))

fruits = ['apple', 'banana', 'cherry']
print(random.choice(fruits))

random.shuffle(fruits)
print(fruits)

def generate_pin():
    return random.randint(1000, 9999)
print(f"Your 4 digit pin {generate_pin()}")