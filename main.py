import sys
import sqlite3
from collections import defaultdict
from matplotlib import pyplot as plt
#writing a script that connects to a given KoboReader.sqlite file

def connect_db(path = "KoboReader.sqlite"):
    return sqlite3.connect(path)

def draw_graph(keys, values):
    # bar-graph
    plt.bar(keys, values)
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.title('Bookmark Type Frequency')
    plt.tight_layout()
    plt.savefig("output.rgba")
    plt.show()

def main():
    path = "KoboReader.sqlite"
    
    if(len(sys.argv) == 2):
        path = sys.argv[1]
    
    connection = connect_db(path)
    curr = connection.cursor()

    curr.execute("Select Type from Bookmark")
    freq = defaultdict(int)
    row = curr.fetchone()
    while (row is not None):
        print(row)
        print(row[0])
        freq[row[0]] += 1
        row = curr.fetchone()
    
    draw_graph(list(freq.keys()), list(freq.values()))


main()