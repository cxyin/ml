from numpy import *

def loadDataset(filename):
	dataMat = []
	fr = open(fileName)
	for line in fr.readlines():
		curLine = line.strip().split('\t')
		fltLine = map(float, curLine)
		dataMat.append(fltLine)
	return dataMat

def binSplitDataSet(dataSet, feature, value):
	mat0 = dataSet[nonzero(dataSet[:,feature] > value)[0], :][0]
	mat1 = dataSet[nonzero(dataSet[:,feature] <= value)[0], :][0]
	return mat0, mat1


def createTree(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4)):
	feat, val = chooseBestSplit(dataSet, leaf, errType, ops)
	if feat == None: return val
	retTree = {}
	retTree['spInd'] = feat
	retTree['spVal'] = val
	lSet, rSet = binSplitDataSet(dataSet, feat, val)
	retTree['left'] = createTree(lSet, leafType, errType, ops)
	retTree['right'] = createTree(rSet, leafType, errType, ops)
	return retTree

def regLeaf(dataSet):
	return mean(dataSet[:-1])

def regErr(dataSet):
	return var(dataSet[:,-1] * shape(dataSet))[0]

def chooseBestSplit(dataSet, leafType=regLeaf, errType=regErr, ops=(1, 4)):
	tolS = ops[0];tolN = ops[1]
	if len(set(dataSet[:, -1].T.tolist()[0])) == 1:
		return None, leafType(dataSet)
	m,n = shape(dataSet)
	S = errType(dataSet)
	bestS = inf; bestIndex = 0; bestValue = 0
	for featIndex in range(n-1):
		for splitVal in set(dataSet[:, featIndex]):
			mat0, mat1 = binSplitDataSet(dataSet, featIndex, splitVal)
			if (shape(mat0)[0] < tol)
