#!/usr/bin/python
import csv
import networkx as nx
#import matplotlib.pyplot as plt
import time
import sys
import os
import json
import yaml
import matplotlib.pyplot as plt
from builtins import len
from _tkinter import create

# import own helper-modules
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(__file__),"../../networkx_modules")))
from helpers.generalStuff import *
from helpers.networkx_load_n_save import *
from algoPackage.pageRank import *

from networkx.algorithms.coloring.greedy_coloring_with_interchange import Node
from networkx.classes.function import get_node_attributes
from networkx.readwrite import json_graph
from _operator import itemgetter
from xlwt.ExcelFormulaLexer import false_pattern
from networkx.drawing.nx_pylab import draw_kamada_kawai
from numpy import number
from pip._vendor.webencodings import labels
from networkx.classes.digraph import DiGraph

def draw_graph(Graph):
    """ Draws the graph """
    nx.draw_kamada_kawai(Graph,with_labels=True,node_color="#FF0000",font_size=8,style="dashed")
    plt.plot()
    plt.show()

def to_ms(time):
    return ("%.3f" % time)

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
    stopTime = time.time()
#    print(str(numberOfNodes) + "," + to_ms(stopTime - startTime) + "," + str(int(round((numberOfNodes / (stopTime - startTime))))))
    start_export_time = time.time()
    export_graph_to_node_link_data(G, "/mnt/data/export_" + str(numberOfNodes) + ".json")
    exportEndTime = time.time()
    print(str(numberOfNodes) + "," + to_ms(stopTime - startTime) + "," + str(int(round((numberOfNodes / (stopTime - startTime))))) + ",/mnt/data/export_" + str(numberOfNodes) + ".json," + to_ms((time.time() - startTime)) + "," + str(int(round((numberOfNodes / (exportEndTime - startTime))))))
    del G

def create_watts_strogatz_graph():
    WSG = nx.watts_strogatz_graph(100,2, 100.0)
    nx.draw_kamada_kawai(WSG,with_labels=True)
    #return G
    plt.plot()
    plt.show()

def create_graph_from_neo4j_csv(G,filePath):
    print("Loading graph from csv: " + filePath)
    with open(filePath,'r') as csv_file:
        #reader = csv.DictReader(csv_file,quotechar = '', delimiter=',')
        reader = csv.DictReader(csv_file, delimiter=',')
        for line in reader:
            if line['_id'] != "":
                G.add_node(line['_id'], name=line['name'], weight=line['occur'], label=line['_labels'], id=line['_id'])
            else:
                G.add_edge(line['_start'],line['_end'],type=line['_type'],cost=line['cost'],count=line['count'],dice=line['dice'])
                G.add_edge(line['_end'],line['_start'],type=line['_type'],cost=line['cost'],count=line['count'],dice=line['dice']) 
    print("Done.")
    

def create_complete_graph(G,attrs=False):
    nodeList = G.nodes()
    for node1 in nodeList:
        for node2 in nodeList:
            if attrs:
                G.add_edge(node1,node2,node1=node1,node2=node2)
            else:
                G.add_edge(node1,node2)

##### HIER GEHTS LOS ##############
filepath='/home/pagai/graph-data/pokec/soc-pokec-relationships_weighted.txt'
tmpfilepath = "/tmp/tmpfile.csv"

limit = 0
seclimit=1
operatorFunction="eq"
verbose=False
doExport=True
doExportTest=False # War nur zum Testen von den unterschiedlichen Arten.
createByImport=False
createByImportTest=False
doAlgo=False
algoVerbose=False

if (len(sys.argv) == 1):
    if (verbose):
        print("NOTHING WAS GIVEN")
    limit = "100"
elif (len(sys.argv) == 2):
    limit = sys.argv[1]
    if (verbose):
        print("WORKING WITH " + str(limit))

importExportFileName = "/tmp/node_link_data_export_" + str(limit) + ".json"

#filepath='/home/pagai/graph-data/tmdb.csv'
#file = open(filepath, 'r')
#if (sys.argv[1]):
#    limit = int(sys.argv[1])
#else:
#    limit=int(100)
 


#filepath='/home/pagai/graph-data/deezer_clean_data/HU_edges.csv'
#G = nx.read_edgelist(filepath, comments="no comments", delimiter=",", create_using=nx.Graph(), nodetype=str)
# Loading headers
#header_reader = csv.reader(filePath)
#print("HEADERS : " + str(get_column_names(header_reader)))
#create_graph_from_neo4j_csv(G, filepath)

#draw_graph(G,None)

#number = int(sys.argv[1])

########################### Range Test #########################
#for number in list(range(25000,1000000,25000)):
#    print(number)
#    create_graph_from_a_list(number)
 
 
########################### EdgeTest ########################### 

G = nx.empty_graph(int(limit),create_using=nx.DiGraph)
if verbose:
    print("NUMBER OF NODES: " + str(G.number_of_nodes()))
    print("NUMBER OF EDGES: " + str(G.number_of_edges()))
start_time = time.time()
create_complete_graph(G,attrs=True)
if verbose:
    print("NUMBER OF NODES: " + str(G.number_of_nodes()))
    print("NUMBER OF EDGES: " + str(G.number_of_edges()))
    for edge in G.edges(data=True):
        print(edge)
#create_watts_strogatz_graph()
#create_graph_from_a_list(10000000)

##################################################################

##################### EXPORT-TEST ################################
# EXPORT FILE
if (doExportTest):
    G = nx.DiGraph()
    filepath='/home/pagai/graph-data/cooccsdatabase/cooccsdb.csv'
    create_graph_from_neo4j_csv(G, filepath)


    start_export_time = time.time()
    export_graph_to_node_link_data(G, '/var/tmp/export_01_node_link_data.json')
    print("Finished in : " + to_ms(time.time() - start_export_time))
    
    start_export_time = time.time()
    export_graph_to_graphML_data(G,'/var/tmp/export_02_graphML.json')
    print("Finished in : " + to_ms(time.time() - start_export_time))
   
    start_export_time = time.time()
    export_graph_to_adjlist_data(G,'/var/tmp/export_03_adjlist.txt')
    print("Finished in : " + to_ms(time.time() - start_export_time))
   
    start_export_time = time.time()
    export_graph_to_multiline_adjlist_data(G,'/var/tmp/export_04_multiline_adjlist.txt')
    print("Finished in : " + to_ms(time.time() - start_export_time))
   
    start_export_time = time.time()
    export_graph_to_yaml_data(G,'/var/tmp/export_05_yaml.yaml')
    print("Finished in : " + to_ms(time.time() - start_export_time))
   
    start_export_time = time.time()
    export_graph_to_gml_data(G,'/var/tmp/export_06_gml.gml')
    print("Finished in : " + to_ms(time.time() - start_export_time))

######################### IMPORT  TEST #############################
#start_time = time.time()
#G = import_node_link_data_to_graph('/var/tmp/node_link_data_5000.json')
#print("File load finished in " + str(time.time() - start_time))
if (createByImportTest):
# IMPORT FILES
    start_import_time = time.time()
    G = import_node_link_data_to_graph('/var/tmp/export_01_node_link_data.json')
    print("Finished in : " + to_ms(time.time() - start_import_time))
    print_all(G)
    print("=================")
    del G
#    
#    start_import_time = time.time()
#    G = import_graphML_to_graph('/var/tmp/export_02_graphML.json')
#    print("Finished in : " + to_ms(time.time() - start_import_time))
#    print_all(G)
#    print("=================")
#    del G
#
#    start_import_time = time.time()
#    G = import_adjlist_to_graph('/var/tmp/export_03_adjlist.txt')
#    print("Finished in : " + to_ms(time.time() - start_import_time))
#    print_all(G)
#    print("=================")
#    del G
#        
#    start_import_time = time.time()
#    G = import_multiline_adjlist_to_graph('/var/tmp/export_04_multiline_adjlist.txt')
#    print("Finished in : " + to_ms(time.time() - start_import_time))
#    print_all(G)
#    print("=================")
#    del G
       
#    start_import_time = time.time()
#    G = import_yaml_to_graph('/var/tmp/export_05_yaml.yaml')
#    print("Finished in : " + to_ms(time.time() - start_import_time))
#    print_all(G)
#    print("=================")
#    del G
    
#    start_import_time = time.time()
#    G = import_gml_to_graph('/var/tmp/export_06_gml.gml')
#    print("Finished in : " + to_ms(time.time() - start_import_time))   
#    print_all(G)
#    print("=================")
#    del G
        
############ Export/Import ##########
if createByImport:
    print("IMPORTING " + importExportFileName)
    start_time = time.time()
    G = import_node_link_data_to_graph(importExportFileName, verbose=verbose)
    if (verbose): 
        print("IMPORTED FILE: " + importExportFileName)
        print(nx.info(G))

if doExport:
    export_graph_to_node_link_data(G, importExportFileName, verbose=verbose)

end_time_full = time.time()

print(str(G.number_of_nodes()),str(G.number_of_edges()),to_ms(end_time_full - start_time),sep=",")
#if os.path.isfile(importExportFileName):
#     os.remove(importExportFileName)


#G = import_yaml_to_graph('/var/tmp/node_link_data_cooccs_to_yaml.yaml')

#G = import_gml_to_graph('/var/tmp/node_link_data_cooccs_to_gml.gml')
#print(G.nodes())
#print(G.edges())


# ALGOS
#algo_shortest_path(G)
#algo_pagerank(G)
#get_hits(G)


#print(pagerank_scipy(subG))
#if limit < 100:
#draw_graph(G)
#print("FERTIG")

