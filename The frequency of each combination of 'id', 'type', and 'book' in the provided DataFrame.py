import pandas as pd
df = pd.DataFrame( {'id' : [1, 2, 1, 1, 2, 1, 2], 
                    'type' : [10, 15, 11, 20, 21, 12, 14], 
                    'book' : ['C','C++','Java','C','C++','Java','C++']})

print("Original DataFrame:")
print(df)
result = df.groupby(['id', 'type', 'book']).size().unstack(fill_value=0)
print("\nResult:")
print(result)
