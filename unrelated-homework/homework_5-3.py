# -*- coding: utf-8 -*-
"""
 * Project: mongodb_for_developers
 * Author name: Iraquitan Cordeiro Filho
 * Author login: iraquitan
 * File: homework_5-3
 * Date: 9/4/16
 * Time: 12:46 AM
"""
import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.test


def class_highest_student_performance():
    agg = [
        {"$unwind": "$scores"},
        {"$match": {"scores.type": {"$ne": "quiz"}}},
        {"$group": {
            "_id": {"class_id": "$class_id", "student_id": "$student_id"},
            "gpa": {"$avg": "$scores.score"}
        }},
        {"$group": {"_id": "$_id.class_id", "average": {"$avg": "$gpa"}}},
        {"$sort": {"average": -1}},
        {"$limit": 1}
    ]
    cursor = db.grades.aggregate(agg)
    for doc in cursor:
        print doc

# main
class_highest_student_performance()
