import pandas as pd
import numpy as np

data = {
    "Name": ["Alice","bob","Charlie","David","Eve"],
    "Age": [25, 30, 22, 29, 27],
    "Score": [85, 90, 78, 88, 92]
}
df = pd.DataFrame(data)

print("DataFrame:\n", df)

age_column = df["Age"]
print("\n Retrieved Column - Age:\n,age_column")

summary = df.describe()
print("\n Summary Statistics Of DataFrame:\n , summary")

mean_values = df.select_dtypes(include = [np.number]).mean()
std_values = df.select_dtypes(include = [np.number]).std()

print("\n Mean Values:\n,mean_values")
print("\nStandard Deviation Values:\n,std_values")





