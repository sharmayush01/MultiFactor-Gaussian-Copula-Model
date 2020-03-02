import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
import random
import math
from scipy.stats import norm

# PDMatrix_df = pd.read_excel('py_v01.xlsx')
data = pd.read_excel('data.xlsx')
TotalDefault = []
Uvector = []
Xvector = []
Zvector = []
PDCOL = []
defaultVector = []
numOfFactor = 5
numOfRanking = 6
rankingCol = data['Unnamed: 1'][3:]
FactorImportanceVector = np.zeros((100,numOfFactor))
SMatrix = np.zeros((100,numOfFactor)) 
horizon = 5 # horizon === time and default value is 5 years
# feature default percetsn
F1 = 0.6
F2 = 0.25
F3 = 0.10
F4 = 0.03
F5 = 0.02
TotalDefautls = [] # have value 100_000
df = [] # emplty data frame
PDMatrix = []



# calculate probablity default
# def createPDMatrix():
#     print("pdmat rix print", data.iloc[3:9,-7:])
#     matrix = data.iloc[3:9,-7:].to_numpy()
    
#     return matrix

##populate the martrix random column vectors
def populateMatrix():
    # print(random.randint(1,6))
    
    pass

# calculate f1 f2 factors 
# // get user input for number of features and horizon(time)
def generateFactorsImportance():
    for i in range(0,100):
        FactorImportanceVector[i][0] = random.random()*math.sqrt(F1)
        FactorImportanceVector[i][1] = random.random()*math.sqrt(F2)
        FactorImportanceVector[i][2] = random.random()*math.sqrt(F3)
        FactorImportanceVector[i][3] = random.random()*math.sqrt(F4)
        FactorImportanceVector[i][4] = random.random()*math.sqrt(F5)


# generate factor matrix
def generrateFactorMatrix():
    pass

# generate s matrix
def generateSMatrix():
    s1 = norm.ppf(random.random())
    s2 = norm.ppf(random.random())
    s3 = norm.ppf(random.random())
    s4 = norm.ppf(random.random())
    s5 = norm.ppf(random.random())
    for i in range(0, 100):
        SMatrix[i][0] = s1 
        SMatrix[i][1] = s2 
        SMatrix[i][2] = s3 
        SMatrix[i][3] = s4 
        SMatrix[i][4] = s5 

# create z columns:
def createZColumn():
    for i in range(0,100):
        Zvector.append(norm.ppf(random.random()))

#create columns X 
def createXColumn():
    for i in range(0,100):
        factorList = FactorImportanceVector[i]
        sList = SMatrix[i]
        tmp = sum([a*b for a,b in zip(factorList,sList)])
        sq_factorList = sum(factorList ** 2)
        value = tmp + Zvector[i] * math.sqrt(sq_factorList)     
        Xvector.append(value)

#create u coloumns
def createUColumn():
    for i in Zvector:
        Uvector.append(norm.cdf(i))
    
# create probability default column
def createPDColumn():
    # PDMatrix = createPDMatrix()
    import pandas as pd
    df = pd.read_excel('./py_v01.xlsx').to_numpy()
   
    for i in range(3,103):
        val = 0
        r = rankingCol[i]
        for j in range(0,6):
            if r == df[j][1]:
                val = df[j, horizon+1]
                # print(df[i][horizon+1] / 100)\
        PDCOL.append(val/100)
        
       
        
   


#create default column vector probability == 0
def createDefaultColumnvector():
    print(type(Uvector), len(Uvector))
    print(type(PDCOL), len(PDCOL))
    for i in range(100):
        if Uvector[i] < PDCOL[i]:
            defaultVector.append(1)
        else:
            defaultVector.append(0)

    print(defaultVector)
# calculate total default and store them in array , than plot them 
def calculateTotalDefault():
    df = pd.read_excel('./py_v01.xlsx').to_numpy()
    lst = ['AAA','AA','A','BBB','BB','B']
    for i in range(10):
        TotalDefault.append(sum(defaultVector))
        
        print(random.choice(lst))
        rankingCol[0] = random.choice(lst)
        print(rankingCol)

if __name__ == "__main__":
    #  run 100_000 times and then plot histogram.
    # horizon = input("please enter horizon : ")
    # numOfFactor = input("please enter number of factors : ")
    # PDMatrix = pd.read_excel('py_v01.xlsx')
    # data = pd.read_excel('data.xlsx')
    generateFactorsImportance()
    generateSMatrix()
    createZColumn()
    createXColumn()
    createUColumn()
    createPDColumn()
    createDefaultColumnvector()
    calculateTotalDefault()
    print(TotalDefault)