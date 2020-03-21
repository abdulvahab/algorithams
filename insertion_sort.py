#!/usr/bin/python
'''
This module use insertion sort algoritham to sort out a list in ascending order
'''

#unsorted_list = [5,2,4,6,1,10,4,22,3,23,54,65,76,21,23]
#unsorted_list = [6,1,2,3,4,5]
#sorted_list = [unsorted_list.pop()]
#print(sorted_list)
def sort_list(unsorted_list):
    sorted_list = [unsorted_list.pop()]
    while unsorted_list:
        key = unsorted_list.pop()
        i=0
        #print(i, key)
        sorted_length = len(sorted_list)
        for j in range(sorted_length):
            if key < sorted_list[j]:
                #print(j, key)
                sorted_list.insert(j,key)
                #print(unsorted_list)
                #print(sorted_list)
                break
            else:
                i += 1
                #print(i)
                #print(j,key)
                if i == sorted_length:
                    sorted_list.append(key)
                #print(unsorted_list)
                #print(sorted_list) 
                continue
                # print(j+1, key)
                # sorted_list.insert(j+1,key)
    return sorted_list

def find_value_index(array,value):
    for i, li in enumerate(array):
        print(i,li)
        if li == value:
            return i
        else:
            print(len(array))
            print(i,li)
            if i == len(array)-i:  
                return None
            continue


if __name__=="__main__":
    unsorted_list = [5,2,4,6,1,10,4,22,3,23,54,65,76,21,23]
    print("Unsorted List: ", unsorted_list)
    sorted_list = sort_list(unsorted_list)
    print("Sorted List: ", sorted_list)      

    #find a value in a list
    unsorted_list = [5,2,4,6,1,10,4,22,3,23,54,65,76,21,23]
    value_index = find_value_index(unsorted_list, 6)
    print(value_index)

#print(unsorted_list)
#print(sorted_list)




# if key < sorted_list[j]:

# if unsorted_list[i]>

# sorted_list.append(li)

# if unsorted_list[i] < li:

# key = unsorted_list[i]
# if key > li:
#     sorted_list.append(li)


