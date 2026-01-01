# pyclean

A minimal Python package (RAP4MADS session 5) that standardizes DataFrame column names.

## Usage

```python
import pandas as pd
from pyclean import clean_names

df = pd.DataFrame({"First Name": ["Ada"], "Last.Name": ["Lovelace"]})
print(clean_names(df).columns.tolist())
Run tests
pytest
E0F
