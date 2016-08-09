# -*- coding: utf-8 -*-
__author__ = 'Shang'
from sklearn import svm
class Models:
    @staticmethod
    def SVC(X, Y):
        """
        @X: features
        @Y: label

        return SVC model
        """
        model = svm.SVC(probability=True)
        model.fit(X, Y)

        return model

