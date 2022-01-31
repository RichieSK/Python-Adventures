def simulate_trouble_sort(lst):
    #Trouble sort is basically splitting an array into two halves(odd indices
    # and even indices).
    #So, we'll sort those two arrays and then compare adjacent elements.
    
    even = sorted(lst[::2])
    odd = sorted(lst[1::2])
    combined_array = []
    for index in range(len(even)):
        combined_array.append(even[index])
        if index < len(odd):
            combined_array.append(odd[index])
    for index in range(len(combined_array)-1):
        if combined_array[index] > combined_array[index+1]:
            print("The array won't be sorted properly and index {} will be faulty.".format(index)) 
            break
    else:
        print("The array will be sorted")
#     faulty_index = None
#     for index in range(len(odd)):
#         #First we'll compare if the corresponding odd index(say 1) contains a
#         # lesser value than the corresponding even index(say 0).
#         #This compares indices (0,1) (2,3) and so on.
#         #Since the number of elements in the odd array 
#         if odd[index] < even[index]:
#             faulty_index = index*2
#             break
#         #We also have to compare indices (1,2), (3,4) and so on.
#         #So we compare ith index of odd with i+1 index of even.
#         #There is an edge case where the number of elements in both arrays are
#         # equal, where we might go out of bounds in array odd.
#         elif index < len(even)-1 and odd[index] > even[index+1]:
#             faulty_index = index*2+1
#             break
#     if faulty_index is None:
#         print("The array will be sorted")
#     else:
#         print("The array won't be sorted properly and index {} will be faulty.".format(faulty_index)) 

simulate_trouble_sort([2, 1])
simulate_trouble_sort([1, 3, 2])
simulate_trouble_sort([0, 1, 5, 3])
simulate_trouble_sort([1, 7, 6, 2])
