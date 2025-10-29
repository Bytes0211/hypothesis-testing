
import numpy as np 
import sys
sys.path.insert(0, '..')
from resources import test, datum 

test = test.Test()
data = datum.Data()

def create_test_params():    
    test_type = "prop"
    CL = 0.95
    mu = 0
    sigma1 = 1
    sigma2 = 0
    tail = 'lower'   
    N = 0                                      
    n1 = 100
    n2 = 80
    xbar1 = 0 # the mean of the expected value
    xbar2 = 0
    p_hat = 0
    p1 = 0.30
    p2 = 0.40
    observed_value = 0 # the historical mean
    successes = 20    
    p = 0.25
    var1 = 0
    s1 = 1
    s2 = 0
    null_hypo = 'p is greater than or equal to 0.25'
    alt_hypo = 'p is less than 0.25'
    
    # no need to check mu and sigma values for test type proportion 
    mean = mu
    std_dev = sigma1
    #std_dev = sigma1 if sigma1 > 0 else s1
    # mean = mu if mu > 0 else xbar1
    
    # for a proportion test I will use a standard normal distr
    x_data = list(np.linspace(-3, 3, n1))
    y_data = data.get_normal_dist(x_arr= x_data, mu = mean, sigma = std_dev)
    hypothesize_diff = 30
    statement = True 
    visual = True 


    
    margin_of_error_for_calculating_minimum_n = 2
    
    test_params = {}
    test_params['cl'] = CL
    test_params['type'] = test_type 
    test_params['mu'] = mu
    test_params['tail'] = tail
    test_params['N'] = N
    test_params['sigma1'] = sigma1
    test_params['sigma2'] = sigma2
    test_params['n1'] = n1
    test_params['n2'] = n2
    test_params['xbar1'] = xbar1
    test_params['xbar2'] = xbar2
    test_params['p_hat'] = p_hat
    test_params['p'] = p
    test_params['p1'] = p1
    test_params['p2'] = p2
    test_params['observed_value'] = observed_value
    test_params['successes'] = successes
    test_params['var1'] = var1
    test_params['s1'] = s1
    test_params['s2'] = s2
    test_params['hypothesize_diff'] = hypothesize_diff
    test_params['x_data'] = x_data
    test_params['y_data'] = y_data
    test_params['null_hypo'] = null_hypo
    test_params['alt_hypo'] = alt_hypo
    test_params['mar_err_min_n'] =   margin_of_error_for_calculating_minimum_n
    test_params["statement"] = statement
    test_params["visual"] = visual
    test
    return test_params

# check out the data before testing 
# params = create_test_params()
# data.check_normality(params["y_data"])

test.make_hypothesis_test(info = create_test_params())

