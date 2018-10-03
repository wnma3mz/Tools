# coding: utf-8

from sklearn import svm, grid_search
from sklearn.metrics import classification_report
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split

digits = load_digits()

train_X, test_X, train_y, test_y = train_test_split(
    digits.data, digits.target, test_size=0.25, random_state=25)
# 参数设定
# parameter_grid = [
#     {'kernel': ['linear'], 'C': [1, 10, 50, 600]},
#     {'kernel': ['poly'], 'degree': [2, 3]},
#     {'kernel': ['linear', 'rbf'], 'gamma': [
#         0.01, 0.001], 'C': [1, 10, 50, 600]},
# ]
parameter_grid = [
    {'kernel': ['linear', 'rbf'], 'gamma': [0.01, 0.001],
        'C': [1, 10, 50, 600], 'degree': [2, 3]},
]
# 评价指标
"""
['accuracy', 'adjusted_mutual_info_score', 'adjuste
d_rand_score', 'average_precision', 'completeness_score', 'e
xplained_variance', 'f1', 'f1_macro', 'f1_micro', 'f1_sample
s', 'f1_weighted', 'fowlkes_mallows_score', 'homogeneity_sco
re', 'mutual_info_score', 'neg_log_loss', 'neg_mean_absolute
_error', 'neg_mean_squared_error', 'neg_mean_squared_log_err
or', 'neg_median_absolute_error', 'normalized_mutual_info_sc
ore', 'precision', 'precision_macro', 'precision_micro', 'pr
ecision_samples', 'precision_weighted', 'r2', 'recall', 'rec
all_macro', 'recall_micro', 'recall_samples', 'recall_weight
ed', 'roc_auc', 'v_measure_score']

"""
metrics = ['accuracy', 'recall_weighted']

for metric in metrics:
    print('当前评价指标是: {}'.format(metric))

    classifier = grid_search.GridSearchCV(
        svm.SVC(C=1), parameter_grid, cv=5, scoring=metric)
    classifier.fit(train_X, train_y)

    # 模型得分
    for params, avg_score, _ in classifier.grid_scores_:
        print('{}: avg_score: {}'.format(params, round(avg_score, 3)))

    print('最高分参数：{}'.format(classifier.best_params_))
    y_pred = classifier.predict(test_X)

    print(classification_report(test_y, y_pred))
