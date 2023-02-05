from controller.validator.validate_email import valid_email
from service.question_model import question_model

obj = question_model()


def post_question_controller():
    print("To Post a Question: ")
    question = input("Enter the question: ")
    userId = input("Enter the userId as your emailId: ")
    if valid_email(userId):
        data = {
            "question": question,
            "userId": userId
        }
        response = obj.post_questions_model(data)
        print(response)
    else:
        return post_question_controller()


# post_question_controller()


def getAnswer_by_questionId_controller():
    print("\n")
    print("To Get an Answer by QuestionId: ")
    questionId = input("Enter the questionId: ")
    data = {"questionId": questionId}
    # return obj.getAnswer_by_questionId_model(data)
    response = obj.getAnswer_by_questionId_model(data)
    print(response)


# getAnswer_by_questionId_controller()


def getAll_question_by_userId_controller():
    print("\n")
    print("To Get a Question by userId: ")
    userId = input("Enter the userId: ")
    data = {"userId": userId}
    # return obj.getAll_question_by_userId_model(data)
    response = obj.getAll_question_by_userId_model(data)
    print(response)


# getAll_question_by_userId_controller()


def edit_answers_controller():
    print("\n")
    print("To Edit an Answer: ")
    print("\n")
    print("Please enter following details to edit and update a particular answer: ")
    questionId = input("questionId: ")
    userId = input("userId: ")
    val1 = input("Enter the answer thats has to be updated: ")
    data = {
        "questionId": questionId,
        "userId": userId,
        "val1": val1
    }
    response = obj.edit_answers_model(data)
    print(response)


edit_answers_controller()


def delete_question_controller():
    print("\n")
    print("To Delete a Question: ")
    questionId = input("Enter the questionId: ")
    userId = input("Enter the userId as your emailId: ")
    data = {
        "questionId": questionId,
        "userId": userId
    }
    response = obj.delete_question_model(data)
    print(response)


# delete_question_controller()
