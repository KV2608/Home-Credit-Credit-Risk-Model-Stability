from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier

def train_lgbm(X, y):
    model = LGBMClassifier()
    model.fit(X, y)
    return model
