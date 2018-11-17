def add_matrices(mat1, mat2):
    linijka = []
    mat3 = []
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Różna ilość wierszy")
    for row_i in range(len(mat1)):
        for row_j in range(len(mat1[0])):
            linijka.append(mat1[row_i][row_j] + mat2[row_i][row_j])
        mat3.append(linijka)
        linijka = []
    return mat3

def sub_matrices(mat1, mat2):
    linijka = []
    mat3 = []
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Różna ilość wierszy")
    for row_i in range(len(mat1)):
        for row_j in range(len(mat1[0])):
            linijka.append(mat1[row_i][row_j] - mat2[row_i][row_j])
        mat3.append(linijka)
        linijka = []
    return mat3
