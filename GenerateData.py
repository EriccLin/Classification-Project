# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 00:35:07 2018

@author: linjiayuan
"""
import numpy as np
import csv

rng = np.random.RandomState(8)
sex = (1.1 * rng.rand(100) > 0.5 ).astype(int)
drink = ( rng.rand(100) > 0.5 ).astype(int)
smoke = ( rng.rand(100) > 0.5 ).astype(int)
eat_betel_nuts = ( rng.rand(100) > 0.5 ).astype(int)
marriage = (rng.rand(100) < 0.7).astype(int)+(rng.rand(100) < 0.7).astype(int)
num_children = ( 3 * rng.rand(100) ).astype(int) + ( 8 * rng.rand(100) <= 1).astype(int)

sex2 = [(lambda x :'female' if x == 1 else 'male')(x) for x in sex]
drink2 = [(lambda x : True if x == 1 else False )(x) for x in drink]
smoke2 = [(lambda x : True if x == 1 else False )(x) for x in smoke]
eat_betel_nuts2 = [(lambda x : True if x == 1 else False )(x) for x in eat_betel_nuts]

def repMarriage(x):
    if x == 2:
        return 'marriaged'
    elif x == 1:
        return 'divorced'
    else:
        return 'unmarried'

marriage2 = [repMarriage(x) for x in marriage]

data = np.c_[sex2, drink2, smoke2, eat_betel_nuts2, marriage2, num_children]

target = ((sex + marriage + num_children)**2 + 20 * rng.rand(100) + 50 - 2 * (drink + smoke + eat_betel_nuts)) > 76

feature_names = ['sex','drink','smoke','eat_betel_nuts','marriage','num_children']
target_names = ['Age_Of_Death>= HALE']

with open('mydata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['unique_id']+feature_names + target_names)
    for index, row in enumerate(np.c_[data, target]):
        writer.writerow(np.r_[[index],row])
        
