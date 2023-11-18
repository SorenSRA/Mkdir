# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:23:05 2023

@author: soren bhy
"""

import os

sub_dirs = ['CC2_Travel',
            'CC3_ExternalAss',
            'CC4_DurGoods',
            'CC5_LandPurch',
            'CC6_Consume',
            'CC7_OtherCost'
            ]

path_root_dir = r'C:\SraDiverse\TestDir'

root_dir = 'Bilag2023'

for sub_dir in sub_dirs:
    
    new_dir = os.path.join(path_root_dir, root_dir, sub_dir)
    
    os.makedirs(new_dir)