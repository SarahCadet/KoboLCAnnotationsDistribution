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

def create_cursor(path):
    connection = connect_db(path)
    cursor = connection.cursor()
    return cursor

def getAnnotationData(cursor : sqlite3.Cursor) -> defaultdict:
    """Obtain the types of annotations from the Bookmark table found in KoboReader.sqlite"""
    
    query = "Select Type from Bookmark"
    cursor.execute(query)

    freq = defaultdict(int)
    row = cursor.fetchone()
    while (row is not None):
        print(row)
        print(row[0])
        freq[row[0]] += 1
        row = cursor.fetchone()
    return freq


def main():
    path = "KoboReader.sqlite"
    
    if(len(sys.argv) == 2):
        path = sys.argv[1]

    cursor = create_cursor(path)
    freq = getAnnotationData(cursor)
    draw_graph(list(freq.keys()), list(freq.values()))


main()