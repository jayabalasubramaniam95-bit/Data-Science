import pandas as pd
class Univariate():
    def fnQuanQuali(dataset):
        quan=[]
        quali =[]
        for colName in dataset.columns:
            if(dataset[colName].dtype =='O'):
                quali.append(colName)
            else:
                quan.append(colName)
    
        return quan,quali



    def fnCentralDedency(quan, dataset):
        import pandas as pd
        descriptive = pd.DataFrame(index=["Mean", "Median", "Mode", "Q1:25%", "Q2:50%", "Q3:75%","Max", "IQR", "1.5Rule","Lesser","Greater","Min","Max","Skew","Kurtosis",'Var', 'StdVar'], columns=quan)
        for colName in quan:            
             descriptive[colName]["Mean"]= dataset[colName].mean()
             descriptive[colName]["Median"]=  dataset[colName].median()
             descriptive[colName]["Mode"]=  dataset[colName].mode()[0]
             descriptive[colName]["Q1:25%"]=  dataset.describe()[colName]["25%"]
             descriptive[colName]["Q2:50%"]= dataset.describe()[colName]["50%"]
             descriptive[colName]["Q3:75%"]= dataset.describe()[colName]["75%"]             
             descriptive[colName]["Max"]=  dataset.describe()[colName]["max"]
             descriptive[colName]["IQR"]=  descriptive[colName]["Q3:75%"] - descriptive[colName]["Q1:25%"]
             descriptive[colName]["1.5Rule"] = 1.5 * descriptive[colName]["IQR"]
             descriptive[colName]["Lesser"] =descriptive[colName]["Q1:25%"]-descriptive[colName]["1.5Rule"]
             descriptive[colName]["Greater"] = descriptive[colName]["Q3:75%"]+ descriptive[colName]["1.5Rule"]
             descriptive[colName]["Min"]=dataset[colName].min()
             descriptive[colName]["Max"]=dataset[colName].max()
             descriptive[colName]["Skew"]=dataset[colName].skew()
             descriptive[colName]["Kurtosis"]=dataset[colName].kurtosis()
             descriptive[colName]["Var"]=dataset[colName].var()
             descriptive[colName]["StdVar"]=dataset[colName].std()
        return descriptive


    def fnfreTable(colName, dataset):
        freqTable= pd.DataFrame( columns=["Values","Frequency", "Relative Frequency", "Cusum Frequency"])
        freqTable["Values"] = dataset[colName].value_counts().index
        freqTable["Frequency"] = dataset[colName].value_counts().values
        tableLength = len(freqTable["Values"])
        freqTable["Relative Frequency"]= freqTable["Frequency"]/tableLength
        freqTable["Cusum Frequency"]= freqTable["Relative Frequency"].cumsum()
        return freqTable

    def fnfindOutlier(quan, descriptive):
        lesser=[]
        greater=[]
        for colName in quan:
            if(descriptive[colName]["Min"]<descriptive[colName]["Lesser"]).any():
                lesser.append(colName)
            if(descriptive[colName]["Max"]>descriptive[colName]["Greater"]).any():
                greater.append(colName)
        return lesser,greater

    def fnReplaceOutlier(lesser, greater, dataset,descriptive):
        for colName in lesser:
            dataset[colName][dataset[colName]<descriptive[colName]["Lesser"]]= descriptive[colName]["Lesser"]
        for colName in greater:
            dataset[colName] [dataset[colName]>descriptive[colName]["Greater"]] = descriptive[colName]["Greater"]
        return dataset
    
    


    
         
         
      
        