import math
import os
import random
import re
import sys
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)


LR = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr')

LR.fit(X_train, y_train)
predictions = LR.predict(X_test)




