import random
import numpy as np
N = 3


def super_matrix_creation(n):
    sp = np.arange(1, n**2+1)#sp like super matrix, np.array([1,2, ... n**2+1])
    np.random.shuffle(sp)#shuffling
    return np.reshape(sp, (n,n))#reshaping to a 2D matrix
    

s = super_matrix_creation(N)
# print("Original_matrix")
# print(s)

def local_search_random_change(s_matrix):
    s = np.array(s_matrix)
    n = len(s)

    run = True
    while run:
        i1 = np.random.choice(n, 2) #indexes1
        i2 = np.random.choice(n, 2) #2 random samples from range(n) repetition posible
        #print(i1);print(i2) #show indexes 
        if  not all(i1 == i2):
            run = False
            
    s[i1[0]][i1[1]], s[i2[0]][i2[1]] = s[i2[0]][i2[1]], s[i1[0]][i1[1]]
    return s
        

#s_changed_localy = local_search_random_change(s)
# print("changed_matrix"), print(s_changed_localy)
# print("original_matrix_again"), print(s) #testing a function

def error_function(s_matrix):
    s = np.array(s_matrix)

    #super_trans = [[s[j][i] for j in range(len(s))] for i in range(len(s[0]))]
    super_trans = np.transpose(s) #transpose
    super_value = len(s_matrix) * (len(s_matrix)**2 + 1) / 2 
    error_hor, error_ver, error_d1, error_d2 = 0,0,super_value,super_value #initializing errors
    for i in range(len(s_matrix)):
        error_hor += abs(sum(s_matrix[i]) - super_value)#horizontal error
        error_ver += abs(sum(super_trans[i]) - super_value)#vertical error
        for j in range(len(s_matrix)):
            if i == j: #checkig main diagonal and updating error_d1 
                error_d1 -= s_matrix[i][j]
            if i + j == len(s_matrix) - 1: #checking side diagonal and updating error_d2
                error_d2 -= s_matrix[i][j]
            
    error = abs(error_hor) + abs(error_ver) + abs(error_d1) + abs(error_d2) #sum of errors
    return error
    

# error1 = error_function(s)
# print(error1)


##random search, super_matrix, local, error_function
# s = super_matrix_creation(4)
# print("Origin: "); print(s)
# print("Origin error: "); print(error_function(s))
# Max_Depth = 100
# Branches = 50



def Climbing_a_hill(max_depth, depth, crazy_matrix, branches,list_of_errors, preserving_best = True,verbose = True):
    #Climbing_a_hill_basic(Max_depth, current depth - if we start it as 0: 11th iteration will be depth == 10
    #super_crazy_matrix, number of branches at depth, list of errors through the iterations
    #if we dont find better matrix at this depth, do we preserve last best matrix or we continue frow new matrix which is worse,
    #printing stats - analyzing)
    s = np.array(crazy_matrix)
    if depth == 0 and verbose: print("Algoritam started")
        
    if depth == max_depth:
        if verbose:
            print(f"We are at the max depth of {max_depth}, last matrix is:"); print(s)
        return s, list_of_errors
        
    
    else:
        best_error = len(crazy_matrix)**4 if not preserving_best else error_function(crazy_matrix)
        best_matrix = np.zeros((len(s),len(s))) if not preserving_best else crazy_matrix
        for i in range(branches):
            matrix = np.array(local_search_random_change(crazy_matrix))
            if error_function(matrix) == 0:
                if verbose: print(f"We find perfect matrix at depth: {depth}"); print(matrix)
                return matrix, list_of_errors
                
            if error_function(matrix) <= best_error:
                best_error = error_function(matrix)
                best_matrix = matrix
            list_of_errors[depth] = best_error #depth - 1 if start with 1 == depth
  
        if verbose: print(best_error)
        
        return Climbing_a_hill(max_depth, depth + 1, best_matrix, branches,list_of_errors, preserving_best, verbose)
        
        
# errors = np.zeros(Max_Depth)
# RANDOMED0 = Climbing_a_hill_basic(Max_Depth, 0, s, Branches, errors, False)
# print(RANDOMED0[1])
# print(np.count_nonzero(RANDOMED0[1]))


def Random_search(dimension, super_N, verbose = True):#calling a cration of super_matrix Super_N times and choosing best matrix
    best_matrix = np.zeros((dimension, dimension))
    best_error = dimension**4
    for i in range(super_N):
        matrix = super_matrix_creation(dimension)
        error = error_function(matrix)
        if error <= best_error:
            best_error, best_matrix = error, matrix
    if verbose: print(best_error)
        
    return best_matrix, best_error

#Random_search(3, 1000)  
    

def Simulated_annealing(crazy_matrix, start_temperature, cooling, iterations, verbose = True):
    #Simulated_annealing(crazy_matrix, start_temperature, how much we reduce the temperature after
    #for loop, iterations in one for loop, verbose - printing, analysus):
    s = np.array(crazy_matrix)
    best_error, e = len(s)**4, 2.71828
    Temperature = start_temperature
    error_list = []

    while Temperature >= 0:
        for i in range(iterations):
            new_matrix = local_search_random_change(s)
            
            error = error_function(new_matrix)
            if error <= best_error or e**(-error/Temperature) > np.random.rand():
                s = new_matrix
                best_error = error
                #if best_error == 0 ... maybe
                
        
        error_list.append(best_error)
        Temperature -= cooling  
        
    return s, error_list
        
    
s = super_matrix_creation(3)
print("Origin: "); print(s)
print("Origin error: "); print(error_function(s))

# S = Simulated_annealing(s, 30, 0.1, 40)
# print(S)


def Local_Beam_Search_basic(crazy_matrixes, max_depth, depth, branches, num_of_children):#softmax idea for children
    #Local_Beam_Search_basic(crazy_matrix, max_depth, depth, branching - every previous solution gives
    #branches*new_solutions, from all solution at current depth we choose num_of_children best):
        
    if depth == 0:
        s = [np.array(crazy_matrixes)]
    else:
        s = np.array(crazy_matrixes)
    
    
        
    if depth == max_depth:
        return crazy_matrixes
    
    else:
        list_of_matrixes_and_errors = []
        for m in s:
            for i in range(branches):
                #print(m)
                matrix_temp = local_search_random_change(m)
                list_of_matrixes_and_errors.append((error_function(matrix_temp), matrix_temp))
                
        
        #print(list_of_matrixes_and_errors)
        list_of_errors = [m[0] for m in list_of_matrixes_and_errors]
        list_of_matrixes = list(m[1] for m in list_of_matrixes_and_errors)
        #print(list_of_matrixes)
        #print(list_of_errors)
        list_of_errors = sorted(list_of_errors)
        #print(list_of_errors)
        list_of_errors = list_of_errors[0:num_of_children]
        #print(list_of_errors)
        legit_list_of_matrixes = []
        for m in list_of_matrixes_and_errors:
            if m[0] in list_of_errors:
                legit_list_of_matrixes.append(m[1])
        
        return Local_Beam_Search_basic(legit_list_of_matrixes, max_depth, depth+1, branches, num_of_children)
        
        
# a = Local_Beam_Search_basic(s, 20, 0, 50,5)
# print(a)

# for m in a:
#     print(error_function(m))
    
# print(s)


    

