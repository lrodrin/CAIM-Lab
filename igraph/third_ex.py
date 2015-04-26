from igraph import * 

karate = Graph.Famous("Zachary")
pagerank = karate.pagerank()

layout = karate.layout("kk")
print  "El node amb mes pagerank es: " + str(pagerank.index(max(pagerank))) + " i el valor es: " + str(max(pagerank))

plot(karate, layout = layout, vertex_size = [int(round(a*200)) for a in pagerank])