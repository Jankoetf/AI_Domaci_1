import numpy as np
some_2D_array = np.array([[100, 200, 50, 400], [50, 20, 110, 100], [350, 100, 50, 200]])
some_1D_data = np.array([1,2,3,4,5])
some_3D_data = a = np.array([[[1,2],[4,3]], [[5,10], [14, 2]]])

def info_of_np_array_data(data):
    print("data is:\n", data, "\n")
    print("data.size - number of elements: ", data.size)
    print("a.ndim - number of dimensions: ", data.ndim)
    print("data.shape - shape: ", data.shape)
    print("data.dtype - type: ", data.dtype)
    print("data.strides - strides: ", data.strides)
    #data.T is the same data just looked differently - strides is reversed
    #Strides: strides[0] -> how much bytes we need to jump in the memory to go from first element from one column to first element in the next column, strides[1] -> bytes for one element
    #print("data.flags - flags: ", data.flags)
    
def useful_numpy_commands_on_data(data):
    print("initial array: \n", data)
    print("data.ravel() - make 1D np_array from any np_araray\n", data.ravel())
    
    print("data.copy() - copy\n", data.copy(), type(data.copy()))
    print("data.T - transpose of array\n", data.T, "")
    print("np.sum(data): ", np.sum(data))
    print("np.sum(data, axis = 0):\n", np.sum(data, axis=0))
    print("np.argmax(data) - position of max element\n", np.argmax(data, axis = 0))
    print("np.argmax(data, axis = 0) - position of max element in every row\n", np.argmax(data, axis = 0))
    print("also: np.argmin(data)...")
    print("np.var(data, axis = 1) - variance\n", np.var(data, axis = 1))
    print("np.argsort(data) - indexes of elements in incending order by columns\n", np.argsort(data))
    
    
def numpy_and_memory(data):
    print(data.ravel())
    abytes = data.ravel().view(dtype = np.uint8)[:24]
    print(abytes)
    abytes[1] = 1
    print(abytes)
    print(data.ravel())
    
def numpy_broadcasting():
    a = np.array([[100, 200, 50, 400], [50, 20, 110, 100], [350, 100, 50, 200]])
    print("initial matrix a: \n", a)
    print("a + 1: \n", a + 1)
    print("a + np.array([1, 2, 3, 4]): \n", a + np.array([1,2,3,4]))
    print("a + np.array([[1], [2], [3]): \n", a + np.array([[1], [2], [3]]))
    print("np.all(a), np.any(a): ", np.all(a), np.any(a))
    b = np.array([1,21,3])
    print("initial matrix b: \n",b )
    
    print("b[:, np.newaxis]\n", b[:, np.newaxis], "")
    print("b[np.newaxis,:]\n", b[np.newaxis, :])
    #print(a + b) - error
    print("a + b[:, np.newaxis]\n", a + b[:, np.newaxis])
    

info_of_np_array_data(some_2D_array)
useful_numpy_commands_on_data(some_2D_array)
numpy_broadcasting()

