# O(nm) time | O(nm) space
def min_distance(str1, str2):
    edits = [[x for x in range(len(str1)+ 1)] for y in range(len(str2)+ 1)] # initialize the edit array 2D
    for i in range(1, len(str2)+ 1):
        edits[i][0] = edits[i - 1][0] + 1
    for i in range(1, len(str1) + 1):
        if str2[ i - 1] == str1[ j - 1]:
            edits[i][j] = edits[i -1][j-1]
        else:
            edits[i][j] = 1 + min(edits[i - 1][j -1],edits[j-1][i], edits[i -1][j])
    return edits[-1][-1]

# O(nm) time | O(min(n,m))
def min_distance(str1, str2):
    
