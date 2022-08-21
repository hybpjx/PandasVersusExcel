import pandas as pd

df= pd.DataFrame({
    "id":[1,2,3],
    "name":[1,2,3]
                  })


# 指定某个字段为索引 不然会默认多出一行作为索引
df.set_index("id")

# index=False 去除索引
df.to_excel("a.xlsx",index=False)

