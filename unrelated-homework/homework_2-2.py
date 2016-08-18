import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.students
grades = db.grades


def delete_score(_id):
    try:
        doc = grades.find_one_and_delete({'_id': _id})
        print("removed score {0}, for student {1}".format(
            doc['score'], doc['student_id']))
    except Exception as e:
        print("Unexpected error: {}".format(e))


def delete_lowest_homework():
    query = {'type': "homework"}
    sort_ = [('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)]
    try:
        cursor = grades.find(query).sort(sort_)
    except Exception as e:
        print("Unexpected error: {}".format(e))

    curr_student_id = -1
    for doc in cursor:
        if doc['student_id'] != curr_student_id:
            curr_student_id = doc['student_id']
            delete_score(doc['_id'])


# main
delete_lowest_homework()
