#!/usr/bin/python
import csv
import networkx as nx
import time
import sys
import os
from builtins import len

# import own helper-modules
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(__file__),"../../networkx_modules")))
from helpers.generalStuff import *
from helpers.networkx_load_n_save import *
from algoPackage.pageRank import *

def get_column_names(filereader):
  headers = next(filereader, None)
  return headers

def remove_doubles(inputlist):
    return list(set(inputlist))

def print_all(G):
    print("LE GRAPHE: ")
    print(G.nodes(data=True))
    print(G.edges(data=True))
    print(G.number_of_nodes())
    print(len(G.edges()))

def create_subGraph(G):
    subG = G.subgraph()
 
def create_graph_from_a_list(numberOfNodes):
    n = numberOfNodes
    G = nx.Graph()
    startTime=time.time()
    for node in list(range(n)):
        # Create pure node
        G.add_node(node)
        # Create node with property
        #G.add_node(node, name=node)
        # Create node with label
        #G.add_node(node, label="SINGLE_NODE")
        # Create node with property and label
        #G.add_node(node, label="SINGLE_NODE", name=node)
    # with export
    export_graph_to_node_link_data(G, "/tmp/export.json", False)
    stopTime = time.time()
    #print(str(numberOfNodes) + "," + to_ms(stopTime - startTime) + "," + str(int(round((numberOfNodes / (stopTime - startTime))))))
    print(str(numberOfNodes) + "," + to_ms(stopTime - startTime) + "," + str(int(round((numberOfNodes / (stopTime - startTime))))))
    
#filepath='/home/pagai/graph-data/deezer_clean_data/HU_edges.csv'
#G = nx.read_edgelist(filepath, comments="no comments", delimiter=",", create_using=nx.Graph(), nodetype=str)
# Loading headers
#header_reader = csv.reader(filePath)
#print("HEADERS : " + str(get_column_names(header_reader)))
#create_graph_from_neo4j_csv(G, filepath)

#draw_graph(G,None)

if (len(sys.argv) > 1): 
    number = int(sys.argv[1])
    create_graph_from_a_list(number)
else:
    print("Anzahl,Zeit,Knoten_pro_sekunde")
    for number in list(range(25000,1000001,25000)):
        #print(number)
        create_graph_from_a_list(number)
    
#if mainVerbose:
#    print("NUMBER OF NODES: " + str(G.number_of_nodes()))
#   print("NUMBER OF EDGES: " + str(G.number_of_edges()))

#create_watts_strogatz_graph()
#create_graph_from_a_list(10000000)



