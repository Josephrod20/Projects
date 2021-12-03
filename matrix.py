# ------------------------------------------------------------------------------
# matrix.py
# ------------------------------------------------------------------------------
from random import uniform


class Matrix:
    """Class representing a rectangular matrix."""

    # built-in methods ---------------------------------------------------------
    def __init__(self, L=[]):
        """
        Initialize a Matrix object from a list of lists. If the list is empty,
        the resulting Matrix is empty (size 0x0).
        """

        # get number of rows and columns
        n = self.numRows = len(L)
        m = self.numCols = len(L[0]) if n > 0 else 0
        self.elements = {}
        if n == 0:
            return
        # end if

        # build dictionary
        if n > 0:
            for i in range(n):
                if len(L[i]) != m:
                    msg = f"could not create Matrix from ragged list:\n{L}"
                    raise ValueError(msg)
                # end if
                for j in range(m):
                    self.elements[(i + 1, j + 1)] = L[i][j]
                # end for
            # end for
        # end if

    # end init__()

    def __str__(self):
        """
        Return string representation of self.
        """

        strings = []
        for i in range(1, self.numRows + 1):
            strings.append([])
            for j in range(1, self.numCols + 1):
                strings[-1].append(f"{self.elements[(i, j)]:8.2f}")
        return "\n".join(" ".join(string) for string in strings)

    def __eq__(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            return False
        for index, v in self.elements.items():
            if v != other.elements[index]:
                return False
        return True

    # Matrix instance methods --------------------------------------------------
    def add(self, other):
        """
        Return sum of self with other.
        """
        if self.numCols != other.numCols or self.numRows != other.numRows:
            raise ValueError("add(): incompatible matrix sizes:\n")

        result = Matrix()
        result.numCols = self.numCols
        result.numRows = self.numRows

        for index, v in self.elements.items():
            result.elements[index] = v + other.elements[index]

        return result

    def sub(self, other):
        """
        Return difference of self with other.
        """

        if self.numCols != other.numCols or self.numRows != other.numRows:
            raise ValueError("sub(): incompatible matrix sizes:\n")

        result = Matrix()
        result.numCols = self.numCols
        result.numRows = self.numRows

        for index, v in self.elements.items():
            result.elements[index] = v - other.elements[index]

        return result

    def scale(self, c):
        """
        Return the scalar product of self with c.
        """

        result = Matrix()
        result.numRows = self.numRows
        result.numCols = self.numCols

        for index, v in self.elements.items():
            result.elements[index] = v * c

        return result

    def trans(self):
        """
        Return the transpose of self.
        """

        result = Matrix()
        result.numRows = self.numCols
        result.numCols = self.numRows

        for (i, j), v in self.elements.items():
            result.elements[(j, i)] = v
        return result

    def mult(self, other):
        """
        Return product of self by other.
        """

        if self.numCols != other.numRows:
            raise ValueError("mult(): incompatible matrix sizes:\n")

        result = Matrix()
        n = result.numRows = self.numRows
        m = result.numCols = other.numCols

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                result.elements[(i, j)] = 0
                for k in range(1, self.numCols + 1):
                    result.elements[(i, j)] += (
                        self.elements[(i, k)] * other.elements[(k, j)]
                    )

        return result

    # Matrix class methods -----------------------------------------------------
    def from_string(s=""):
        """
        Return the Matrix represented by the string s. If s is empty, the
        resulting Matrix is empty (size 0x0).
        """

        lst_mat = [list(map(int, line.split())) for line in s.splitlines()]
        return lst_mat

    def identity(n):
        """
        Return the nxn identity Matrix.
        """

        lst_mat = [[0 if i != j else 1 for i in range(n)] for j in range(n)]
        return lst_mat

    def randMatrix(n, m, a, b):
        """
        Return an nxm Matrix with random elements x, uniformly distributed over
        the interval a<=x<=b.
        """

        lst_mat = [[uniform(a, b) for _ in range(m)] for _ in range(n)]
        return lst_mat
