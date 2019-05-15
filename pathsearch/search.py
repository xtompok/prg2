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

wgs = pyproj.Proj( "+init=epsg:4326")
jtsk = pyproj.Proj("+init=epsg:5514")
def jtsk2wgs(coords):
    return pyproj.transform(jtsk,wgs,coords[0],coords[1])
#    return pyproj.transform(jtsk,wgs,*coords)

def wgs2jtsk(coords):
    return pyproj.transform(wgs,jtsk,coords[0],coords[1])

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

def create_graph(nodes,segments):
    G = nx.Graph()
    G.add_nodes_from(nodes.keys())
    print("Features: {}".format(len(segments["features"])))
    for f in segments["features"]:
        coords = f["geometry"]["coordinates"]
        length = linestring_length(coords)
        props = f["properties"]
        props["length"] = length
        G.add_edge(tuple(coords[0]),tuple(coords[-1]),**props)

    maxvertices = 0
    maxcomp = None
    for comp in nx.connected_components(G):
        comp = set(comp)
        if len(comp) > maxvertices:
            maxcomp = comp
            maxvertices = len(comp)
    return G.subgraph(maxcomp)

G = create_graph(nodes,segments)

def find_nearest_node(x,y):
    """Vrátí nejbližší vrchol grafu k zadaným souřadnicím"""
    minlen = float('inf')
    minlennode = None
    for n in G.nodes:
        len = seg_length((x,y),n)
        if len < minlen:
            minlen = len
            minlennode = n
    return minlennode

def search_path(fromlon,fromlat, tolon, tolat):
    # Převedeme WGS na JTSK
    (fromx,fromy) = wgs2jtsk((fromlon,fromlat))
    (tox, toy) = wgs2jtsk((tolon,tolat))
    print("flon: {}, flat: {}, fx: {}, fy: {}".format(fromlon,fromlat,fromx,fromy))
    # Najdeme nejbližší vrcholy grafu k zadaným souřadnicím
    fromnode = find_nearest_node(fromx,fromy)
    tonode = find_nearest_node(tox,toy)
    # Najdeme nejkratší cestu
    path = nx.shortest_path(G,fromnode,tonode,'length')
    # Převedeme nejkratší cestu zpět do WGS
    wgspath = [jtsk2wgs(n) for n in path]
    return wgspath

def save_to_geojson(path,filename):
    outjson = {"type": "FeatureCollection",
               "features": [{
                  "type" : "Feature",
                  "geometry": {
                      "type": "LineString",
                    "coordinates": path
                  }
               }]
    }
    with open(filename,"w") as f:
        json.dump(outjson,f)



path = search_path(14.4299708,50.0624341,15,50)
save_to_geojson(path,"output.json")


