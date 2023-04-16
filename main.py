from Functions import *

n = 5

start = rnd_square(n)
print(start)
print(target_func(start))
print("===========")
t = random_search(100,np.copy(start))
print(t)
print(target_func(t))
print("===========")
t = hill_climb(np.copy(start))
print(t)
print(target_func(t))
print("===========")
t = beam_search(np.copy(start))
print(t)
print(target_func(t))