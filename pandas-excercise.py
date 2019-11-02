import numpy as np
import pandas as pd

sr = pd.read_csv('c:\python37\doc\insurance.csv').head(5)

sr.to_string()
#print(sr)
print(sr.age, sr.children, sr.charges)

