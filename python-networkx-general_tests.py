#!/usr/bin/python
import csv
import networkx as nx
import matplotlib.pyplot as plt
import time
import sys
import json

from builtins import len
from networkx.algorithms.coloring.greedy_coloring_with_interchange import Node
from networkx.classes.function import get_node_attributes
from networkx.readwrite import json_graph
from _operator import itemgetter
from xlwt.ExcelFormulaLexer import false_pattern
from networkx.drawing.nx_pylab import draw_kamada_kawai
from numpy import number

def draw_graph(Graph):
    """ Draws the graph """
    nx.draw(Graph, with_labels=True)
    #nx.draw_kamada_kawai(Graph,with_labels=True)
    plt.plot()
    plt.show()

def to_ms(time):
    return ("%.3f" % time)

def getNodeCount(graph):
    nodecount = 0
    for node in G.nodes.items():
        nodecount = nodecount + 1
    return nodecount

def get_column_names(filereader):
  headers = next(filereader, None)
  return headers

def remove_doubles(inputlist):
    return list(set(inputlist))

def import_node_link_data_to_graph(inputfile):
    file_to_read = open(inputfile, 'r')
    json_data = json.loads(file_to_read.read())    
    return json_graph.node_link_graph(json_data, directed=True, multigraph=False)

def export_graph_to_node_link_data(G,outputfile):
    print("Exporting graph to node_link_data-file")
    file_to_write = open(outputfile, 'w')
    file_to_write.write(json.dumps(json_graph.node_link_data(G)))

def algo_shortest_path(G):
    actor_list=[x for x,y in G.nodes(data=True) if y['type'] == 'actor']

def create_subGraph(G):
    subG = G.subgraph()
 
def create_graph_from_a_list(numberOfNodes):
    n = int(numberOfNodes)
    G = nx.Graph()
    startTime=time.time()
    for node in list(range(n)):
        G.add_node(node)
    stopTime = time.time()
    print("Runtime for creation of " + str(numberOfNodes) + " nodes: " + to_ms(stopTime - startTime))
    #draw_graph(G)
 
def create_watts_strogatz_graph():
    WSG = nx.watts_strogatz_graph(100,2, 100.0)
    nx.draw_kamada_kawai(WSG,with_labels=True)
    #return G
    plt.plot()
    plt.show()

def create_graph_from_csv_file(csvfile):
    # Loading headers
    header_reader = csv.reader(file)
    print("HEADERS : " + str(get_column_names(header_reader)))
    #print(headers)
    
    # Creating graph
    G = nx.DiGraph()
    
    ## opening file
    with open(filepath, 'r') as csv_file1:
        linecount = 1 
        reader1 = csv.DictReader(csv_file1, quotechar='"', delimiter=',')
    
        
    # creating nodes
        startTime= time.time()
        for actor in unique_actors:
            G.add_node(actor, type='actor', name=str(actor))
        for keyword in unique_keywords:
            G.add_node(keyword, type='keyword', name=str(keyword))
        for genre in unique_genres:
            G.add_node(genre, type='genre' , name=str(genre))
        for director in unique_directors:
            G.add_node(director, type='director' , name=str(director))
        for company in unique_companies:
            G.add_node(company, type='production_company', name=str(company))
        print("Runtime adding single nodes : " + str((time.time() - startTime)))
    
    # creating movienodes and relationships
    startTime = (time.time())  
    with open(filepath, 'r') as csv_file1:
        reader1 = csv.DictReader(csv_file1, quotechar='"', delimiter=',')
        linecount=1
    # Reading actors, genres, keywords, companies and directors for every movie
        edgelist_to_import = []
        for row in reader1:
            if linecount < limit:
                linecount = linecount + 1 
                G.add_node(row['original_title'], type='movie', attr_dict=row)
                for actor1 in row['cast'].split("|"):
                    for actor2 in row['cast'].split("|"):
                        if actor2 != actor:
                            G.add_edge(actor1, actor2,type='ACTED_WITH',count=1.0)
                            G.add_edge(actor2, actor1,type='ACTED_WITH',count=1.0)
                    G.add_edges_from([(actor1, row['original_title'])], type='ACTED_IN' )
                for director in row['director'].split("|"):
                    G.add_edges_from([(director, row['original_title'])], type="DIRECTED" )
                for company in row['production_companies'].split("|"):
                    G.add_edges_from([(company, row['original_title'])], type="PRODUCED" )    
                for genre in row['genres'].split("|"):
                    G.add_edges_from([(row['original_title'], genre)], type="IN_GENRE" )
                for keyword in row['keywords'].split("|"):
                    G.add_edges_from([(row['original_title'], keyword)], type="HAS_KEYWORD" )


def create_graph_from_neo4j_csv(G,filePath):
    with open(filePath,'r') as csv_file:
        reader = csv.DictReader(csv_file,quotechar = '"', delimiter=',')
        for line in reader:
            if line['_id'] != "":
                G.add_node(line['_id'], weight=line['occur'], label=line['_labels'], name=line['name'])
            else:
                G.add_edge(line['_start'],line['_end'],type=line['_type'],cost=line['cost'],count=['count'],dice=['dice'])
                G.add_edge(line['_end'],line['_start'],type=line['_type'],cost=line['cost'],count=['count'],dice=['dice']) 
 
    start_time = time.time() 
    dict_nodes = nx.closeness_centrality(G)
    print("ZEIT: " + str(time.time() - start_time))

##### HIER GEHTS LOS ##############
filepath='/home/pagai/graph-data/tmdb.csv'
file = open(filepath, 'r')
limit = sys.argv[0]
if limit == None:
    limit=100
 

G = nx.Graph()
filePath='/home/pagai/graph-data/cooccsdatabase/cooccsdb.csv'

# Loading headers
header_reader = csv.reader(filePath)
print("HEADERS : " + str(get_column_names(header_reader)))

create_graph_from_neo4j_csv(G, filePath)
    

#create_watts_strogatz_graph()
#create_graph_from_a_list(10000000)

#### IMPORT FILE
#start_time = time.time()
#G = import_node_link_data_to_graph('/var/tmp/node_link_data_5000.json')
#print("File load finished in " + str(time.time() - start_time))

# EXPORT FILE
#start_time = time.time()
#export_graph_to_node_link_data(G, '/var/tmp/node_link_data_5000.json')
#print("File export finished in : " + str(time.time() - start_time))


# ALGOS
#algo_shortest_path(G)
#algo_pagerank(G)
#get_hits(G)


#print(pagerank_scipy(subG))
#if limit < 100:
draw_graph(G)

print("FERTIG")
