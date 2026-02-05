# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 22:20:10 2026

@author: Zukisa Matshazini
"""

import subprocess
file = "app.py"
#file = "app_plots.py"
#file = "app_profiler.py"
#file = "app_profiler_menus.py"
subprocess.Popen(
    ["streamlit", "run", file], shell=True
)