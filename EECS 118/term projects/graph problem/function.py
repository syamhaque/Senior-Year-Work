#find s where is_path(s, A, B) and total_weight(s, t) and color(s, Color, u) and t>C and u=D 
#Mohammed Haque
#Jose Alberto Padilla
#EECS 118 TP2
#12/5/19
import networkx as nx
import csv
import sys

#Obtains information from csv file in format (Node1,Node2,weight,color)
#with no titles and makes a graph out of it
def input_csv(g, the_graph):
    with open(the_graph) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if row[0] == 'Node1':
                continue
            g.add_edge(int(row[0]),int(row[1]), weight = float(row[2]), color = row[3])
    return g    

#Checks if a and b (A,B) is a path in s by creating a graph g out of list s
#Then checks if g has the path a, b (A,B).
def is_path(s, a, b):
    g = nx.Graph()
    nx.add_path(g, s)
    if(nx.has_path(g, a, b)):
        return True
    else:
        return False

#Checks if the total weight on path s is greater than t (C) by making a
#path graph from the path s (is a list). Then iterates through the edges
#of the path and obtains the weight of each edge using the graph g. Finally
#checks if the total weight calculated of the path is greater than t.
def total_weight(s, t, g):
    path_weights = 0
    path_graph = nx.path_graph(s)
    for eattr in path_graph.edges():
        path_weights += list(g.edges[eattr].values())[0]
    if (path_weights > t):
        return True
    else:
        return False

#Checks if the amount of colors k (Color) in path s is equal to n (D) by a
#making path graph from the path s (is a list). Then iterates through the 
#edges of the path and obtains the colors of each edge using the graph g.
#The colors and their amount are all put into a dictionary and then checks
#if the amount of color k in the dictionary is equal to n.
def color(s, k, n, g):
    path_colors = {}
    path_graph = nx.path_graph(s)
    for eattr in path_graph.edges():
        if list(g.edges[eattr].values())[1] not in path_colors.keys():
            path_colors[list(g.edges[eattr].values())[1]] = 1
        else:
            path_colors[list(g.edges[eattr].values())[1]] += 1
    if (path_colors.get(k) == n):
        return True
    else:
        return False

#Gets a list of paths that satisfy the predicates and outputs them to a
#csv according to the pdf
def output_csv(s):
    count = 0
    with open('output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        if len(s) == 0:
            writer.writerow(["NULL"])
        else:
            for i in s:
                count += 1
                path_count = 'path_' + str(count)
                writer.writerow([path_count])
                path_graph = nx.path_graph(i)
                for eattr in path_graph.edges():
                    writer.writerow([eattr[0],eattr[1]])
