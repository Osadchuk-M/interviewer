#!/usr/bin/python3

import csv
import sys
import random

def read_questions_answers(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        # Ensure that the CSV reader correctly handles multiline fields
        reader = csv.reader(file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        return list(reader)

def main(number_of_questions, questions_answers):
    random.shuffle(questions_answers)
    number_of_questions = min(number_of_questions, len(questions_answers))

    for i in range(number_of_questions):
        question, answer = questions_answers[i]
        print(f"Question {i+1}: {question}")
        input("Press 'enter' to show the answer...")
        print(f"Answer: {answer}\n")
        input("Press 'enter' for the next question...")

if __name__ == "__main__":
    default_number_of_questions = 5

    if len(sys.argv) > 1:
        try:
            number_of_questions = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid number for the number of questions.")
            sys.exit(1)
    else:
        number_of_questions = default_number_of_questions

    csv_file_path = 'cxx_questions_and_answers.csv'
    questions_answers = read_questions_answers(csv_file_path)
    main(number_of_questions, questions_answers)
