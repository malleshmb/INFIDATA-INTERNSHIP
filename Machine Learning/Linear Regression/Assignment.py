import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('exam_marks.csv')

# Display the first few rows of the dataset
print(df.head())

# Visualize the relationship between study hours and exam scores
plt.figure(figsize=(10, 6))
sns.scatterplot(x='hours', y='marks', data=df)
plt.title('Study Hours vs Exam Scores')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.show()
