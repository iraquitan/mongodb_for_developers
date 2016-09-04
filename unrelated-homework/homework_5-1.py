# -*- coding: utf-8 -*-
"""
 * Project: mongodb_for_developers
 * Author name: Iraquitan Cordeiro Filho
 * Author login: iraquitan
 * File: homework_5-1
 * Date: 9/3/16
 * Time: 11:14 PM
"""
import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.blog


def most_frequent_commenter():
    agg = [
        {"$unwind": "$comments"},
        {"$group": {"_id": "$comments.author", "number_posts": {"$sum": 1}}},
        {"$sort": {"number_posts": pymongo.DESCENDING}},
        {"$limit": 1}
    ]
    cursor = db.posts.aggregate(agg)
    for doc in cursor:
        print doc

# main
most_frequent_commenter()
