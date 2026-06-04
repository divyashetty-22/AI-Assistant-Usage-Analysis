import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def dataset_summary(df):
    summary = {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Average Session Length": round(df["SessionLengthMin"].mean(), 2),
        "Average Prompts": round(df["TotalPrompts"].mean(), 2),
        "Average Satisfaction": round(df["SatisfactionRating"].mean(), 2),
    }
    return summary

def task_distribution(df):
    return df["TaskType"].value_counts()

def satisfaction_by_task(df):
    return df.groupby("TaskType")["SatisfactionRating"].mean().sort_values(ascending=False)

def discipline_distribution(df):
    return df["Discipline"].value_counts()
