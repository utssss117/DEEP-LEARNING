import os

# Path where your project files are
path = r"C:\Users\uttu2\OneDrive\Desktop\coding\deep learning\customer churn prediction"

# List all files in that folder
files = os.listdir(path)

# Show all files
print("📂 Files in folder:")
for f in files:
    print("  -", f)

# Check if Churn_Modelling.csv exists
csv_path = os.path.join(path, "Churn_Modelling.csv")
print("\n✅ File exists?" , os.path.exists(csv_path))
