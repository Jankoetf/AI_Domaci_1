# Function for creation of super matrix: - Universal function  
name: super_matrix_creation__name_of_colaborator_  
inputs:1) Dimensionality of matrix that will be created - n - integer  
output:1) Nympy array with dimensions n*n, with elements from 1 to n**2, in random order without repetition   
example:  
def super_matrix_creation__Yungulovski_(n):  
    ...  
    return super_matrix  
  
# Function that finds one local solution from existing one:  
name: local_search__name_of_colaborator_index  
inputs:1) Matrix than needs local change  
outputs:1) different numpy array matrix with same dimensions as initial and with same restrictions  
comments: #below function definition make comments on uniqueness of function before any code within function  
example:  
def local_search__Yungulovski_1(super_matrix):  
#my function swithes two random elements of initial matrix within the same randomly choosen column  
...  
return new_super_matrix  
  
# Function that finds error funktion for given matrix - Universal function  
name: error_function__name_of_colaborator_  
inputs: 1) Matrix  
outputs: 1) error - real  
example:  
def error_function__Yungulovski_(super_matrix):  
...  
return error  
  
# Function with implemented algorithm: Climbing a Hill  
name: Climbing_a_hill__name_of_colaborator_index  
inputs:1) Matrix
*2) LOl  
outputs:1) different numpy array matrix with same dimensions as initial and with same restrictions  
comments: #below function definition make comments on uniqueness of function before any code within function  
example:  
def Climbing_a_hill__Yungulovski_1(super_matrix):  
#my function swithes two random elements of initial matrix within the same randomly choosen column  
...  
return new_super_matrix  
  
#  
  
  



    
        
