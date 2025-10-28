
class InvalidTypeError(Exception):
    """Raised when invalid type passed as a parameter"""
    pass 

class LargeArrayError(Exception):
    """Raised when Iteration List is too large to process"""
    pass


class Combinatorics:   
    def __init__(self, combKeys: int = 0):
        self.keys = combKeys


    def chunk_list(self, chunks : list, size : int):
        """
        split list into equal size lengths based on parameter size
    
        Parameters
        ----------
        chunks : list, mandatory - the list to be split
        size : int, mandatory  - the size of each segment to be split
        Returns
        -------
        list that contain the the parts of the list that were split
        """    
        if isinstance(chunks, list) and isinstance(size, int):
            for chunk in range(0, len(chunks), size):
                yield chunks[chunk:chunk + size]           
        else:
            raise InvalidTypeError()

        
    def get_permutation_without_reps(self, n : int = 0, k : int = 0, val : str = "N")->int | float:
        import math 
        from IPython.display import display, Math 
        """
        calculate the permutations of the based on parameter n and r 
    
        Parameters
        ----------
        n : int, mandatory - The set from which elements are permuted
        k : int, mandatory  - size of each permutation
            n, k are both non negative integers
        val: str, optional - Default "N"
            If N  ipython display is returned, If Y calculation result is return as float value 

        Returns
        -------
        IPython display message that reads out 
        """       
        if isinstance(n, int) and isinstance(k, int):
            denom = n - k
            fac_n = math.factorial(n)
            fac_denom = math.factorial(denom)
            ans = float(fac_n/fac_denom )


            msg = '\\displaystyle _nP_k = \dfrac{n!}{(n - k)!} \\\\~\\\\-\\\\'
            msg = msg + '_%sP_{%s} = \\dfrac{%s!}{(%s - %s)!} = \\dfrac{%s!}{%s!} = \\dfrac{%s}{%s} = %s'
            if val == "N":
                return display(Math(msg%(n, k, n, n, k, n, denom, fac_n, fac_denom, ans)))
            else:
                return ans 
        else:
            raise InvalidTypeError()


    def get_permutation_with_reps(self, n : int = 0, r : int = 0, val : str = "N"):
        import math 
        from IPython.display import display, Math 
        """
        calculate the permutations based on parameters n and r 
    
        Parameters
        ----------
        n : int, mandatory - The set from which elements are permuted
        r : int, mandatory  - size of each permutation
            n, r are both non negative integers
        val: str, optional - Default "N"
            If N  ipython display is returned, If Y calculation result is return as float value 

        Returns
        -------
        IPython display message that reads out 
        """       
        if isinstance(n, int) and isinstance(r, int):
            ans = float(n**r)


            msg = '\\displaystyle nP_r = n^r \\\\~\\\\%sP_{%s} = %s^{%s} = %s'
    
            if val == "N":
                return display(Math(msg%(n, r, n, r, ans)))
            else:
                return ans 
        else:
            raise InvalidTypeError()
        
        

    def get_combinations_with_repetition(self, n : int, k : int, val : str = "N"):
        import math 
        from IPython.display import display, Math 
        """
        calculate the combination with repetition based on parameters n and k
        Ex:
        we choose 3 people out of 20. 
        But we allow for repeated people
        Combinations with Repetition so Steve, Ahmet, Liz (SAL), and Liz, Ahmet, Steve (LAS)
        are are included, along with LLA, SSS, WAW, SWW and many more. 
        Returns the number of sets of 3 were order does not matter but repetition is allowed

        ----------
        n : int, mandatory - The set from which elements are permuted
        k : int, mandatory  - size of each combination, or the number of choices made
            n, k are both non negative integers
        val: str, optional - Default "N"
            If N  ipython display is returned, If Y calculation result is return as float value 

        Returns
        -------
        IPython display message that reads out 
        """   
        if isinstance(n, int) and isinstance(k, int):
            
            num_fact = k + n - 1
            denom_fact_k = k
            denom_fact_n = n - 1
            num_ans = math.factorial(num_fact)
            denom_ans_k = math.factorial(denom_fact_k)
            denom_ans_n = math.factorial(denom_fact_n)
            denom_ans = denom_ans_k * denom_ans_n
            ans = float(num_ans/denom_ans )
            
            

            msg = '\\displaystyle _nC_k = \\dfrac{(k + n - 1)!}{k!(n - 1)!}\\\\~\\\\'
            msg = msg + '\\displaystyle _%sC_{%s} = \\dfrac{(%s + %s - 1)!}{%s!(%s - 1)!} = '
            msg = msg + '\\dfrac{%s!}{%s! \\cdot %s!} = \\dfrac{%s}{%s \\cdot %s} = \\dfrac{%s}{%s} = %s'
    
            if val == "N":
                return display(Math(msg%(n, k, k, n, k, n, num_fact, denom_fact_k, denom_fact_n
                                         ,num_ans, denom_ans_k, denom_ans_n, num_ans, denom_ans, ans)))
            else:
                return ans 
        else:
            raise InvalidTypeError()
        
        
        
    def get_combinations_without_repetition(self, n : int = 0, k : int = 0, val : str = "N"):
        import math 
        from IPython.display import display, Math 
        """
        calculate the combination without repetition based on parameters n and k 
        Ex:
        we choose 3 people out of 20. Returns the number of sets of 3 were order does not matter
        However Steve, Ahmet, Liz (SAL) and Liz, Ahmet and Steve (LAS) are included
        LLA, SAS, AAA are not allowed
  

        Returns the number of sets were order does not matter and repetition NOT ALLOWED
        LLA, SSS, WAW will not be included for example

        Parameters
        ----------
        n : int, mandatory - The set from which elements are permuted
        k : int, mandatory  - size of each combination, choices made 
            n, k are both non negative integers
        val: str, optional - Default "N"
            If N  ipython display is returned, If Y calculation result is return as float value 

        Returns
        -------
        IPython display message that reads out 
        """   
        if isinstance(n, int) and isinstance(k, int):
            
            num_ans = math.factorial(n) 
            denom_fact_k = math.factorial(k)
            denom_sub_n = n - k
            denom_fact_n = math.factorial(denom_sub_n)
            denom_ans = denom_fact_k * denom_fact_n
            ans = num_ans/denom_ans
            display_ans = f'{(num_ans/denom_ans):,}'
            
            msg = '\\displaystyle _nC_{k} = \\dfrac{n!}{k!(n - k)!}\\\\~\\\\~\\\\'
            msg = msg + '_%sC_{%s} = \\dfrac{%s!}{%s!(%s - %s)!} = '
            msg = msg + '\\dfrac{%s!}{%s! \\cdot %s!} = \\dfrac{%s}{%s} = %s'

            if val == "N":
                return display(Math(msg%(n, k, n, k, n, k, n, k, denom_sub_n, num_ans, denom_ans, display_ans)))
            else:
                return ans 
        else:
            raise InvalidTypeError()
        
        
    def get_variation_without_repetition(self, n : int = 0, k : int = 0, val : str = "N"):
            import math 
            from IPython.display import display, Math 
            """
            calculate the variation without repetition based on parameters n and p
        
            Parameters
            ----------
            n : int, mandatory - The set from which elements are permuted
            k : int, mandatory  - size of element variations
                n, r are both non negative integers
            val: str, optional - Default "N"
                If N  ipython display is returned, If Y calculation result is return as float value 

            Returns
            -------
            IPython display message that reads out result
            Or
            int/float result of calculation determined by the parameter val
            """   
            if isinstance(n, int) and isinstance(k, int):
                
                denom_sub = n - k
                num_ans = math.factorial(n)
                denom_ans = math.factorial(denom_sub)
                ans = num_ans / denom_ans               

                msg = '\\displaystyle \\large V^k_n = \\dfrac{n!}{(n - k)!} = '
                msg = msg + '\\dfrac{%s!}{(%s - %s)!} = \\dfrac{%s!}{%s!} = \\dfrac{%s}{%s} = %s'


                if val == "N":
                    return display(Math(msg%(n, n, k, n, denom_sub, num_ans, denom_sub, ans)))
                else:
                    return ans 
            else:
                raise InvalidTypeError()
            
            
    def get_variation_with_repetition(self, n : int = 0, k : int = 0, val : str = "N"):
            import math 
            from IPython.display import display, Math 
            """
            calculate the variation without repetition based on parameters n and p
        
            Parameters
            ----------
            n : int, mandatory - The set from which elements are permuted
            k : int, mandatory  - size of element variations
                n, r are both non negative integers
            val: str, optional - Default "N"
                If N, ipython display is returned, If Y calculation result is return as float value 

            Returns
            -------
            IPython display message that reads out result
            Or
            int/float result of calculation determined by the parameter val
            """   
            if isinstance(n, int) and isinstance(k, int):
                
                ans = n**k    

                msg = '\\displaystyle \\large \\bar{V}^k_n = \\bar{V}^{%s}_{%s} = %s^{%s} = %s'

                if val == "N":
                    return display(Math(msg%(k, n, n, k, ans)))
                else:
                    return ans 
            else:
                raise InvalidTypeError()
            
        
    def get_combination_list(self, lst : list, size : int,)-> list:
        """
        calculate the combinations of the parameter lst based on parameter size
    
        Parameters
        ----------
        list : list, mandatory
        size : int, mandatory 

        Returns
        -------
        list 
        """
        if isinstance(lst, list) and isinstance(size, int):
            from itertools import combinations
            comb = list(combinations(lst, size))
            return comb 
        else:
            raise InvalidTypeError()

 
    

    def get_permutation_list(self, lst : list, size : int)-> list:
        """
        calculate the combinations of the parameter lst based on parameter size
    
        Parameters
        ----------
        list : list, mandatory
        size : int, mandatory 

        Returns
        -------
        list 
        """
        if isinstance(lst, list) and isinstance(size, int):
            from itertools import permutations
            res = list(permutations(lst, size)) 
            return res 
        else:
            raise InvalidTypeError()