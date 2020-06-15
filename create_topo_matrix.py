import json
import numpy as np

#参考博客园

def readJSONFile(path):
    f = open(path, "r")
    return json.load(f)


def createNodesMatrix():
    arr = np.zeros((100, 100))
    nodes_json = readJSONFile("data_release/topology/topology_edges_node.json")
    for node in nodes_json:
        for son in nodes_json[node]:
            arr[int(son.split("_")[1])][int(node.split("_")[1])] = 1
    np.savetxt("arr.csv", arr, fmt="%i", delimiter=",")
    return arr


if __name__ == '__main__':
    nodes = createNodesMatrix()