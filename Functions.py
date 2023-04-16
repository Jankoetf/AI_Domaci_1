import numpy as np
import os

def rnd_square(n):
    temp = np.arange(1,n**2+1).reshape((n,n))
    for i in range(int(os.urandom(1)[0]/25)):
        np.random.shuffle(temp)
    return temp



def target_func(sqr):
    d1, d2, error = 0, 0, 0
    n = sqr.shape[0]
    crit = n*(n**2+1)/2
    for i in range(n):
        error+=abs(sqr[i,:].sum()-crit)
        error+=abs(sqr[:,i].sum()-crit)
        d1+=sqr[i][i]
        d2+=sqr[n-1-i][i]
    error +=abs(d1-crit)
    error +=abs(d2-crit)
    return error

def local_search(sqr):
    n = sqr.shape[0]
    x1,x2,y1,y2 = 0,0,0,0
    while True:
        x1 = int(os.urandom(1)[0]/256*n)
        y1 = int(os.urandom(1)[0]/256*n)
        x2 = int(os.urandom(1)[0]/256*n)
        y2 = int(os.urandom(1)[0]/256*n)
        if (x1,y1) != (x2,y2):
            temp = sqr[x1][y1]
            sqr[x1][y1] = sqr[x2][y2]
            sqr[x2][y2] = temp
            break
    return sqr

#Algorithms

def random_search(Cycles,start_sqr):
    best_sqr = start_sqr
    best_error = target_func(best_sqr)
    temp_error,temp_sqr = best_error,np.copy(best_sqr)
    for i in range(Cycles):
        if best_error == 0:
            break
        temp_sqr = local_search(temp_sqr)
        temp_error = target_func(temp_sqr)
        if temp_error < best_error:
            best_sqr = np.copy(temp_sqr)
            best_error = temp_error
    return best_sqr

def hill_climb(start_sqr):
    n = start_sqr.shape[0]
    cur_sqr = np.copy(start_sqr)
    buffer = []
    neighbours = []
    Tolerance = n
    counter = 0
    while counter < Tolerance:
        if(target_func(cur_sqr)) == 0:
            break
        neighbours = []
        next_level = False
        i = 0
        while i < (n*n):
            flag = False
            temp = local_search(np.copy(cur_sqr))
            for j in range(len(buffer)):
                if np.array_equal(buffer[j], temp):
                    flag = True
                    break
            if flag:
                continue
            buffer.append(np.copy(temp))
            neighbours.append(np.copy(temp))
            i+=1
        for i in range(len(neighbours)):
            if target_func(neighbours[i])<target_func(cur_sqr):
                cur_sqr = np.copy(neighbours[i])
                counter = 0
                next_level = True
                buffer = []
        if not(next_level):
            counter +=1
    return cur_sqr
        

def beam_search(start_sqr):
    n = start_sqr.shape[0]
    best_sqr = np.copy(start_sqr)
    parents = []
    parents.append(np.copy(start_sqr))
    candidates = []
    kids = n
    depth = n*n
    for d in range(depth):
        if target_func(best_sqr) == 0:
            break
        for i in range(len(parents)):
            for j in range(kids):
                temp = np.copy(local_search(parents[i]))
                temp = (temp,target_func(temp))
                flag = False
                for g in range(len(candidates)):
                    if np.array_equal(candidates[g][0], temp[0]):
                        flag = True
                if flag:
                    j-=1
                else:
                    candidates.append(temp)
        for i in range(len(candidates) - kids):
            worst_candidate = (np.copy(candidates[0][0]), candidates[0][1])
            index = 0
            for j in range(len(candidates)):
                if candidates[j][1]>worst_candidate[1]:
                    worst_candidate = (np.copy(candidates[j][0]), candidates[j][1])
                    index = j
            candidates.pop(index)
        parents = []
        best_sqr = np.copy(candidates[0][0])
        for i in range(len(candidates)):
            if candidates[i][1]<target_func(best_sqr):
                best_sqr = np.copy(candidates[i][0])
            parents.append(np.copy(candidates[i][0]))
    return best_sqr
        
        