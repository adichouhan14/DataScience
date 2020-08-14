import pandas as pd
import numpy as np

dict={"name":["ravi","tarun","mayur"],"salary":[10000,20000,15000],"experience":[1,2,3],
      "joining year":[2000,2001,2002]}

x=pd.DataFrame(dict)
print(x["salary"].mean())