#!/usr/bin/python3
'''
A script to export data in the CSV format.
'''

import csv
import requests
import sys


def getData(id):
    """
    Get data from json api and export to json file
    """
    usersurl = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todourl = "{}/todos".format(usersurl)

    request1 = requests.get(usersurl)
    result = request1.json()
    userid = result['id']
    username = result['username']

    request2 = requests.get(todourl)
    tasks = request2.json()


    with open("{}.csv".format(userid), "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([userid, username, task['completed'], task['title']])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = sys.argv[1]
    else:
        id = 1
    getData(str(id))