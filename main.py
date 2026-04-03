import sys
import sqlite3
from collections import defaultdict
from matplotlib import pyplot as plt
import psutil
import os
#writing a script that connects to a given KoboReader.sqlite file

def connect_db(path = "KoboReader.sqlite"):
    return sqlite3.connect(path)

def draw_graph(keys, values):
    # bar-graph
    bars = plt.bar(keys, values)
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.title('Bookmark Type Frequency')

    # add value labels on top of each bar
    for bar, value in zip(bars, values):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, str(value), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig("output.svg")
    plt.show()

def create_cursor(path):
    connection = connect_db(path)
    cursor = connection.cursor()
    return cursor

def getAnnotationData(cursor : sqlite3.Cursor) -> defaultdict:
    """Obtain the types of annotations from the Bookmark table found in KoboReader.sqlite"""
    
    query = "Select Type from Bookmark"
    cursor.execute(query)
    
    rows_found = 0

    freq = defaultdict(int)
    row = cursor.fetchone()
    while (row is not None):
        rows_found += 1
        print(row)
        print(row[0])
        freq[row[0]] += 1
        row = cursor.fetchone()
    
    if(rows_found == 0):
        print("either something went wrong and the sqlite table was not found where assumed or... you need to read more :(")

    return freq

def detectKoboDevice() -> tuple:
    """Returns true and the location of the """
    parts = psutil.disk_partitions()
    for part in parts:
        print(psutil.disk_usage(part.mountpoint))
        koboMetadataFolder = os.path.join(part.mountpoint, ".kobo")
        if(os.path.exists(koboMetadataFolder)):
            return (True, os.path.join(koboMetadataFolder, "KoboReader.sqlite"))
    print(type(parts[0].device))
    return (False,)

def main(default_path : str = None): # type: ignore

    kobo_detection = detectKoboDevice()
    kobo_present = kobo_detection[0]
    if (not kobo_present):
        print("kobo device was not detected")
        return
    
    path = kobo_detection[1]
    
    if(len(sys.argv) == 2):
        path = sys.argv[1]
    
    cursor = create_cursor(path)
    freq = getAnnotationData(cursor)
    draw_graph(list(freq.keys()), list(freq.values()))


#main()
#print(detectKoboDevice())