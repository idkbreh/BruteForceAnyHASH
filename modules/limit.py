class Matrix:
    def __init__(self, size, listNumber: list, method: str):
        self.size = size
        self.listNumber = listNumber
        self.method = method
        self.matrix = [self.listNumber[i * size:(i + 1) * size] for i in range(size)]

    def get_matrix_minor(self, matrix, i, j):
        return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

    def calculate_determinant(self, matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant = 0
        for c in range(len(matrix)):
            minor = self.get_matrix_minor(matrix, 0, c)
            determinant += ((-1) ** c) * matrix[0][c] * self.calculate_determinant(minor)

        return determinant

    def Determinant(self):
        if self.method == "recursive":
            return self.calculate_determinant(self.matrix)
        else:
            raise NotImplementedError(f"Method '{self.method}' is not implemented yet.")

