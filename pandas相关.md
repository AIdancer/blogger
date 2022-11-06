### 几种pandas DataFrame的filter方法
```
  newdf = df[(df.origin == "JFK") & (df.carrier == "B6")]
  
  newdf = df.query('origin == "JFK" & carrier == "B6"')
  
  newdf = df.loc[(df.origin == "JFK") & (df.carrier == "B6")]
  
  df.loc[df.index[0:5],["origin","dest"]]
  
  newdf = df.loc[(df.origin == "JFK") | (df.origin == "LGA")]
  newdf = df[df.origin.isin(["JFK", "LGA"])]
  
  newdf = df.loc[(df.origin != "JFK") & (df.carrier == "B6")]
  
  newdf = df[~((df.origin == "JFK") & (df.carrier == "B6"))]
  
  newdf = df[df.origin.notnull()]
  
  df[df['var1'].str[0] == 'A']
  
  df.rename(columns={'var1':'var 1'}, inplace = True)
```
