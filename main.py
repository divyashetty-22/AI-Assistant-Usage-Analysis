from src.analysis import (
    load_data,
    dataset_summary,
    task_distribution,
    satisfaction_by_task
)

from src.visualization import (
    plot_task_distribution,
    plot_satisfaction_by_task
)

DATA_FILE = "data/ai_assistant_usage_student_life.csv"

def main():

    print("Loading Dataset...")
    df = load_data(DATA_FILE)

    print("\nDataset Loaded Successfully")
    print(df.head())

    summary = dataset_summary(df)

    print("\nDATASET SUMMARY")
    for key, value in summary.items():
        print(f"{key}: {value}")

    tasks = task_distribution(df)
    satisfaction = satisfaction_by_task(df)

    plot_task_distribution(tasks)
    plot_satisfaction_by_task(satisfaction)

    with open("output/summary_report.txt", "w") as f:
        f.write("AI ASSISTANT USAGE ANALYSIS REPORT\n")
        f.write("="*40 + "\n\n")

        for key, value in summary.items():
            f.write(f"{key}: {value}\n")

        f.write("\nTask Distribution\n")
        f.write(str(tasks))

        f.write("\n\nAverage Satisfaction by Task\n")
        f.write(str(satisfaction))

    print("\nAnalysis Complete")
    print("Results saved in output folder")

if __name__ == "__main__":
    main()
