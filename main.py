import pandas as pd

df = pd.read_table('human_plasmids.tsv')
pd.set_option('display.max_columns', None)
print(df)

df_filtered = df.dropna(subset=['IsolationSource_BIOSAMPLE'])
print(df_filtered)

healthy = df_filtered[df_filtered["IsolationSource_BIOSAMPLE"].str.contains("healthy")]
print(healthy)
healthy.to_csv("healthy.csv", index=False, header=False)

sick = df_filtered[df_filtered["IsolationSource_BIOSAMPLE"].str.contains("healthy") == False]
print(sick)
sick.to_csv("sick.csv", index=False, header=False)



