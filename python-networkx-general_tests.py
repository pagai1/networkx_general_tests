#!/usr/bin/python
import csv
import networkx as nx
#import matplotlib.pyplot as plt
import time
import sys
import json
import yaml
import matplotlib.pyplot as plt
from builtins import len

from networkx.algorithms.coloring.greedy_coloring_with_interchange import Node
from networkx.classes.function import get_node_attributes
from networkx.readwrite import json_graph
from _operator import itemgetter
from xlwt.ExcelFormulaLexer import false_pattern
from networkx.drawing.nx_pylab import draw_kamada_kawai
from numpy import number
from pip._vendor.webencodings import labels

def draw_graph(Graph):
    """ Draws the graph """
    nx.draw_kamada_kawai(Graph,with_labels=True,node_color="#FF0000")
    plt.plot()
    plt.show()

def to_ms(time):
    return ("%.3f" % time)

def get_column_names(filereader):
  headers = next(filereader, None)
  return headers

def remove_doubles(inputlist):
    return list(set(inputlist))

### NODELINKDATA
def import_node_link_data_to_graph(inputfile):
    file_to_read = open(inputfile, 'r')
    json_data = json.loads(file_to_read.read())    
    return json_graph.node_link_graph(json_data, directed=True, multigraph=False)

def export_graph_to_node_link_data(G,outputfile):
    print("Exporting graph to node_link_data-file")
    file_to_write = open(outputfile, 'w')
    file_to_write.write(json.dumps(json_graph.node_link_data(G)))
### NODELINKDATA

#### GRAPHML
def export_graph_to_graphML_data(G,outputfile):
    print("Exporting to graphML")
    nx.write_graphml(G, outputfile, prettyprint=True )

def import_graphML_to_graph(inputfile):
    print("Importing graphML file")
    return nx.read_graphml(inputfile)
    
#### GRAPHML

#### GRAPHML
def export_graph_to_adjlist_data(G,outputfile):
    print("Exporting graph to normal Adj List")
    nx.write_adjlist(G, outputfile, delimiter=',')

def import_adjlist_to_graph(inputfile):
    print("Importing normal Adj List")
    file_to_read = open(inputfile, 'r')
    json_data = json.loads(file_to_read.read())    
    return json_graph.node_link_graph(json_data, directed=True, multigraph=False)
#### GRAPHML

#### MULTILINE ADJLIST
def export_graph_to_multiline_adjlist_data(G,outputfile):
    print("Exporting graph to Multiline Adj List")
    nx.write_multiline_adjlist(G, outputfile, delimiter=',',comments="PENGPUFFZACK")

def import_multiline_adjlist_to_graph(inputfile):
    print("Importing Multiline Adj List")
    file_to_read = open(inputfile, 'r')
    json_data = json.loads(file_to_read.read())    
    return json_graph.node_link_graph(json_data, directed=True, multigraph=False)
#### MULTILINE ADJLIST

#### YAML
def export_graph_to_yaml_data(G,outputfile):
    print("Exporting graph to YAML")
    nx.write_yaml(G, outputfile)

def import_yaml_to_graph(inputfile):
    print("Importing YAML")
    G = nx.read_yaml(inputfile)
    return G
#### YAML

#### GML
def export_graph_to_gml_data(G,outputfile):
    print("Exporting graph to GML")
    nx.write_gml(G, outputfile)

def import_gml_to_graph(inputfile):
    print("Importing GML")
    G = nx.read_gml(inputfile)
    return G
#### GML


def create_subGraph(G):
    subG = G.subgraph()
 
def create_graph_from_a_list(numberOfNodes):
    n = numberOfNodes
    G = nx.Graph()
    startTime=time.time()
    for node in list(range(n)):
        G.add_node(node)
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
##### HIER GEHTS LOS ##############
#filepath='/home/pagai/graph-data/tmdb.csv'
#file = open(filepath, 'r')
#if (sys.argv[1]):
#    limit = int(sys.argv[1])
#else:
#    limit=int(100)
 
#G = nx.DiGraph()
#filepath='/home/pagai/graph-data/cooccsdatabase/cooccsdb.csv'
#create_graph_from_neo4j_csv(G, filepath)

#filepath='/home/pagai/graph-data/deezer_clean_data/HU_edges.csv'
#G = nx.read_edgelist(filepath, comments="no comments", delimiter=",", create_using=nx.Graph(), nodetype=str)
# Loading headers
#header_reader = csv.reader(filePath)
#print("HEADERS : " + str(get_column_names(header_reader)))
#create_graph_from_neo4j_csv(G, filepath)

#draw_graph(G,None)

#number = int(sys.argv[1])
#for number in list(range(100000,10000001,250000)):
#    print(number)
#    create_graph_from_a_list(number)
#create_graph_from_a_list(number)

    
#print("NUMBER OF NODES: " + str(G.number_of_nodes()))
#print("NUMBER OF EDGES: " + str(G.number_of_edges()))

#create_watts_strogatz_graph()
#create_graph_from_a_list(10000000)
export = False
if (export):
# EXPORT FILE
    start_export_time = time.time()
    export_graph_to_node_link_data(G, '/var/tmp/export_01_node_link_data.json')
    print("Finished in : " + to_ms(time.time() - start_export_time))
    
    start_export_time = time.time()
    export_graph_to_graphML_data(G,'/var/tmp/export_02_graphML.json')
    print("Finished in : " + to_ms(time.time() - start_export_time))
    
    start_export_time = time.time()
    export_graph_to_adjlist_data(G,'/var/tmp/export_03_adjlist.json')
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

#### IMPORT FILE
#start_time = time.time()
#G = import_node_link_data_to_graph('/var/tmp/node_link_data_5000.json')
#print("File load finished in " + str(time.time() - start_time))

G = import_graphML_to_graph('/var/tmp/export_02_graphML.json')

    
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
draw_graph(G)

#print("FERTIG")
