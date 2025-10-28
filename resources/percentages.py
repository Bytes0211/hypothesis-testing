# percentages.py
import numpy as np 

class InvalidParamEntry(Exception):
    """Raised when invalid parameter is passed"""
    pass

class Pct():
    
    def __init__(self):
        self.msg  = ''

    def get_pct_of_num(self, pct : int | float, num : int | float, std_out : str = 'N') -> int | float :
        """
        calculate the percentage of a number 
        
        Parameters 
        ----------
        pct : int | float, mandatory - The percentage of the num argument to calculate
        num : int | float, mandatory  - the number to calculate the percentage of 

        Returns
        -------
        int | float
        """
        if (pct > 0 and pct < 100) and num > 0:
            ans = (pct/100) * num 
            if std_out == 'Y':
                from IPython.display import display, Math 
                msg = '\\displaystyle \\text{%s is %s percent of %s}'
                return display(Math(msg%(ans, pct, num)))
                
            else:
                return ans
        else:
            raise InvalidParamEntry()


    def get_pct_of_two_nums(self, num1 : int | float, num2 : int | float, std_out : str = 'N') -> int | float :  
        """
        calculate the percentage difference of two number\s
        
        Parameters 
        ----------
        num1 : int | float, mandatory  - the first number in the percent difference calculation
        num2 : int | float, mandatory  - the second number in the percent difference calculation 

        Returns
        -------
        int | float
        """
        if num1 > 0 and num2 > 0:
            import numpy as np 
            diff = np.abs(num1 - num2)
            avg = (num1 + num2) / 2
            tmp = (diff / avg)
            if tmp > 1:
                tmp2 = tmp - 1
                ans = (1 - tmp2) * 100 
            else:
                ans = (diff / avg) * 100
        if std_out == 'Y':
            from IPython.display import display, Math 
            msg = '\\displaystyle \\text{The percentage diffence between %s and %s is %s}'
            return display(Math(msg%(num1, num2, ans)))          
        else:
            return ans





