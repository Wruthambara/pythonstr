def find_removal_indices(str1, str2):
    if len(str1) != len(str2) + 1:
        return [-1]
    
    indices = []
    for i in range(len(str1)):
        # Create a new string by removing the character at index i
        new_str = str1[:i] + str1[i+1:]
        if new_str == str2:
            indices.append(i)
    
    if indices:
        return sorted(indices)
    else:
        return [-1]

# Read input from stdin
import sys
data = sys.stdin.read().split()
str1 = data[0]
str2 = data[1]

# Get the result
result = find_removal_indices(str1, str2)

# Print the output
if result == [-1]:
    print(-1)
else:
    for idx in result:
        print(idx)