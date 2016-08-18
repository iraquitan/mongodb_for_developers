# -*- coding: utf-8 -*-
"""
 * Created by PyCharm.
 * Project: login_logout_signup
 * Author name: Iraquitan Cordeiro Filho
 * Author login: pma007
 * File: homework_3-1
 * Date: 8/18/16
 * Time: 11:47
 * To change this template use File | Settings | File Templates.

.. moduleauthor:: Iraquitan Cordeiro Filho <iraquitanfilho@gmail.com>

"""
import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.school
students = db.students


def update_scores(_id, new_scores):
    doc = students.find_one_and_update(
        {'_id': _id}, {'$set': {'scores': new_scores}},
        return_document=pymongo.ReturnDocument.AFTER)
    print("updated scores for student {}".format(doc['_id']))


def remove_lowest_homework():
    query = {}
    sort_ = [('_id', pymongo.ASCENDING)]
    cursor = students.find(query).sort(sort_)
    for doc in cursor:
        lowest = 1000
        for score in doc['scores']:
            if score['type'] == 'homework' and score['score'] < lowest:
                lowest = score['score']
                lowest_score = score
        # removes the lowest homework from doc
        doc['scores'].remove(lowest_score)
        update_scores(doc['_id'], doc['scores'])

# main
remove_lowest_homework()
