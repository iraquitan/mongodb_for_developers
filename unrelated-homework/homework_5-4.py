# -*- coding: utf-8 -*-
"""
 * Project: mongodb_for_developers
 * Author name: Iraquitan Cordeiro Filho
 * Author login: iraquitan
 * File: homework_5-4
 * Date: 9/4/16
 * Time: 1:51 PM
"""
import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.test


def population_on_where_city_starts_digit():
    agg = [
        {"$project": {
            "first_char": {"$substr": ["$city", 0, 1]},
            "pop": 1}},
        {"$match": {"first_char": {"$regex": "[0-9]"}}},
        {"$group": {"_id": "null", "sum_pop": {"$sum": "$pop"}}}
    ]
    cursor = db.zips.aggregate(agg)
    for doc in cursor:
        print doc


# main
population_on_where_city_starts_digit()
