from igraph import *
import matplotlib.pyplot as plt
import random
import sys
import math

random.seed(1234)

shrt0 = 0
print(shrt0);

p = ((1+sys.float_info.epsilon)*math.log(50))/50
g2 = Graph.Erdos_Renyi(50, p)
shrt1 = g2.average_path_length()
print(shrt1);

p = ((1+sys.float_info.epsilon)*math.log(100))/100
g2 = Graph.Erdos_Renyi(100, p)
shrt2 = g2.average_path_length()
print(shrt2);

p = ((1+sys.float_info.epsilon)*math.log(500))/500
g2 = Graph.Erdos_Renyi(500, p)
shrt3 = g2.average_path_length()
print(shrt3);

p = ((1+sys.float_info.epsilon)*math.log(1000))/1000
g2 = Graph.Erdos_Renyi(1000, p)
shrt4 = g2.average_path_length()
print(shrt4);

p = ((1+sys.float_info.epsilon)*math.log(2500))/2500
g2 = Graph.Erdos_Renyi(2500, p)
shrt5 = g2.average_path_length()
print(shrt5);

p = ((1+sys.float_info.epsilon)*math.log(5000))/5000
g2 = Graph.Erdos_Renyi(5000, p)
shrt6 = g2.average_path_length()
print(shrt6);

p = ((1+sys.float_info.epsilon)*math.log(10000))/10000
g2 = Graph.Erdos_Renyi(10000, p)
shrt7 = g2.average_path_length()
print(shrt7);

p = ((1+sys.float_info.epsilon)*math.log(20000))/20000
g2 = Graph.Erdos_Renyi(20000, p)
shrt8 = g2.average_path_length()
print(shrt8);

p = ((1+sys.float_info.epsilon)*math.log(30000))/30000
g2 = Graph.Erdos_Renyi(30000, p)
shrt9 = g2.average_path_length()
print shrt8;

plt.plot([0,50,100,500,1000, 2500, 5000, 10000, 20000, 30000], [shrt0,shrt1,shrt2,shrt3,shrt4, shrt5, shrt6, shrt7, shrt8, shrt9], 'r')
plt.axis([0, 30000, 0, 5])
plt.show()



