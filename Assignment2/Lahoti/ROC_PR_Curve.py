
# PR Curve
import matplotlib as mpl
mpl.use('TkAgg')
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

y_true = [0, 1, 0, 0, 1, 0, 1, 1, 0, 1]
y_probas = [1, 2, 3.2, 3.4, 4.3, 4.7, 5.3, 6, 7, 9]
fpr, tpr, thresholds = metrics.roc_curve(y_true, y_probas, pos_label=0)

plt.plot(tpr,fpr)
plt.show()

auc = np.trapz(fpr,tpr)
print('AUC:', auc)

from sklearn.metrics import precision_recall_curve
precision, recall, _ = precision_recall_curve(y_true, y_probas)

from sklearn.metrics import average_precision_score
average_precision = average_precision_score(y_true, y_probas)

plt.step(recall, precision, color='b', alpha=0.2, where='post')
plt.fill_between(recall, precision, step='post', alpha=0.2,
                 color='b')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
          average_precision))
plt.show()
