import numpy as np
import pandas as pd

df = pd.read_excel('CourseEvaluation.xlsx')
Data_without_SID = df.iloc[:, 1:].values
num_of_key= int(input("Enter Number of keys : "))

clusters =[]
clusters = {
    i+1: df.iloc[:, 1:].sample(1)
    for i in range(num_of_key)
}

print(clusters)
clusters=list(clusters)

clusters_table = [[] for i in range(num_of_key)]
temp_clusters_table=[[] for i in range(num_of_key)]


while(True):
    temp_clusters_table = [[] for i in range(num_of_key)]
    temp_clusters_table=clusters_table.copy()
    clusters_table = [[] for i in range(num_of_key)]

    for i in range(0, len(Data_without_SID)):
        temp_Distance = []
        for j in range(0, len(clusters)):
            Euclidean_Distance = np.linalg.norm(np.array(Data_without_SID[i]) - np.array(clusters[j]))
            temp_Distance.append(Euclidean_Distance)
        min = np.argmin(np.array(temp_Distance))
        clusters_table[min].append(Data_without_SID[i])

    #print(clusters)
    print('---------')
    for i in range(0, len(temp_clusters_table)):
        print('The length of cluster in temp_clusters_table',i,' : ',len(temp_clusters_table[i]))
    print(temp_clusters_table)
    print('------')
    for i in range(0, len(clusters_table)):
        print('The length of cluster in clusters_table',i,' : ',len(clusters_table[i]))
    print(clusters_table)
    print('////////////////////////////////////////////////////////////////////////////////////////////////')
    if  (pd.DataFrame(clusters_table).equals(pd.DataFrame(temp_clusters_table))):
           break

    else:
                 clusters = []
                 for i in range(len(clusters_table)):
                     if clusters_table[i]==[]:
                         continue
                     else:
                        clusters.append(np.array(clusters_table[i]).mean(axis=0))
