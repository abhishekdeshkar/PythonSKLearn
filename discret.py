from sklearn.preprocessing import KBinsDiscretizer

X = [[-2,1,-4,-1],[-1,2,-3,-0.5],[0,3,-2,0.5],[1,4,-1,-2]]
est = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform') 
est.fit(X)
# print(est)
Xt = est.transform(X)
print(Xt)