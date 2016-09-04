# -*- coding: utf-8 -*-
"""
 * Project: mongodb_for_developers
 * Author name: Iraquitan Cordeiro Filho
 * Author login: iraquitan
 * File: homework_5-2
 * Date: 9/4/16
 * Time: 12:16 AM
"""
import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.agg


def avg_pop_gt25000():
    agg = [
        {"$group": {
            "_id": {"state": "$state", "city": "$city"},
            "pop": {"$sum": "$pop"}
        }},
        {"$match": {
            "pop": {"$gt": 25000},
            "_id.state": {"$in": ["CA", "NY"]}
        }},
        {"$group": {
            "_id": "null",
            "avg": {"$avg": "$pop"}
        }}
    ]

    cursor = db.smallzips.aggregate(agg)
    for doc in cursor:
        print doc

# main
avg_pop_gt25000()
