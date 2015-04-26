from igraph import *
import matplotlib.pyplot as plt
import random

random.seed(1234)
g2 = Graph.Watts_Strogatz(1, 2000, 4, 0, bool(1))
x = g2.average_path_length();
y = g2.transitivity_avglocal_undirected()

g2 = Graph.Watts_Strogatz(1, 2000, 4, 0.0001, bool(1))
trans1 = g2.transitivity_avglocal_undirected()/y
shrt1 = g2.average_path_length()/x

g2 = Graph.Watts_Strogatz(1, 2000, 4, 0.0005, bool(1))
trans2 = g2.transitivity_avglocal_undirected()/y
shrt2 = g2.average_path_length()/x


g2 = Graph.Watts_Strogatz(1, 2000, 4, 0.001, bool(1))
trans3 = g2.transitivity_avglocal_undirected()/y
shrt3 = g2.average_path_length()/x

g2 = Graph.Watts_Strogatz(1, 2000, 4, 0.005, bool(1))
trans4 = g2.transitivity_avglocal_undirected()/y
shrt4 = g2.average_path_length()/x


g2 = Graph.Watts_Strogatz(1, 2000, 4, 0.01, bool(1))
trans5 = g2.transitivity_avglocal_undirected()/y
shrt5 = g2.average_path_length()/x

g2 = Graph.Watts_Strogatz(1, 2000, 4, 0.05, bool(1))
trans6 = g2.transitivity_avglocal_undirected()/y
shrt6 = g2.average_path_length()/x


g2 = Graph.Watts_Strogatz(1, 2000, 4, 0.1, bool(1))
trans7 = g2.transitivity_avglocal_undirected()/y
shrt7 = g2.average_path_length()/x

g2 = Graph.Watts_Strogatz(1, 2000, 4, 0.5, bool(1))
trans8 = g2.transitivity_avglocal_undirected()/y
shrt8 = g2.average_path_length()/x

g2 = Graph.Watts_Strogatz(1, 2000, 4, 1, bool(1))
trans9 = g2.transitivity_avglocal_undirected()/y
shrt9 = g2.average_path_length()/x


plt.plot([0.0001,0.0005,0.001,0.005, 0.01, 0.05, 0.1, 0.5, 1], [trans1,trans2,trans3,trans4, trans5, trans6, trans7, trans8, trans9], 'b')
plt.xscale('log')
plt.plot([0.0001,0.0005,0.001,0.005, 0.01, 0.05, 0.1, 0.5, 1], [shrt1,shrt2,shrt3,shrt4, shrt5, shrt6, shrt7, shrt8, shrt9], 'r')
plt.axis([0, 1, 0, 1])
plt.show()



