import pandas as pd
print(pd.read_csv("reddit_posts.csv"))

x = {"Name":["Surya","Ponni"],"Age":[21,23],"City":["Coimbatore","Coimbatore"]}
res = pd.DataFrame(x)
print(res)