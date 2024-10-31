import pandas as pd
import csv

# Path to the raw dataset
data_path = "./data/fra.txt"

input_texts = []
target_texts = []

with open(data_path, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

for line in lines:
    try:
        input_text, target_text, _ = line.split("\t") 
        input_texts.append(input_text)
        target_texts.append(target_text)
    except ValueError:
        print(f"Skipping line due to split error: {line}")

df = pd.DataFrame({
    'english': input_texts,  
    'french': target_texts 
})

# Save the DataFrame to a CSV file
output_path = "./data/data.csv" 
df.to_csv(output_path, index=False, encoding='utf-8', quoting=csv.QUOTE_MINIMAL)

print(f"Data saved to {output_path}")
