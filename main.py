# -*- coding: utf-8 -*-
__author__ = 'Shang'


from models import Models
from copy import deepcopy
import pickle



def main():
    X_train = []
    Y_train = []
    X_test = []
    userID = []

    with open('./util/train_f.pkl', 'r') as f:
        features = pickle.load(f)
        X_train = deepcopy(features[:-2])
        Y_train = deepcopy(features[-1])

    with open('./util/test_f.pkl', 'r') as f:
        features = pickle.load(f)
        X_test = deepcopy(features[:-1])
        userID = deepcopy(features[-1])

    svc = Models.SVC(X_train, Y_train)
    result = svc.predict_proba(X_test)

    print "Saving ..."
    with open('submission.txt', 'w') as f:
        for idx, r in enumerate(result):
            s = userID[idx] + ',' + str(r[1]) + '\n'
            f.write(s)


if __name__ == '__main__':
    main()
    print "Done!"