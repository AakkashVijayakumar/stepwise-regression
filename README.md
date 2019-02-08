# Stepwise Regression
 
A python package which executes linear regression forward and backward

# Usage

The package can be imported and the functions

forward_regression:

Performs a forward feature selection 
    based on p-value from statsmodels.api.OLS
    Arguments:
        X - pandas.DataFrame with candidate features
        y - list-like with the target
        threshold_in - include a feature if its p-value < threshold_in
        verbose - whether to print the sequence of inclusions and exclusions
    Returns: list of selected features
    
backward_regression:

Performs a forward feature selection 
    based on p-value from statsmodels.api.OLS
    Arguments:
        X - pandas.DataFrame with candidate features
        y - list-like with the target
        threshold_out - exclude a feature if its p-value > threshold_out
        verbose - whether to print the sequence of inclusions and exclusions
    Returns: list of selected features


can be used