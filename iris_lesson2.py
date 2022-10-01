import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
X = pd.DataFrame(data=iris.data, columns=['sepal_length', 'sepal_width',
                                          'petal_length', 'petal_width'])

