# Student Performance Analysis Project

import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Create visualization folder
try:
    os.makedirs("visualizations", exist_ok=True)
except Exception as e:
    print("Error creating visualization folder:", e)


# Step 2: Load Dataset
try:
    df = pd.read_csv("data/student_data.csv")
    print("Dataset loaded successfully\n")
except FileNotFoundError:
    print("Error: Dataset file not found.")
    exit()
except Exception as e:
    print("Error loading dataset:", e)
    exit()


# Step 3: Data Exploration
print("First 5 rows of dataset:\n")
print(df.head())

print("\nDataset Information:\n")
print(df.info())

print("\nBasic Statistics:\n")
print(df.describe())


# Step 4: Data Cleaning
# Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Drop rows if any missing values exist
df = df.dropna()


# Step 5: Data Analysis

# Calculate average marks for each student
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Top student
top_student = df.loc[df["Average"].idxmax()]

print("\nTop Performing Student:")
print(top_student)

# Subject averages
subject_avg = df[["Math", "Science", "English"]].mean()

print("\nAverage Marks per Subject:")
print(subject_avg)


# Step 6: Visualization 1
try:
    subject_avg.plot(kind="bar")

    plt.title("Average Marks per Subject")
    plt.ylabel("Marks")
    plt.xlabel("Subjects")

    plt.tight_layout()
    plt.savefig("visualizations/subject_average.png")
    plt.close()

    print("\nChart 1 saved: subject_average.png")

except Exception as e:
    print("Error creating subject average chart:", e)


# Step 7: Visualization 2
try:
    df.plot(x="Name", y="Average", kind="bar")

    plt.title("Student Average Scores")
    plt.ylabel("Marks")
    plt.xlabel("Student Name")

    plt.tight_layout()
    plt.savefig("visualizations/student_average.png")
    plt.close()

    print("Chart 2 saved: student_average.png")

except Exception as e:
    print("Error creating student chart:", e)


# Step 8: Insights

print("\n-------- Insights --------")

highest_subject = subject_avg.idxmax()
lowest_subject = subject_avg.idxmin()

print(f"Highest scoring subject on average: {highest_subject}")
print(f"Lowest scoring subject on average: {lowest_subject}")
print(f"Top performing student: {top_student['Name']}")

print("\nProject analysis completed successfully!")