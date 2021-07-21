# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 10:12:04 2021

@author: Utilisateur
"""

import pandas as pd
import numpy as np

# tansform the xlsx file to dataframe
df_web = pd.read_excel("web.xlsx")
df_erp = pd.read_excel("erp.xlsx")
df_liaison = pd.read_excel("liaison.xlsx")

df_web_origin, df_erp_origin, df_liaison_origin = df_web, df_erp, df_liaison

print(df_web.head())
print(df_web.info())
print(df_web.describe())


df_1 = df_web.merge(df_liaison, left_on='sku', right_on='id_web')

df_1_origin = df_1

df_1.drop_duplicates()

