
import numpy as np
import sympy as sp
import array
from colorama import Fore, Back, Style

class InvalidParamEntry(Exception):
    """Raised when invalid parameter is passed"""

class Structure:
    
    def __init__(self, label: str = "new_array"):
        self.name = label
        
    def print_complexities(self, tc: str, sc: str) -> None:
        print('\n')
        print(Style.BRIGHT)
        print(Fore.GREEN + 'Time Complexity')
        print(Style.RESET_ALL)
        print(Fore.GREEN + tc)
        print(Style.RESET_ALL)
        print(Style.BRIGHT)
        print(Fore.GREEN + 'Space Complexity')
        print(Style.RESET_ALL)
        print(Fore.GREEN + sc)
    
    
    def make_range_array(self, length: int, rows: int, cols: int) -> tuple:
        """
            Create a range array of a given length, rows and columns
            
            Parameters
            ----------
            length : int
                the length of the array
            rows: int
                the number of rows in the array
            cols : int
                the number of columns in the array

            Raises
            ======
                InvalidParamEntry

            Returns
            -------
            tuple
                A tuple containing the array and the sympy matrix
        """
        if([isinstance(length, int), isinstance(rows, int), isinstance(cols, int)]):
            arr = np.arange(length).reshape(rows, cols)
            if arr.ndim == 1:
                oneDim = arr.flatten()
                matrix = sp.Matrix(arr)
                return oneDim, matrix
            else:
                matrix = sp.Matrix(arr)
                return arr, matrix
        else:
            msg = "Invalid parameter passed"
            raise InvalidParamEntry(msg)
        
    
    def make_random_array(self, low: int = 1, high: int = 9, size: tuple = (1, 5)) -> tuple:
        """
            Create a random array of a given low, high and size
            
            Parameters
            ----------
            low : int
                the lower bound of the random number
            high: int
                the upper bound of the random number
            size : tuple
                the size of the array
                
        Raises
        ======
            InvalidParamEntry
        """
        arr = np.random.randint(low = low, high = high, size = size)
        if arr.shape[0] == 1:
            oneDim = arr.flatten()
            matrix = sp.Matrix(arr)
            return oneDim, matrix
        else:
            matrix = sp.Matrix(arr)
            return arr, matrix
        
    def make_array(self, arr: np.ndarray) -> np.ndarray:
        """"
            Create an array from a given numpy array
            
            Parameters
            ----------
            arr : np.ndarray
                the numpy array to be converted
            low : int
                the lower bound of the random number
            high: int
                the upper bound of the random number
            size : tuple
                the size of the array
            
            Raises
            ======
                InvalidParamEntry
        """
        if isinstance(arr, np.ndarray):
            if len(arr) == 1:
                onedim = arr.fllatten()
                matrix = sp.Matrix(arr)
                return onedim, matrix
            else:
                matrix = sp.Matrix(arr)
                return arr, matrix 
        else:
            msg = "Argument psssed to make_array() must be a ndarray"
            raise InvalidParamEntry(msg)

        
        
    def add_row_to_matrix(self, matrix: np.ndarray, row: np.ndarray, idx: int = 0,) -> sp.Matrix:
        """
            Add a row to a matrix at a given index
            
            Parameters
            ----------
            matrix : np.ndarray
                the matrix to add the row to
            row: np.ndarray
                the row to be added
            idx : int
                the index to add the row
                
            Raises
            ======
                InvalidParamEntry
        """
        if all([(isinstance(idx, int)), (isinstance(matrix, np.ndarray)), (isinstance(row, np.ndarray))]):
            if row.shape[1] == matrix.shape[1]:
                arr = np.insert(matrix, idx, row, axis = 0)
                matrix = sp.Matrix(arr)
                return arr, matrix 
            else:
                msg = "Row must have the same number of columns as the matrix"
                raise InvalidParamEntry(msg)
        else:
            msg = "Invalid parameter passed"
            raise InvalidParamEntry(msg)
        
        
    def add_col_to_matrix(self, matrix: np.ndarray, col: np.ndarray, idx: int = 0,) -> sp.Matrix:
        """
            Add a column to a matrix at a given index
            
            Parameters
            ----------
            matrix : np.ndarray
                the matrix to add the column to
            col: np.ndarray
                the column to be added
            idx : int
                the index to add the column
        """
        if all([(isinstance(idx, int)), (isinstance(matrix, np.ndarray)), (isinstance(col, np.ndarray))]):
            if col.shape[1] == matrix.shape[1]:
                arr = np.insert(matrix, idx, col, axis = 1)
                matrix = sp.Matrix(arr)
                return arr, matrix 
            else:
                msg = "Column must have the same number of columns as the matrix"
                raise InvalidParamEntry(msg)
        else:
            msg = "Invalid parameter passed"
            raise InvalidParamEntry(msg)
                    
    
