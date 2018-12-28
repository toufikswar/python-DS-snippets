import numpy as np
import pandas as pd

textfile = 'raw data/dob_job_application_filings_subset.csv'

df = pd.read_csv(textfile)


print(df.describe())