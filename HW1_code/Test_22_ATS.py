from code_py.get_dataset import *
from code_py.ex22 import RBF_Extreme_Opt
import numpy as np
from code_py.get_dataset import load_split_dataset



def ICanGeneralize(X_test , rho = 1e-05, sigma = 1.05, N = 40):
    '''
    Predict the labels of the dataset based on the optimal values found for the hyper-parameters rho, sigma and N
    in RBF Network

    :param X_test: The dataset consists of the data features only
    :param rho: hyper-parameter, optimal value is given as default
    :param sigma: hyper-parameter, optimal value is given as default
    :param N: hyper-parameter, optimal value is given as default

    :return: prediction for the output value vector -> len(X_test) x 1
    '''
    # seed 
    np.random.seed(7)

    # load the data
    x_train,y_train,x_test,y_test=load_split_dataset(name="data/DATA.csv",fraction=0.744,seed=1942297)

    ext_RBF_net = RBF_Extreme_Opt(x=x_train,y=y_train,x_test=x_test,y_test=y_test,rho=rho,sigma=sigma,N=N,c_flag=True) 
    best_c = ext_RBF_net.Random_Sampling(100)
    _,v_ext_opt,_   = ext_RBF_net.convex_training_error_opt(c=best_c, verbose=False)

    y_predict = ext_RBF_net.prediction(X_test, v=v_ext_opt, c=best_c)
    return y_predict


"""
How to ICanGeneralize
"""
new_imput = np.random.rand(10,2)
out = ICanGeneralize(new_imput)
print(out)
