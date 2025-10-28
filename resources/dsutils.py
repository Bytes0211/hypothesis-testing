""" 
# datum.py
Data class contains functions to support statistical calculations
"""

from typing import Iterable, List, Dict, Tuple
import numpy as np
import copy 
from tabulate import tabulate 
from IPython.display import display, Markdown, Math 
import sys 
sys.path.insert(0, '..')
from resources import datum

data = datum.Data()





class InvalidParamEntry(Exception):
    """Raised when invalid parameter is passed"""

class InvalidParamValue(Exception):
    """Raised when invalid parameter is passed"""

class InvalidTypeError(Exception):
    """Raised when invalid type passed as a parameter"""


class InvalidKeyError(Exception):
    """Raised when invalid type is passed as a key """


class InvalidDictError(Exception):
    """Raised when invalid object passed as dictionary """


class Utils: 
    
    def __init__(self, x: List, y: List):
        if isinstance(x, list) and isinstance(y, list):
            self.x = x
            self.y = y


    def chart_regression(self, chart: bool = False, statement: bool = False):
        
        if chart: 
            x_tbl = copy.copy(self.x)
            y_tbl = copy.copy(self.y)
            
            mu_x = np.mean(self.x)
            mu_y = np.mean(self.y)
            s_x = np.std(self.x)
            s_y = np.std(self.y)
            xy = [self.x[i] * self.y[i] for i in range(len(self.x))]
            var_x = [self.x[i] - mu_x for i in range(len(self.x))]
            var_y = [self.y[i] - mu_y for i in range(len(self.y))]
            mu_x_sqr = [(i - mu_x)**2 for i in self.x]
            mu_y_sqr = [(i - mu_y)**2 for i in self.y]
            mu_x_mu_y = [var_x[i] * var_y[i] for i in range(len(self.x))]

            # get sums 
            x_sum = sum(self.x)
            y_sum = sum(self.y)
            xy_sum = sum(xy)
            mu_x_sqr_sum = sum(mu_x_sqr)
            mu_y_sqr_sum = sum(mu_y_sqr)
            cov = sum(mu_x_mu_y) # covariance is the sum of (x - mu_x) * (y - mu_y)
            mu_cov = np.mean(mu_x_mu_y)
            col1 = list(range(1, (len(self.x) + 1)))
            
            # add sum to the columns 
            x_tbl.append(x_sum)
            y_tbl.append(y_sum)
            xy.append(xy_sum)
            mu_x_sqr.append(mu_x_sqr_sum)
            mu_y_sqr.append(mu_y_sqr_sum)
            mu_x_mu_y.append(cov)
            col1.append('$\Sigma$')

            # add mean to the columns 
            x_tbl.append(mu_x)
            y_tbl.append(mu_y)
            xy.append(np.mean(xy[:len(self.x)]))
            mu_x_sqr.append(np.mean(mu_x_sqr[:len(self.x)]))
            mu_y_sqr.append(np.mean(mu_y_sqr[:len(self.x)]))
            mu_x_mu_y.append(np.mean(mu_x_mu_y[:len(self.x)]))
            col1.append('$\mu$')
            
            xy_sum, mu_x_sqr_sum, mu_y_sqr_sum, cov, mu_cov = data.chart_regression(self.x, self.y)

            info = {'point #': col1, '$x$': x_tbl, '$y$':  y_tbl, '$xy$': xy, '$\mu_x^2$': mu_x_sqr, '$\mu_y^2$': mu_y_sqr, '$\mu_x \cdot \mu_y$': mu_x_mu_y}
            tab = tabulate(info, headers='keys', tablefmt='pipe', numalign="center", stralign="center")
            header = '<br><b>Regresion Chart</b><br><br>\r'
            disp = header + tab
            display(Markdown(disp))
        
        if statement: 
            r = data.get_corr_coeff(cov = mu_cov, s_x = s_x, s_y = s_y)
            beta1 = data.get_beta1(r = r, x_arr = self.x, y_arr = self.y)
            #b_0 = mu_y - (b_1 * mu_x)
            beta0 = data.get_beta0(b_1 = beta1, x_arr=self.x, y_arr=self.y)

            msg = '\\\\~\\\\'
            msg = msg + '\\displaystyle s_x: %s\\\\~\\\\s_y: %s\\\\~\\\\r: %s\\\\~\\\\'
            msg = msg + '\\beta_1: %s\\\\~\\\\\\beta_0: %s\\\\~\\\\'
            msg = msg + '\\hat{\\beta}_0 = \\hat{y} - (\\hat{\\beta}_1 \\cdot \\bar{x}) \\Rightarrow \\hat{\\beta}_0 = %s - (%s \\cdot %s) = %s'

            display(Math(msg%(
                f'{s_x: .4f}', f'{s_y: .4f}'
                ,f'{r: .4f}'
                ,f'{beta1: .6f}', f'{beta0: .6f}'
                , f'{mu_y: .2f}', f'{beta1: .6f}', f'{mu_x: .2f}', f'{beta0: .6f}'
                )))
        