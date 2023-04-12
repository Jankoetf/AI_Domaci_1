import numpy as np


def numpy_matrix_legit_shit():
    a1D = np.array([1,2,3])
    b1D = np.array([0,5,10])
    a2D = np.array([[2,5,1], [0,1,4], [0, 0, 10]])
    b2D = np.array([[3,3, 3], [3,3,3], [3,3,3]])
    print("a1D initial: \n", a1D, "\nb1D initial: \n", b1D, "\na2D initial: \n", a2D,"\nb2D initial: \n", b2D)
    
    print("matrix legit operations:")
    print("a1D@b1D - legit matrix myltiplication:\n ", a1D@b1D, "")
    print("a1D*b1D - skalar multiplication:\n", a1D*b1D, "")
    print("np.vdot(a1D, b1D) - dot product: ", np.vdot(a1D, b1D))
    print("a2D@b2D - legit matrix myltiplication: \n", a2D@b2D, "")
    print("a2D*b2D - scalar multiplication: \n", a2D*b2D, "")
    print("np.vdot(a2D, b2D) - dot product: ", np.vdot(a2D, b2D), "")
    print("a2D.T:\n", a2D.T, "\n")
    
    print("matrix useful methods")
    print("np.diag(a1D) - returns diagonal matrix:\n",np.diag(a1D))
    print("np.diag(a2D) - returns diagonal of 2D matrix: \n", np.diag(a2D))
    print("np.trace(a2D)-returns a sum of main diagonal: ", np.trace(a2D))
    print("np.fliplr(a2D) - Reverse the order of elements along axis 1 (left/right)\n", np.fliplr(a2D))
    print("np.fliplr(a2D)*np.diag(np.ones(a.shape[0]) - showing side diagonal:\n", np.fliplr(np.fliplr(a2D)*np.diag(np.ones(a2D.shape[0]))))
    print("np.diag(np.fliplr(a2D)) - getting side diagonal", np.diag(np.fliplr(a2D)))
    
numpy_matrix_legit_shit()
