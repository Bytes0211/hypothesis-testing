
# message.py

class Statement:
    def __init__(self, data : dict = {}) -> None:
        self.data = data 

    def create_statement(self):
        from IPython.display import display, Math 
        import numpy as np 
        ###############################
        # user for all test and tail types
        # critical value calculation
        # if upper tail
        if self.data["tail"] == "upper":
            if self.data["critical_value_upper"]:
                cv_msg = '\\qquad \\star~\\text{upper tail critical value test:}\\\\~\\\\'
                cv_msg = cv_msg + '\\qquad \\qquad \\star~\\text{test statistic %s is greater than the critical value %s}\\\\~\\\\'
                cv_msg = cv_msg + '\\qquad \\qquad \\star~\\text{the critical value test fails to support for the Null Hypothesis}\\\\~\\\\~\\\\'
            else:
                cv_msg = '\\qquad \\star~\\text{upper tail critical value test:}\\\\~\\\\'
                cv_msg = cv_msg + '\\qquad \\qquad \\star~\\text{test statistic %s is less than the critical vaue %s}\\\\~\\\\'
                cv_msg = cv_msg + '\\qquad \\qquad \\star~\\text{the critcal value test lends support for the Null Hypothesis}\\\\~\\\\~\\\\'
        # if lower tail
        if self.data["tail"] == "lower":
            if self.data["critical_value_lower"]:
                cv_msg = '\\qquad \\star~\\text{lower tail critical value test:}\\\\~\\\\'
                cv_msg = cv_msg + '\\qquad \\qquad \\star~\\text{test statistic %s is less than the critical value %s}\\\\~\\\\'
                cv_msg = cv_msg + '\\qquad \\qquad \\star~\\text{the critical value test fails to support for the Null Hypothesis}\\\\~\\\\~\\\\'
            else:
                cv_msg = '\\qquad \\star~\\text{lower tail critical value test:}\\\\~\\\\'
                cv_msg = cv_msg + '\\qquad \\qquad \\star~\\text{test statistic %s is greater than the critical vaue %s}\\\\~\\\\'
                cv_msg = cv_msg + '\\qquad \\qquad \\star~\\text{the critical value test lends support for the Null Hypothesis}\\\\~\\\\~\\\\'
        # else two two tail
        else:
            if self.data["critical_value_lower"] or self.data["critical_value_upper"]:
                cv_msg = '\\qquad \\star~\\text{two tail critical value test:}\\\\~\\\\'
                cv_msg = cv_msg + '\\qquad \\qquad \\star~\\text{test statistic %s is more extreme than the critical value %s}\\\\~\\\\'
                cv_msg = cv_msg + '\\qquad \\qquad \\star~\\text{the critical value test fails to support for the Null Hypothesis}\\\\~\\\\~\\\\'
            else:
                cv_msg = '\\qquad \\star~\\text{two critical value test:}\\\\~\\\\'
                cv_msg = cv_msg + '\\qquad \\qquad \\star~\\text{test statistic %s is less extreme than the critical vaue %s}\\\\~\\\\'
                cv_msg = cv_msg + '\\qquad \\qquad \\star~\\text{the critical value test lends support for the Null Hypothesis}\\\\~\\\\~\\\\'
        
        # display calculation for test statistic         
        nom = round((self.data['xbar1'] - self.data['observed_value']), 4)
        denom = round(self.data['s1'] / np.sqrt(self.data['n1']), 4)
        sqrt_n = round(np.sqrt(self.data['n1']))
        if self.data["p_value"] > 0.10:
            # p-value test
            conclusion = '\\qquad \\star~\\text{p-value test:}\\\\~\\\\'
            conclusion = conclusion + '\\qquad \\qquad \\star~\\text{p-value %s} > 0.10\\\\~\\\\'
            conclusion = conclusion + '\\qquad \\qquad \\star~ \\text{There is weak or no evidence against Null Hypothesis}\\\\~\\\\'
            # critical value test 
            conclusion = conclusion + cv_msg
        elif self.data["p_value"] > 0.05 and self.data["p_value"] <= 0.10:
            conclusion = '\\qquad \\star~\\text{p-value value test}\\\\~\\\\'
            conclusion = conclusion + '\\qquad \\qquad \\star~0.05 < \\text{p-value %s} \\le 0.10  \\\\~\\\\'
            conclusion = conclusion + '\\qquad \\qquad \\star~ \\text{There is moderate evidence against Null Hypothesis}\\\\~\\\\'
            # critical value test 
            conclusion = conclusion + cv_msg
        elif self.data["p_value"] >= 0.01 and self.data["p_value"] <= 0.05:
            conclusion = '\\qquad \\star~\\text{p-value value test}\\\\~\\\\'
            conclusion = conclusion + '\\qquad \\qquad \\star~0.01 \\le \\text{p-value %s} \\le 0.05  \\\\~\\\\'
            conclusion = conclusion + '\\qquad \\qquad \\star~ \\text{There is strong evidence against Null Hypothesis}\\\\~\\\\'
            # critical value test 
            conclusion = conclusion + cv_msg
        elif self.data["p_value"] < 0.01:
            conclusion = '\\qquad \\star~\\text{p-value value test}\\\\~\\\\'
            conclusion = conclusion + '\\qquad \\qquad \\star~\\text{p-value %s} < 0.01  \\\\~\\\\'
            conclusion = conclusion + '\\qquad \\qquad \\star~ \\text{There is very strong evidence against Null Hypothesis}\\\\~\\\\'
            # critical value test 
            conclusion = conclusion + cv_msg
        else:
            conclusion = '\\qquad \\star~\\text{p-value value test}\\\\~\\\\'
            conclusion = conclusion + '\\qquad \\qquad \\star~ \\text{There is no statistical evidence for a p-value of %s}\\\\~\\\\'

            conclusion = conclusion + '\\qquad \\star~ \\text{accept the Null Hypothesies } \\Rightarrow '
            conclusion = conclusion + '~H_o:~\\text{ ' + self.data["null_hypo"] + '}\\\\~\\\\'
            conclusion = conclusion + '\\qquad \\star~ \\text{reject the Alternative Hypothesis } \\Rightarrow '
            conclusion = conclusion + '~H_a:~\\text{ ' + self.data["alt_hypo"] + '}\\\\~\\\\' 
        ###############################
        if self.data['type'] == 'diff':
            if self.data['sigma1'] > 0:
                # diff or means with known population standard deviation 
                msg = '\\displaystyle \\quad \\star \\large \\quad n_1,~n_2:~ \\normalsize %s,~%s\\\\~\\\\'
                msg = msg + '\\quad \\star \\large \\quad \\bar{x}_1,~\\bar{x}_2:~ \\normalsize %s,~%s\\\\~\\\\'
                msg = msg + '\\quad \\star \\large \\quad \\sigma_1,~\\sigma_2:~ \\normalsize %s,~%s\\\\~\\\\'
                msg = msg + '\\quad \\star \\quad  \\text{Confidence Level: %s}\\\\~\\\\'
                msg = msg + '\\quad \\star \\quad  a: \\dfrac{(1 - %s)}{2} = %s\\\\~\\\\'
                msg = msg + '\\quad \\star \\quad  \\text{Critical Value: %s}\\\\~\\\\'
                msg = msg + '\\quad \\star \\quad \\text{Population Standard  Deviaiton is known therefore the forumula to use is:}\\\\~\\\\'
                msg = msg + '\\qquad \\quad  (a, b) = (\\bar{x}_1 - \\bar{x}_2) \\pm Z_{\\dfrac{a}{2}} \\cdot \\sqrt{\\dfrac{\\sigma^2_1}{n_1} + \\dfrac{\\sigma^2_2}{n_2}}\\\\~\\\\'
                msg = msg + '\\qquad \\qquad  (a, b) = (%s - %s) \\pm %s \\cdot \\sqrt{\\dfrac{%s^2}{%s} + \\dfrac{%s^2}{%s}}\\\\~\\\\'
                msg = msg + '\\qquad \\qquad (a, b) = %s \\pm %s \\cdot \\sqrt{%s + %s}\\\\~\\\\'
                msg = msg + '\\qquad \\qquad  (a, b) = %s \\pm %s \\cdot %s\\\\~\\\\'
                msg = msg + '\\qquad \\qquad  (a, b) = %s \\pm %s\\\\~\\\\'
                msg = msg + '\\qquad \\qquad  (a, b) = (%s, %s) \\\\~\\\\'
               
                display(Math(msg%(
                    self.data["n1"], self.data["n1"]
                    ,self.data["xbar1"], self.data["xbar2"]
                    ,self.data["sigma1"], self.data["sigma2"]
                    ,self.data["cl"]
                    ,self.data["cl"], f'{self.data["alpha"]: .3f}' 
                    ,self.data["test_statistic"]
                    ,self.data["xbar1"], self.data["xbar2"], self.data["test_statistic"], self.data["sigma1"], self.data["n1"], self.data["sigma2"], self.data["n1"] 
                    ,self.data["diff_of_means"], self.data["test_statistic"], f'{self.data["frac1"]: .4f}', f'{self.data["frac2"]: .4f}'
                    ,self.data["diff_of_means"], self.data["test_statistic"], f'{self.data["std_err"]: .4f}'
                    ,self.data["diff_of_means"], f'{self.data["ci"]: .4f}'
                    ,f'{self.data["a"]: .3f}', f'{self.data["b"]: .3f}'

                )))
            else:
                # diff or means with unknown population standard deviation 
                msg = '\\displaystyle \\quad \\star \\large \\quad n_1,~n_2:~ \\normalsize %s,~%s\\\\~\\\\'
                msg = msg + '\\quad \\star \\large \\quad \\bar{x}_1,~\\bar{x}_2:~ \\normalsize %s,~%s\\\\~\\\\'
                msg = msg + '\\quad \\star \\large \\quad \\sigma_1,~\\sigma_2:~ \\normalsize %s,~%s\\\\~\\\\'
                msg = msg + '\\quad \\star \\large \\quad \\sigma^2_1,~\\sigma^2_2:~ \\normalsize %s,~%s\\\\~\\\\'
                msg = msg + '\\quad \\star \\quad  \\text{Confidence Level: %s}\\\\~\\\\'
                msg = msg + '\\quad \\star \\quad  \\text{two tail alpha } \\rightarrow a = \\dfrac{(1 - %s)}{2} = %s\\\\~\\\\'
                msg = msg + '\\quad \\star \\quad \\text{Since %s is NOT 2 times %s we can state that } %s \\approx %s\\\\~\\\\'
                msg = msg + '\\qquad \\quad \\text{Therefore we can use the pooled standard deviaiton formula : }'
                msg = msg + 'S_p = \\sqrt{\\dfrac{(n_1 - 1) \\cdot s^2_1 + (n_2 - 1) \\cdot s^2_2}{n_1 + n_2 - 2}}\\\\~\\\\'
                msg = msg + '\\qquad \\qquad S_p = \\sqrt{\\dfrac{(%s - 1) \\cdot %s + (%s - 1) \\cdot %s}{%s + %s - 2}}\\\\~\\\\'
                msg = msg + '\\qquad \\qquad S_p = \\sqrt{\\dfrac{%s \\cdot %s + %s \\cdot %s}{%s}}\\\\~\\\\'
                msg = msg + '\\qquad \\qquad S_p = \\sqrt{\\dfrac{%s  + %s}{%s}}\\\\~\\\\'
                msg = msg + '\\qquad \\qquad S_p = %s\\\\~\\\\'
                msg = msg + '\\quad \\star \\quad  df = n_1 + n_2 - 2 = %s + %s - 2 = %s\\\\~\\\\'
                msg = msg + '\\quad \\star \\quad  \\text{critical value : %s}\\\\~\\\\'
                msg = msg + '\\quad \\star \\quad  \\text{confidence interval: }'
                msg = msg + '(a, b) = (\\bar{x}_1 - \\bar{x}_2) \\pm t_{\\dfrac{a}{2}} \\cdot s_p \\cdot \\sqrt{\\dfrac{1}{n_1} + \\dfrac{1}{n_2}}\\\\~\\\\'
                msg = msg + '\\qquad \\qquad (a, b) = (%s - %s) \\pm %s \\cdot %s \\cdot \\sqrt{\\dfrac{1}{%s} + \\dfrac{1}{%s}}\\\\~\\\\'
                msg = msg + '\\qquad \\qquad (a, b) = (%s) \\pm %s \\cdot %s \\cdot %s\\\\~\\\\'
                msg = msg + '\\qquad \\qquad (a, b) = (%s) \\pm %s\\\\~\\\\'
                msg = msg + '\\qquad \\qquad (a, b) = (%s, %s)\\\\~\\\\'


                display(Math(msg%(
                    self.data['n1'], self.data["n2"]
                    , self.data["xbar1"], self.data["xbar2"]
                    , self.data["s1"], self.data["s2"]
                    , f'{self.data["var1"]: .4f}', f'{self.data["var2"]: .4f}'
                    , f'{self.data["cl"]: .2f}'
                    , self.data["cl"], f'{self.data["alpha"]: .3f}' 
                    , f'{self.data["var1"]: .4f}', f'{self.data["var2"]: .4f}',f'{self.data["var1"]: .4f}', f'{self.data["var2"]: .4f}'
                    , self.data['n1'] ,f'{self.data["var1"]: .4f}', self.data["n2"], f'{self.data["var2"]: .4f}', self.data['n1'], self.data["n2"] 
                    , (self.data['n1'] - 1), f'{self.data["var1"]: .4f}', (self.data["n2"] - 1), f'{self.data["var2"]: .4f}', (self.data['n1'] + self.data["n2"] - 2) 
                    , f'{((self.data["n1"] - 1) * self.data["var1"]): .4f}', f'{((self.data["n2"] - 1) * self.data["var2"]): .4f}', (self.data['n1'] + self.data["n2"] - 2) 
                    , f'{self.data["pooled_variance"]: .4f}' 
                    , self.data['n1'], self.data["n2"], self.data["df"]
                    , f'{self.data["test_statistic"]: .4f}'
                    , self.data["xbar1"], self.data["xbar2"], f'{self.data["test_statistic"]: .4f}', f'{self.data["pooled_variance"]: .4f}', self.data['n1'], self.data["n2"]
                    , f'{self.data["diff_of_means"]: .1f}', f'{self.data["test_statistic"]: .4f}', f'{self.data["pooled_variance"]: .4f}', f'{self.data["std_err"]: .4f}'
                    , f'{self.data["diff_of_means"]: .1f}', f'{self.data["ci"]: .4f}'
                    , f'{self.data["b"]: .4f}',  f'{self.data["a"]: .4f}'
                )))
        elif self.data['type']  == 'mean':
            if self.data['mu'] > 0:
                msg_mu_xbar = '\\qquad \\star~ \\mu = %s ~-~ \\text{population mean}\\\\~\\\\'
                mu_xbar = self.data['mu']
            else:
                msg_mu_xbar = '\\qquad \\star~ \\bar{x} = %s ~-~ \\text{sample mean}\\\\~\\\\'
                mu_xbar = self.data['xbar1']
            if self.data['sigma1'] > 0:
                msg_sigma_or_s = '\\qquad \\star~ \\sigma = %s ~-~ \\text{population standard deviation }\\\\~\\\\'
                sigma_or_s = self.data['sigma1']
                sigma_or_s_label = '\\sigma'
            else:
                msg_sigma_or_s = '\\qquad \\star~ s = %s ~-~ \\text{sample standard deviation }\\\\~\\\\'
                sigma_or_s = self.data['s1']
                sigma_or_s_label = 's'
                       
            msg = '\\displaystyle \\text{ Understand the information and the problem statement}\\\\~\\\\'
            msg = msg + '\\qquad \\star~CL~= %s~-~ \\text{ confidence level is the probability that an estimate will include the observed value}\\\\~\\\\'
            msg = msg + '\\qquad \\star~ \\text{%s tail test } ~-~ \\text{type of hypothesis test}\\\\~\\\\'
            msg = msg + msg_mu_xbar
            msg = msg + msg_sigma_or_s
            msg = msg + '\\qquad \\star~ x_o = %s~-~ \\text{mean of observed data}\\\\~\\\\'
            msg = msg + '\\qquad \\star~  n = %s ~-~ \\text{the sample size}\\\\~\\\\'
            msg = msg + '\\qquad \\star~  a = %s ~-~ \\text{the alpha value / level of significance}\\\\~\\\\'
            msg = msg + '\\qquad \\star~  c = %s ~-~ \\text{critical value}\\\\~\\\\'
            msg = msg + '2. \\text{ Form an alternative and null hypothesis}\\\\~\\\\'
            msg = msg + '\\qquad \\star~ H_0: \\text{ ' + self.data["null_hypo"] + '}\\\\~\\\\'
            msg = msg + '\\qquad \\star~ H_a: \\text{ '  + self.data["alt_hypo"] +  '}\\\\~\\\\'
            msg =  msg + '3.\\text{ Calculate the z-score:}\\\\~\\\\'
            msg = msg + '\\qquad \\star~Z = \\dfrac{\\bar{x} - x_o}{\\dfrac{' + sigma_or_s_label + '}{\\sqrt{n}}} = \\dfrac{%s - %s}{\\dfrac{%s}{\\sqrt{%s}}}'
            msg = msg + '=\\dfrac{%s}{\\dfrac{%s}{%s}} = \\dfrac{%s}{%s} = %s\\\\~\\\\'
            msg = msg + '4.\\text{ Find the p-value:}\\\\~\\\\'
            msg = msg + '\\qquad \\star~ \\text{p-value } = %s \\text{ (z-score) } \\Rightarrow  \\text{z-table } \\Rightarrow %s\\\\~\\\\'
            msg = msg + '\\displaystyle 5.\\text{ Perform p-value and critical value test:}\\\\~\\\\'
            msg = msg + conclusion
            display(Math(msg%(
                # Step 1 
                f'{self.data["cl"]: .2f}', self.data["tail"], mu_xbar, sigma_or_s, self.data['observed_value'], self.data['n1'], 
                f'{self.data["alpha"]: .2f}', f'{self.data["critical_value"]: .4f}' 
                # Step 2 (null and alternate hypothesis hardcode in msg) - no variables here
                # Step 3 Calculate the z-score - uses sigma_or_s switch in msg 
                , round(self.data['xbar1'], 4), self.data['observed_value'], round(self.data['s1'], 4), round(self.data['n1'])
                , nom, round(self.data['s1'], 4), sqrt_n, nom, denom, round(self.data['test_statistic'], 4)
                # Step 4 find p-value
                , round(self.data['test_statistic'], 4), self.data["p_value"]
                # Step 5 - p-value test
                ,self.data["p_value"]
                # STep 5 - critical value test
                , round(self.data['test_statistic'], 4), round(self.data['critical_value'], 4)   
                )))
        elif self.data['type']  == 'prop':
            # Section 1
            msg = '\\displaystyle1.\\text{ Understand the information and the problem statement}\\\\~\\\\'
            msg = msg + '\\qquad \\star~CL~= %s~-~ \\text{ confidence level is the probability that an estimate will include the observed value}\\\\~\\\\'
            msg = msg + '\\qquad \\star~  a = %s ~-~ \\text{the alpha value / level of significance}\\\\~\\\\'
            msg = msg + '\\qquad \\star~ \\text{%s tail test } ~-~ \\text{type of hypothesis test}\\\\~\\\\'
            msg = msg + '\\qquad \\star~  n = %s ~-~ \\text{the sample size}\\\\~\\\\'
            msg = msg + '\\qquad \\star~  p = %s ~-~ \\text{The proportion of the sample that is the successes}\\\\~\\\\'
            msg = msg + '\\qquad \\star~  \hat{p} = %s ~-~ \\text{The ratio of successes relative to the sample size}\\\\~\\\\'
            msg = msg + '2. \\text{ Form an alternative and null hypothesis}\\\\~\\\\'
            msg = msg + '\\qquad \\star~ H_0: \\text{ ' + self.data["null_hypo"] + '}\\\\~\\\\'
            msg = msg + '\\qquad \\star~ H_a: \\text{ '  + self.data["alt_hypo"] +  '}\\\\~\\\\'
            msg =  msg + '3.\\text{ Calculate the z-score:}\\\\~\\\\'
            msg = msg + '\\qquad \\star~Z = \\dfrac{\\hat{p} - p}{\\sqrt{\\dfrac{p(1 - p)}{n}}} = '
            msg = msg + '\\dfrac{%s - %s}{\\sqrt{\\dfrac{%s(1 - %s)}{%s}}} = \\dfrac{%s}{%s} = %s\\\\~\\\\'
            msg = msg + '4.\\text{ Find the p-value:}\\\\~\\\\'
            msg = msg + '\\qquad \\star~ \\text{p-value } = %s \\text{ (z-score) } \\Rightarrow  \\text{z-table } \\Rightarrow %s\\\\~\\\\'
            msg = msg + '\\displaystyle 5.\\text{ Perform p-value and critical value test:}\\\\~\\\\'
            msg = msg + conclusion

            nom = round((self.data["p_hat"] - self.data["p"]), 4)
            denom = round((np.sqrt((self.data["p"] * (1 - self.data["p"]))/self.data["n1"])), 4)

            display(Math(msg%(
                # section 1
                f'{self.data["cl"]: .2f}', f'{self.data["alpha"]: .2f}', self.data["tail"], self.data['n1'], self.data['p'], self.data['p_hat']
                # Step 2 (null and alternate hypothesis hardcode in msg) - no variables here
                # Step 3 Calculate the z-score - uses sigma_or_s switch in msg 
                ,f'{self.data["p_hat"]: .3f}', self.data["p"], self.data["p"], self.data["p"], self.data["n1"], nom, denom, f'{self.data["test_statistic"]: 4f}'
                # Step 4: Calculate the p-value
                , f'{self.data["test_statistic"]: 4f}', f'{self.data["p_value"]: .4f}'
                # Step 5 - p-value test
                ,self.data["p_value"]
                # STep 5 - critical value test
                , round(self.data['test_statistic'], 4), round(self.data['critical_value'], 4)  
                )))
        else:
            print('Statement for hypothesis test of proportion coming soon')