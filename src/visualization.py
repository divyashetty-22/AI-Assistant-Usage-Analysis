import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("output", exist_ok=True)

def plot_task_distribution(task_counts):
    plt.figure(figsize=(8,5))
    sns.barplot(x=task_counts.index, y=task_counts.values)
    plt.title("Task Type Distribution")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("output/task_type_distribution.png")
    plt.close()

def plot_satisfaction_by_task(data):
    plt.figure(figsize=(8,5))
    sns.barplot(x=data.index, y=data.values)
    plt.title("Average Satisfaction by Task")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.savefig("output/satisfaction_by_task.png")
    plt.close()
