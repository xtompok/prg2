import json
import networkx as nx
import pyproj
import math

segments = None

with open("ulice-jtsk.json",encoding='utf-8') as segfile:
    segments = json.load(segfile)

nodes = {}
for f in segments["features"]:
    geom = f["geometry"]["coordinates"]
    first = tuple(geom[0])
    last = tuple(geom[-1])
    if first not in nodes:
        nodes[first] = 1
    else:
        nodes[first] += 1
    if last not in nodes:
        nodes[last] = 1
    else:
        nodes[last] += 1
print(len(nodes))

histogram = {}
for v in nodes.values():
    if v in histogram:
        histogram[v] += 1
    else:
        histogram[v] = 1

for k in sorted(histogram.keys()):
    print("{} : {}".format(k,histogram[k]))

wgs = pyproj.Proj("+init=epsg:4326")
jtsk = pyproj.Proj("+init=epsg:5514")
def utm2wgs(coords):
    return pyproj.transform(jtsk,wgs,coords[0],coords[1])
#    return pyproj.transform(jtsk,wgs,*coords)

def seg_length(pt1, pt2):
    """Spočítá vzdálenost mezi body pt1 a pt2 zadanými v metrickém zobrazení"""
    dx = pt1[0] - pt2[0]
    dy = pt1[1] - pt2[1]
    return math.sqrt(dx**2+dy**2)

def linestring_length(coords):
    """Spočítá délku lomené čáry definované souřadnicemi zadanými v metrickém zobrazení"""
    length = 0
    mempt = coords[0]
    for pt in coords[1:]:
        length += seg_length(mempt,pt)
        mempt = pt
    return length

G = nx.Graph()
G.add_nodes_from(nodes.keys())
print("Features: {}".format(len(segments["features"])))
for f in segments["features"]:
    coords = f["geometry"]["coordinates"]
    length = linestring_length(coords)
    props = f["properties"]
    props["length"] = length
    G.add_edge(tuple(coords[0]),tuple(coords[-1]),**props)

print(nx.shortest_path(G,
    (-734298.7599533685, -1045994.1000395045 ),
    (-734661.9999935701, -1048392.0000447445),'length'))
