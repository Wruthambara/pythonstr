def find_removal_indices(str1, str2):
    if len(str1) != len(str2) + 1:
        return [-1]
    
    # Find the length of the common prefix
    p = 0
    while p < len(str2) and str1[p] == str2[p]:
        p += 1
    
    # Check if the suffix matches
    if str1[p : len(str1)-1] == str2[p:]:
        return list(range(p, len(str1)))
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