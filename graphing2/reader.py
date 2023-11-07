#!/usr/bin/python3

# from python std library
import csv

# python3 -m pip install np
import numpy as np
# python3 -m pip install matplotlib
import matplotlib
matplotlib.use('Agg')
# sudo apt install python3-tk
import matplotlib.pyplot as plt

def parsecsvdata():
    """returns a list. [0] is LAN and [1] WAN data"""
    summary = [] # list that will contain [(LAN), (WAN)]

    # open csv data
    with open("./onepiecefruits.txt",\
     "r") as downtime:
        # parse csv data with csv.reader
        downdata = csv.reader(downtime, delimiter=",")
        for row in downdata:
            rowdat = (str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))
            summary.append(rowdat) # add dict to list
    return summary

def main():
    N = 6
    ## grab our data
    summary = parsecsvdata() # grab our data
    character = summary[0] # LAN data
    fruit = summary[1] # WAN data
    _class = summary[2] # WAN data
    subClass = summary[3] # WAN data
    awakened = summary[4] # WAN data
    status = summary[5] # WAN data

    ind = np.arange(N)    # the x locations for the groups
    # the width of the bars: can also be len(x) sequence
    width = 0.35

    # describe where to display p1
    p1 = plt.bar(ind, _class, width)
    # stack p2 on top of p1
    #p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    # Describe the table metadata
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6"))
    plt.yticks(np.arange(0, 81, 10))
    #plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    # SAVE the graph locally
    plt.savefig("./class.png")
    # Save to "~/static"
    #plt.savefig("/home/student/static/2018summaryv2.png")       
    print("Graph created.")

if __name__ == "__main__":
    main()
