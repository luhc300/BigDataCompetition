from sklearn.model_selection import GridSearchCV
class Classifier:
    def __init__(self):
        self._clf = None
        self._target = None
        self._is_tune = False
        self._tune_params = None
        self._is_prob = True

    def set_attr(self, attr):
        if "target" in attr:
            target = attr.get("target")
            self._target = target
        if "is_tune" in attr:
            is_tune = attr.get("is_tune")
            self._is_tune = is_tune
        if "tune_params" in attr:
            tune_params = attr.get("tune_params")
            self._tune_params = tune_params
        if "is_prob" in attr:
            is_prob = attr.get("is_prob")
            self._is_prob = is_prob

    def train(self, data):
        target = self._target
        X = data.drop(target,axis=1)
        y = data[target]
        if self._is_tune:
            self.param_tuning(data)
        self._clf.fit(X,y)

    def param_tuning(self, data):
        target = self._target
        X = data.drop(target, axis=1)
        y = data[target]
        grid = GridSearchCV(self._clf, cv=3, n_jobs=2, param_grid=self._tune_params)
        grid.fit(X,y)
        self._clf = grid.best_estimator_

    def cross_validation(self, data):
        pass

    def predict(self,data):
        is_prob = self._is_prob
        if is_prob:
            result = self._clf.predict_proba(data)[:,1]
        else:
            result = self._clf.predict(data)
        return result

