#!/usr/bin/env python3

# Input array=[1,1,1,2,2,3], k=2
# Output=[1,2]

# Find the k most frequent elements
def k_most_element(input_array, k):
    base_dict=dict()
    final_set=set()
    for i in input_array:
        if i in base_dict:
            base_dict[i] += 1
            if base_dict[i] >= k:
                final_set.add(i)
        else:
            base_dict[i] = 1
    return list(final_set)


print(k_most_element([1,1,1,2,2,3], 2))
