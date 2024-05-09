# r w
import pandas as pd

heart_disease_analysis = pd.read_csv("../dataset/heart_disease_uci.csv")
print(heart_disease_analysis.shape)
print(heart_disease_analysis.head(20))
print(heart_disease_analysis.tail(30))
print(heart_disease_analysis.info)
print(heart_disease_analysis["age"].mean())
print(heart_disease_analysis["age"].median())
print(heart_disease_analysis["age"].mode())
print("Max", heart_disease_analysis["age"].max())
print("Min", heart_disease_analysis["age"].min())
print("Std",heart_disease_analysis['age'].std());
print('[Age]-[trestbps]-mean',heart_disease_analysis[["age" ,'trestbps']].mean());
print('[Age]-[trestbps]-median',heart_disease_analysis[["age" ,'trestbps']].median());
print("All-data",heart_disease_analysis.describe())
print(heart_disease_analysis['sex']);
print('unique-data',heart_disease_analysis['sex'].unique())
print(heart_disease_analysis['dataset'].unique());
print(heart_disease_analysis['ca'].unique());
print(heart_disease_analysis['oldpeak']);
print(heart_disease_analysis.describe(include="all"));
print(heart_disease_analysis.describe(include='O'));
print(heart_disease_analysis['dataset'].value_counts());



