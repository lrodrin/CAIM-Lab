from igraph import * 

karate = Graph.Famous("Zachary")
print "Average Path Length: " + str(karate.average_path_length())
print "Transivity: " + str(karate.transitivity_avglocal_undirected())
print "Degree distribution: " + str(karate.degree_distribution())
print "Diameter: " + str(karate.diameter())