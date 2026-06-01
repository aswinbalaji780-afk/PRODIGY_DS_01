import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\aswin\OneDrive\Desktop\Practice\PRODIGY_DS_TASK\data\train.csv")

plt.figure(figsize=(10,6))

sns.histplot(df['Age'], bins=20, kde=True)

plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Count")

plt.show()


plt.figure(figsize=(8,5))

sns.countplot(x='Sex', data=df)

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.show()
