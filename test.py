from sklearn.metrics import ndcg_score, dcg_score
import numpy as np

true = np.asarray([[2, 4, 1, 1, 1]])
relevance = np.asarray([[2, 5, 2, 3, 1]])

print(ndcg_score(true, relevance))