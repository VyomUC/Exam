import numpy as np

def reduce_rows(cost_matrix):

    #Subtract the minimum value from each row of the cost matrix.
    row_minima = np.min(cost_matrix, axis=1)
    cost_matrix -= row_minima[:, np.newaxis]
    return cost_matrix

def reduce_columns(cost_matrix):

    #Subtract the minimum value from each column of the cost matrix.
    col_minima = np.min(cost_matrix, axis=0)
    cost_matrix -= col_minima
    return cost_matrix

def hungarian_method_reduction(cost_matrix):

    #Perform row and column reduction as part of the Hungarian Method.
    print("Original Cost Matrix:\n", cost_matrix)
    
    # Row Reduction
    cost_matrix = reduce_rows(cost_matrix)
    print("After Row Reduction:\n", cost_matrix)
    
    # Column Reduction
    cost_matrix = reduce_columns(cost_matrix)
    print("After Column Reduction:\n", cost_matrix)
    
    return cost_matrix

cost_matrix = np.array([[82, 83, 69, 92],
                        [77, 37, 49, 92],
                        [11, 69,  5, 86],
                        [ 8,  9, 98, 23]])

reduced_matrix = hungarian_method_reduction(cost_matrix)
