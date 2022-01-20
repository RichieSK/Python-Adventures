#Merge k arrays
#Unoptimized for readibility and use

def merge_k_arrays(*arrays):
    indices = [0 for x in range(len(arrays))]
    minval = None
    size = sum([len(array) for array in arrays])
    final_array = []
    for index in range(size):
        for k in range(len(arrays)):
            if indices[k] < len(arrays[k]):
                if minval is None:
                    minval = (k, arrays[k][indices[k]])
                else:
                    if arrays[k][indices[k]] < minval[1]:
                        minval = (k, arrays[k][indices[k]])
        final_array.append(minval[1])
        indices[minval[0]] += 1
        minval = None
    return final_array

print(merge_k_arrays([1, 3, 5, 7], [2, 4, 6], [1, 5, 9], [2, 8, 12], [11, 12, 13, 14]))

#TODO
#Update minval to a dictionary and rename for better readibility.
#Rename k in loop to smth meaningful.
