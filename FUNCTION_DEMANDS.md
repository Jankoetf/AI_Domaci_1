# Function for creation of super matrix: - Universal function  
name: super_matrix_creation__name_of_colaborator_  
inputs:1) Dimensionality of matrix that will be created - n - integer  
output:1) Nympy array with dimensions n*n, with elements from 1 to n**2, in random order without repetition   
example:  
def super_matrix_creation__Yungulovski_(n):  
    ... code ...  
    return super_matrix  
  
# Function that finds one local solution from existing one:  
name: local_search__name_of_colaborator_index  
inputs:1) Matrix than needs local change  
outputs:1) different numpy array matrix with same dimensions as initial and with same restrictions  
comments: #below function definition make comments on uniqueness of function before any code within function  
example:  
def local_search__Yungulovski_1(super_matrix):  
#my function swithes two random elements of initial matrix within the same randomly choosen column  
... code ...  
return new_super_matrix  
  
# Function that finds error funktion for given matrix - Universal function  
name: error_function__name_of_colaborator_  
inputs: 1) Matrix  
outputs: 1) error - real  
example:  
def error_function__Yungulovski_(super_matrix):  
... code ...  
return error  
  
# Function with implemented algorithm: Climbing a Hill  
#this algorithm is often implemented by recursion so we need to memorize current depth and list_of_errors  
name: Climbing_a_hill__name_of_colaborator_index  
inputs:1) max_depth - number  
2) current_depth - number  
3) matrix  
4) number_of_branches_at_every_iteration - number  
5) list_of_errors - list of errors at every iteration   
#break algorithm when you have perfect matrix or at max_depth  
outputs:1) best_matrix_so_far  
2) list_of_errors  
comments: #below function definition make comments on uniqueness of function before any code within function  
example:  
def Climbing_a_hill__Yungulovski_1(max_depth, depth, crazy_matrix, branches, list_of_errors):  
#my function preserves best matrix in every iteration, list_of_errors at the output is monotonous  
... code ...  
return new_super_matrix_so_far, list_of_errors  
  

  
  



    
        
