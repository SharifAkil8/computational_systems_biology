import numpy as np

def find_min_distance(matrix):
    """Find the minimum distance in the matrix."""
    min_val = float('inf')
    x, y = -1, -1
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                x, y = i, j
    return x, y, min_val

def update_distance_matrix(matrix, x, y):
    """Update the distance matrix after merging clusters x and y."""
    new_row = []
    for i in range(len(matrix)):
        if i == x or i == y:
            continue
        new_dist = (matrix[x][i] + matrix[y][i]) / 2  # Average linkage
        new_row.append(new_dist)
    
    # Remove the old rows and columns
    matrix = np.delete(matrix, (y, x), axis=0)
    matrix = np.delete(matrix, (y, x), axis=1)
    
    # Add the new row and column
    matrix = np.vstack((matrix, new_row))
    new_col = np.append(new_row, [0.])
    matrix = np.column_stack((matrix, new_col))
    
    return matrix

def upgma(distance_matrix, labels):
    """Perform UPGMA clustering."""
    while len(distance_matrix) > 1:
        x, y, min_dist = find_min_distance(distance_matrix)
        print(f"Merging {labels[x]} and {labels[y]} with distance {min_dist}")
        
        # Update the labels
        new_label = f"({labels[x]}, {labels[y]})"
        del labels[y], labels[x]  # Remove old labels
        labels.append(new_label)  # Add the new label
        
        # Update the distance matrix
        distance_matrix = update_distance_matrix(distance_matrix, x, y)
        
    print("Final clustering:", labels[0])

# # Example usage
# distance_matrix = np.array([
#     [0, 17, 21, 31, 23],
#     [17, 0, 30, 34, 21],
#     [21, 30, 0, 28, 39],
#     [31, 34, 28, 0, 43],
#     [23, 21, 39, 43, 0]
# ])
# labels = ["1", "2", "3", "4", "5"]

distance_matrix = np.array([
    [0, 5, 9, 9, 8, 7],
    [5, 0, 10, 10, 9, 8],
    [9, 10, 0, 4, 3, 8],
    [9, 10, 4, 0, 3, 8],
    [8, 9, 3, 3, 0, 7],
    [7, 8, 8, 8, 7, 0]
])
labels = ["1", "2", "3", "4", "5", "6"]

upgma(distance_matrix, labels)