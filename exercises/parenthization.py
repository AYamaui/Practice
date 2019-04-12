

def parenthization_matrix_multiplication(matrices):


    for i in range(len(matrices) -1):
        matrices = matrices[:i] + multiplication(matrices[i], matrices[i+1])

        if i + 1 < len(matrices):
            matrices += matrices[i+2:]
    min(parenthization_matrix_multiplication(matrices[i]))