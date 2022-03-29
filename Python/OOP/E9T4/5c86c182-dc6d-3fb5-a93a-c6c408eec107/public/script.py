class Matrix:

    def __init__(self, matrix):
        assert matrix != [], 'list is an empty list'
        assert isinstance(matrix, list), 'It is not a nested list'
        for r in matrix:
            assert isinstance(r, list), 'It is not a nested list'
            assert r != [], 'It is an empty sublist'
            assert len(r) == len(matrix[0]), 'The matrix not rectangular'
            for num in r:
                assert isinstance(num, (int, float)), 'invalid type in sublist'
        self.__matrix = matrix

    def __add__(self, other):
        assert isinstance(other, Matrix), 'It is not a matrix'
        r = len(self.__matrix)
        c = len(self.__matrix[0])
        assert r == len(other.__matrix), 'Number of rows are not equal'
        assert c == len(other.__matrix[0]), 'Number of columns are not equal'

        sum = []
        for e in range(rows):
            sum.append([])
            for j in range(cols):
                sum[e].append(0)

        for e in range(rows):
            for j in range(cols):
                sum[e][j] = self.__matrix[e][j] + other.__matrix[e][j]

        return Matrix(sum)

    def __mul__(self, other):

        assert isinstance(other, Matrix), 'It is not a matrix'
        r1 = len(self.__matrix)
        c1 = len(self.__matrix[0])
        r2 = len(other.__matrix)
        c2 = len(other.__matrix[0])
        assert c1 == r2, 'The number of colums of the first matrix are different from the number of rows of the second one'
        
        product = []
        for i in range(r1):
            product.append([])
            for j in range(c2):
                product[i].append(0)

        # fill in prods
        for i in range(r1):
            for j in range(c2):
                for k in range(r2):
                    product[i][j] += self.__matrix[i][k] * other.__matrix[k][j]

        return Matrix(product)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        else:
            return self.__matrix == other.__matrix

    def __hash__(self):
        return hash(tuple([tuple(row) for row in self.__matrix]))

    def __repr__(self):
        return repr(self.__matrix)


if __name__ == '__main__':
    M = Matrix([[5,5],[5,5]])
    T = Matrix([[5,5],[5,5]])
    print(M)
    print(M == T)
    d = {M: "1", T: "2"}
    d.update({M: "3"})
    print(d)