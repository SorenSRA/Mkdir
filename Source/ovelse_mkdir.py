# -*- coding: utf-8 -*-
import os

# Opsaetning og import af egne moduler
import sys

sys.path.append(r"C:\Filkassen\PythonMm\VSCode_projects\LIFEOpsaetning")
import partneroversigt as po


path_root_dir = r"C:\Temp\TestDir"

root_dir = "Bilag2023"

for sub_dir in po.cc_dirs:
    new_dir = os.path.join(path_root_dir, root_dir, sub_dir)

    os.makedirs(new_dir)
