import numpy as np

def super_matrix_creation__Yungulovsky_(n):
    sp = np.arange(1, n**2+1)#sp like super matrix, np.array([1,2, ... n**2+1])
    np.random.shuffle(sp)#shuffling
    return np.reshape(sp, (n,n))#reshaping to a 2D matrix        

def error_function__Yungulovsky_(s_matrix):
    s = np.array(s_matrix)
    
    super_value = s.shape[0] * (s.shape[0]**2 + 1) / 2
    error_hor = (np.sum(abs(np.sum(s, axis = 1) - super_value)))
    error_ver = (np.sum(abs(np.sum(s, axis = 0) - super_value)))
    error_d1 = abs(np.sum(np.trace(s)) - super_value)
    error_d2 = abs(np.sum(np.trace(np.fliplr(s))) - super_value)

    return error_hor + error_ver + error_d1 + error_d2


