import numpy as np
import pandas as pd
import collections

data = pd.read_csv("data.csv")

classes = data['class_type']
print(collections.Counter(list(classes)))