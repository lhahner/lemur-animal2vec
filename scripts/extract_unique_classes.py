import pandas as pd

# Read the pickle file
df = pd.read_pickle("../data/lbl/labels_from_txt.pkl")

# Iterate over all columns of the data frame and print
for col in df:
    print("Column: ", col, df[col].unique())