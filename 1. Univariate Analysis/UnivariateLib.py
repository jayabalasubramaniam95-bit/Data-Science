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



    def fnCentralDedency(quan, descriptive, dataset):
         for colName in quan:
             descriptive[colName]["Mean"]= dataset[colName].mean()
             descriptive[colName]["Median"]=  dataset[colName].median()
             descriptive[colName]["Mode"]=  dataset[colName].mode()[0]
             return descriptive


    
         
         
      
        