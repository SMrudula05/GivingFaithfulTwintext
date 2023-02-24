import pandas as pd
import numpy as np 
def combine_telemetry_data(data1,data2):
  combined_data = pd.concat([data1,data2],axis=1,sort=False).fillna(0)
  return combined_data
  data1 = pd.DataFrame(np.random.randint(0,100,size=(8,4)),columns=list('ABCD'))
  data2 = pd.DataFrame(np.random.randint(0,100,size=(8,4)),columns=list('EFGH'))
  combined_data = combine_telemetry_data(data1,data2)
  print(combined_data)

  
  
  