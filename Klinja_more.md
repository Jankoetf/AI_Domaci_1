Beam_min_graf = []
Beam_mean_graf = []
Gen_min_graf = []
Gen_mean_graf = []
#1) Generisanje resenja:
import numpy as np
def super_matrix_creation__Yungulovsky_(n):
    sp = np.arange(1, n**2+1)#sp like super matrix, np.array([1,2, ... n**2+1])
    np.random.shuffle(sp)#shuffling
    return np.reshape(sp, (n,n))#reshaping to a 2D matrix

#2) Generisanje suseda
def local_search_random_change__Yungulovsky_1(s_matrix):
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

#3) Uporedjivanje svih algoritamma
#Pocetna matrica:
#initial = super_matrix_creation__Yungulovsky_(3)
initial = np.array([[7, 4, 3],[5, 2, 8],[9, 6, 1]])
print(initial)

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


def Random_search(dimension, super_N):#calling a cration of super_matrix Super_N times and choosing best matrix
    best_matrix = np.zeros((dimension, dimension))
    best_error = dimension**4
    for i in range(super_N):
        matrix = super_matrix_creation__Yungulovsky_(dimension)
        error = error_function(matrix)
        if error <= best_error:
            best_error, best_matrix = error, matrix
        
    return best_error

#a) analiza rendoma
def analize_random_search():
    errors = []
    for i in range(100):
        errors.append(Random_search(3, 200))
    
    return np.mean(errors), np.std(errors)
    
#print(analize_random_search())

#b) analiza climbinga
def Climbing_a_hill(max_depth, depth, crazy_matrix, branches,list_of_errors, preserving_best = True,verbose = True):
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
            matrix = np.array(local_search_random_change__Yungulovsky_1(crazy_matrix))
            if error_function(matrix) == 0:
                if verbose: print(f"We find perfect matrix at depth: {depth}"); print(matrix)
                return matrix, list_of_errors
                
            if error_function(matrix) <= best_error:
                best_error = error_function(matrix)
                best_matrix = matrix
            list_of_errors[depth] = best_error #depth - 1 if start with 1 == depth
  
        if verbose: print(best_error)
        
        return Climbing_a_hill(max_depth, depth + 1, best_matrix, branches,list_of_errors, preserving_best, verbose)

def analize_Climbing():
    errors_analize = []
    for i in range(100):
        errors = np.zeros(20)
        randomed = Climbing_a_hill(20, 0, initial, 10, errors, False, False)
        errors_analize.append(randomed[1])
    
    return np.mean(errors_analize), np.std(errors_analize)
        
    
#print(analize_Climbing())


#c) analiza Beama
def Local_Beam_Search_basic(crazy_matrixes, max_depth, depth, branches, num_of_children):#softmax idea for children       
    if depth == 0:
        s = [np.array(crazy_matrixes)]
    else:
        s = np.array(crazy_matrixes)
    
    
        
    if depth == max_depth:
        errors = [error_function(m) for m in crazy_matrixes]
        
        
        return np.min(errors)
        #return crazy_matrixes
    
    else:
        list_of_matrixes_and_errors = []
        for m in s:
            for i in range(branches):
                #print(m)
                matrix_temp = local_search_random_change__Yungulovsky_1(m)
                list_of_matrixes_and_errors.append((error_function(matrix_temp), matrix_temp))
                
        
        #print(list_of_matrixes_and_errors)
        #sorted??????///??/???/???/?/ ne radi 
        list_of_errors = [m[0] for m in list_of_matrixes_and_errors]
        Beam_min_graf.append(np.min(list_of_errors))
        Beam_mean_graf.append(np.mean(list_of_errors))
        
        
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
        
def analize_beam():
    errors = []
    for i in range(100):
        errors.append(Local_Beam_Search_basic(initial, 10, 0, 4,5))
    
    return np.mean(errors), np.std(errors)

#a = Local_Beam_Search_basic(initial, 10, 0, 4,5)
#print(a)
#print(analize_beam())


#d) analize annuealing
def Simulated_annealing(crazy_matrix, start_temperature, cooling, iterations, verbose = True):
    #Simulated_annealing(crazy_matrix, start_temperature, how much we reduce the temperature after
    #for loop, iterations in one for loop, verbose - printing, analysus):
    s = np.array(crazy_matrix)
    best_error, e = len(s)**4, 2.71828
    Temperature = start_temperature
    error_list = []
    p_of_acception = []
    temperature_change = []

    while Temperature >= 0:
        temperature_change.append(Temperature)
        for i in range(iterations):
            new_matrix = local_search_random_change__Yungulovsky_1(s)
            
            error = error_function(new_matrix)
            if i == iterations - 1:
                p_of_acception.append(e**(-error/Temperature))
                
            if error <= best_error or e**(-error/Temperature) > np.random.rand():
                s = new_matrix
                best_error = error
                #if best_error == 0 ... maybe
                
        
        error_list.append(best_error)
        Temperature -= cooling  
        
    return s, error_list, p_of_acception, temperature_change
    #return s, error_list

#S = Simulated_annealing(initial, 5, 0.1, 4)
#print(S)            
def analize_annealing():
    errors = []
    for i in range(100):
        errors.append(np.min(Simulated_annealing(initial, 5, 0.1, 4)[1]))
    
    return np.mean(errors), np.std(errors)
    
#print(analize_annealing())

#e) analize genetic:
def crossover__Yungulovsky_1(parents):
    l = len(parents[0])
    n = len(parents[0])**2
    
    #print(n, "HERERERE")
    p1 = list(np.ravel(parents[0]))
    p2 = list(np.ravel(parents[1]))
    
    cut_after = np.random.choice(range(1, n), 1)[0]
    #cut_after = np.random.choice(range(3, n), 1)[0]
    cut1 = p1[cut_after:]
    cut2 = p2[cut_after:]
    #print(cut_after, cut1, cut2, 'HERERE')
    
    dict_change = dict()
    
    for c1, c2 in zip(cut1, cut2):
       if c1 != c2:
          if (not c1 in dict_change.keys()) and (not c2 in dict_change.keys()):
              #print("not c1 and not c2")
              dict_change[c1] = c2
              dict_change[c2] = c1
              #print(dict_change)
              
          #{1:8, 8:1} + (1,5) => {5:8, 8:5}
          elif (c1 in dict_change.keys()) and (not c2 in dict_change.keys()):
             #print("c1 and not c2")
             temp = dict_change[c1]
             del dict_change[c1]
             dict_change[c2] = temp
             dict_change[temp] = c2
             #print(dict_change)
         
          #{1:8, 8:1} + (5, 1) => {5:8, 8:5}  
          elif (c2 in dict_change.keys()) and (not c1 in dict_change.keys()):
             #print("not c1 and c2")
             temp = dict_change[c2]
             del dict_change[c2]
             dict_change[c1] = temp
             dict_change[temp] = c1
             #print(dict_change)
          
         
          elif (c1 in dict_change.keys()) and (c2 in dict_change.keys()):
             #print("c1 and c2")
             if dict_change[c1] != c2:#{1:8, 8:1, 2:4, 4:2} + (4, 8) => {1:2, 2:1}
                 temp1 = dict_change[c1] #2
                 temp2 = dict_change[c2] #1
                 del dict_change[temp1]
                 del dict_change[temp2]
                 del dict_change[c1]
                 del dict_change[c2]
                 dict_change[temp1] = temp2
                 dict_change[temp2] = temp1
             else:
                 #{1:8, 8:1, 2:4, 4:2} + (8, 1) => {2:4, 4:2}
                 del dict_change[c1]
                 del dict_change[c2]
                 
          #print(dict_change)
             
    for c1, c2, i in zip(cut1, cut2, list(range(len(cut1)))):
        if c1 in dict_change:
            cut1[i] = dict_change[c1]
        if c2 in dict_change:
            cut2[i] = dict_change[c2]
            
    #print(cut1, cut2)
    p1[cut_after:] = cut2
    p2[cut_after:] = cut1

    
    p1 = np.reshape(np.array(p1), (l,l))
    p2 = np.reshape(np.array(p2), (l,l))

    return np.array([p1, p2])

def selection__Yungulovsky_1(parents):
    errors = []
    for p in parents:
        errors.append(error_function(p))
    
    errors = np.array(errors)
    selected = np.argsort(errors)
    selected = selected[:2]
    selected_parents = parents[selected]
    #print(selected_parents)
    return selected_parents
        

#print(selection__Yungulovsky_1(np.array([c,d,M[0], M[1]])))

        
def Mutation__Yungulovsky_1(children):
    probability = 0.02
    child = np.random.choice(2, 1)[0]
    if probability > np.random.rand():
        children[child] = local_search_random_change__Yungulovsky_1(children[child])

def Genetic_algorithm__Yungulovsky_1(depth, parents):
    n = len(parents[0])
    parents = np.array([parents, super_matrix_creation__Yungulovsky_(n)])
    for i in range(depth):
        parents = np.array([parents[0], parents[1], super_matrix_creation__Yungulovsky_(n), super_matrix_creation__Yungulovsky_(3),\
                            super_matrix_creation__Yungulovsky_(3),super_matrix_creation__Yungulovsky_(3),super_matrix_creation__Yungulovsky_(3),\
                            super_matrix_creation__Yungulovsky_(3), super_matrix_creation__Yungulovsky_(3), super_matrix_creation__Yungulovsky_(3)])
        errors = [error_function(p) for p in parents]
        Gen_mean_graf.append(np.mean(errors))
            
        selected_parents = selection__Yungulovsky_1(parents)
        
        #print([error_function__Yungulovsky_(par) for par in parents])
        
        #print("Selected")
        #print(error_function__Yungulovsky_(selected_parents[0]))
        #print(error_function__Yungulovsky_(selected_parents[1]))
        children = crossover__Yungulovsky_1(selected_parents)
        Mutation__Yungulovsky_1(children)
        #print("children")
        #print(error_function__Yungulovsky_(children[0]))
        #print(error_function__Yungulovsky_(children[1]))
        parents = children
        Gen_min_graf.append(min(error_function(parents[0]), error_function(parents[1])))
        #print(parents)
    
    #print(error_function(parents[0]))
    #print(error_function(parents[1]))
    #print(min(error_function(parents[0]), error_function(parents[1])))
    return min(error_function(parents[0]), error_function(parents[1]))
        
    
#print(Genetic_algorithm__Yungulovsky_1(20, initial))

def analize_genetic():
    errors = []
    for i in range(100):
        errors.append(Genetic_algorithm__Yungulovsky_1(20, initial))
    return np.mean(errors), np.std(errors)
    
#print(analize_genetic())


#4) Gramziva pretraga:
#Climbing_a_hill(max_depth, depth, crazy_matrix, branches,list_of_errors, preserving_best = True,verbose = True):
    
# errors = np.zeros(20)    
# randomed = Climbing_a_hill(20, 0, initial, 10, errors, False, False)
# #print(randomed)

# errors = randomed[1]
# means = []
# stds = []
# for i in range(20):
#     means.append(np.mean(errors[:i]))
#     stds.append(np.std(errors[:i]))

import matplotlib.pyplot as plt
# plt.figure()
# plt.plot(errors)
# plt.title("Promena greske sa iteracijama")
# plt.figure()
# plt.plot(means)
# plt.title("Promena srednje vrednosti greske sa iteracijama")
# plt.figure()
# plt.plot(stds)
# plt.title("Promena devijacije greske sa iteracijama")

#5) Kaljenje ali ono simultano
#def Simulated_annealing(crazy_matrix, start_temperature, cooling, iterations, verbose = True):
    
    
# s, errors, p, t = Simulated_annealing(initial, 5, 0.1, 4)
# means = []
# stds = []
# for i in range(50):
#     means.append(np.mean(errors[:i]))
#     stds.append(np.std(errors[:i]))

# plt.figure()
# plt.plot(t)
# plt.title("Promena temperature greske sa iteracijama")
# plt.figure()
# plt.plot(p)
# plt.title("Promena verovatnoce prihvatanja losijeg resenja")

# plt.figure()
# plt.plot(means)
# plt.title("Promena srednje vrednosti greske sa iteracijama")
# plt.figure()
# plt.plot(stds)
# plt.title("Promena devijacije greske sa iteracijama")


#6) pretraga po snopu i genetski
#Local_Beam_Search_basic(initial, 10, 0, 4,5)
# print(Beam_min_graf)
# print(Beam_mean_graf)
# plt.figure()
# plt.plot(Beam_min_graf)
# plt.title("Beam: Promena minimalne greske u populaciji sa iteracijama")
# plt.figure()
# plt.plot(Beam_mean_graf)
# plt.title("Beam: Promena srednje greske u populaciji sa iteracijama")


#)b Genetski
# Genetic_algorithm__Yungulovsky_1(20, initial)
# print(Gen_min_graf)
# print(Gen_mean_graf)
# plt.figure()
# plt.plot(Gen_min_graf)
# plt.title("Gen: Promena minimalne greske u populaciji sa iteracijama")
# plt.figure()
# plt.plot(Gen_mean_graf)
# plt.title("Gen: Promena srednje greske u populaciji sa iteracijama")
