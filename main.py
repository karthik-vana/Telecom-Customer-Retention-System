'''
In this file i will going to load the data and other ml pipeline
techniques do  which are needed
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
import sklearn
import warnings
warnings.filterwarnings('ignore')

from log_code import setup_logging
logger = setup_logging('main')
from EDA import EDA_Analysis




class CUSTOMER_RETENTION_SYSTEM:

    def __init__(self,path):
        try:
            self.path = path
            self.df = pd.read_csv(self.path)

            logger.info(self.df.sample(5))
            logger.info(self.df.shape)
            logger.info(self.df.columns.tolist())
            logger.info(self.df.info())
            logger.info(self.df.isnull().sum())
            logger.info(self.df.describe())

        except Exception as e:
            error_type,error_msg,error_line = sys.exc_info()
            logger.info(f'error in line no : {error_line.tb_lineno} : due to {error_msg}')

    def EDA(self):
        try:
            self.df = EDA_Analysis(self.df)



        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            logger.info(f'error in line no : {error_line.tb_lineno} : due to {error_msg}')


if __name__ == '__main__':
    try:
        obj = CUSTOMER_RETENTION_SYSTEM('C:\\Users\\Karthik\\Downloads\\Customer Retention Prediction System\\WA_Fn-UseC_-Telco-Customer-Churn.csv')
        obj.EDA()

    except Exception as e:
        error_type, error_msg, error_line = sys.exc_info()
        logger.info(f'error in line no : {error_line.tb_lineno} : due to {error_msg}')









