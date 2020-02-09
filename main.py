class TestClass:
    """
    This class is made to test sphinx!
    """

    def testfunc(self, x:float, y:float) -> float:
        """sum

        testfunc to sum two args

        Parameters
        ----------
            x:float
                1st argument
            y:float
                2nd argument

        Returns
        -------------
            float
                sum result
        Note
        -----------
        Here is note

        Examples
        --------------
            >>> print(testfunc(2,5))
            7
        """
        return x+y