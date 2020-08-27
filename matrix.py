class Matrix:
    inf = 99999

    def __init__(self, ssize):
        self.size = ssize
        self.matrix = [[self.inf for x in range(ssize)] for x in range(ssize)]
        for i in range(self.size):
            self.matrix[i][i] = 0

    def __getitem__(self, i):
        return self.matrix[i]

    def floyd(self):
        """Adding vertices individually"""
        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    if (self.matrix[i][k] != self.inf and self.matrix[k][j] != self.inf):
                        self.matrix[i][j] = min(self.matrix[i][k] + self.matrix[k][j], self.matrix[i][j])