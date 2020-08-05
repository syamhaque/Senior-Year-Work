#find s where is_path(s, A, B) and total_weight(s, t) and color(s, Color, u) and t>C and u=D
#Mohammed Haque
#Jose Alberto Padilla
#EECS 118 TP2
#12/5/19
import networkx as nx
import function as fn
import csv
import sys

#Initialize g to graph and read from csv and lists that will hold paths
g = nx.Graph()
all_paths = []
s = []
the_graph = sys.argv[1]
g = fn.input_csv(g, the_graph)

#Ask for user inputs
A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = float(input("Enter C: "))
D = int(input("Enter D: "))
Color = input("Enter Color: ")

#Iterate through all paths between A to B in g and store into a list
for path in nx.all_simple_paths(g, A, B):
    all_paths.append(path)
#Iterate through all valid paths attained and find those that satisfy predicates
for i in all_paths:
    if(fn.is_path(i,A,B) and fn.total_weight(i,C,g) and fn.color(i,Color,D,g)):
        s.append(i)
        
fn.output_csv(s)



