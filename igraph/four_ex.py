from igraph import * 
import matplotlib.pyplot as plt
import numpy as np

g = Graph.Read_GML("wikipedia.gml")
pagerank = g.pagerank()
wk = g.community_walktrap()
#print modularity(wk)
#print membership(wk)
cl = wk.as_clustering()
member = cl.membership;
indexPageRankMax = pagerank.index(max(pagerank))
indexPageRankMin = pagerank.index(min(pagerank))
print "AMB COMMUNITY WALKTRAP"
print  "El node amb MES pagerank es: " + str(indexPageRankMax) + " el valor es: " + str(max(pagerank)) 
print  "Pertany a la communitat: " + str(member[indexPageRankMax])
print "El nombre d'elements a la comunitat del node amb MES pageRank es: " + str(member.count(member[indexPageRankMax]))


print  "El node amb MENYS pagerank es: " + str(indexPageRankMin) + " el valor es: " + str(min(pagerank)) 
print  "Pertany a la communitat: " + str(member[indexPageRankMin])
print "El nombre d'elements a la comunitat del node amb MENYS pageRank es: " + str(member.count(member[indexPageRankMin]))
l = [0] * (max(member)+1);

for i in member:
	l[i] = l[i]+1;


fig = plt.figure()
ax = fig.add_subplot(111)

## necessary variables
ind = np.arange(len(l))                # the x locations for the groups
width = 0.20                      # the width of the bars

## the bars
rects1 = ax.bar(ind, l, width)

#plt.hist2d(np.asarray(range(0,(max(member)+1))), l)
plt.show()
#for num in range(1,max(membership(wk))):


# calculate dendrogram
g2 = g.community_edge_betweenness()
member = g2.membership
print "AMB COMMUNITY_EDGE_BETWEENNESS"
print  "El node amb MES pagerank es: " + str(indexPageRankMax) + " el valor es: " + str(max(pagerank)) 
print  "Pertany a la communitat: " + str(member[indexPageRankMax])
print "El nombre d'elements a la comunitat del node amb MES pageRank es: " + str(member.count(member[indexPageRankMax]))


print  "El node amb MENYS pagerank es: " + str(indexPageRankMin) + " el valor es: " + str(min(pagerank)) 
print  "Pertany a la communitat: " + str(member[indexPageRankMin])
print "El nombre d'elements a la comunitat del node amb MENYS pageRank es: " + str(member.count(member[indexPageRankMin]))


