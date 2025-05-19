import pandas as pd
import os
from datetime import timedelta

rows = []
data_dir = '../data'  # Update to your actual directory

for file in os.listdir(data_dir):
    if file.endswith('.selections.txt'):
        path = os.path.join(data_dir, file)

        # Extract base audio filename
        audio_filename = file.replace('.Table.1.selections.txt', '.wav')

        # Read file — tab-separated
        df = pd.read_csv(path, sep='\t')

        # Drop duplicates from Spectrogram/Waveform pairs (every second row)
        df = df.drop_duplicates(subset=["Begin Time (s)", "End Time (s)", "Annotation"])

        for _, row in df.iterrows():
            rows.append({
                'Name': row['Annotation'],
                'AudioFile': audio_filename,
                'StartRelative': timedelta(seconds=float(row['Begin Time (s)'])),
                'EndRelative': timedelta(seconds=float(row['End Time (s)'])),
                'Focal': True  # Or use any rule you want
            })

# Create dataframe
output_df = pd.DataFrame(rows)

# Save as pickle
output_df.to_pickle('../data/labels_from_txt.pkl')
print("✅ Saved: labels_from_txt.pkl with", len(output_df), "entries.")
