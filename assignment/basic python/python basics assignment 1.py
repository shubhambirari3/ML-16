#!/usr/bin/env python
# coding: utf-8

# In[ ]:
###Question: create different functions to validate the data and create exceptions if required

#Accept roll number

#Create a function to accept n number of subject marks

#accept out of marks

#subject name

#return one dictionary like

#{1: {“English”:67/100 , “Hindi”:45/50, “Sanskrit”: 30/50, “MAths”: 89/100, ‘total’: 231/400, ‘per’:57.75%} ,




#Code:

class InvalidRollNumber(Exception):
    pass

class InvalidMarks(Exception):
    pass

def validate_roll_number(roll_number):
    # Check if roll number is valid (e.g. it's an integer between 1 and 1000)
    if not isinstance(roll_number, int) or roll_number < 1 or roll_number > 1000:
        raise InvalidRollNumber(f"Invalid roll number: {roll_number}")

def validate_marks(subject_marks, out_of_marks):
    # Check if all subject marks are valid (e.g. they're integers between 0 and out_of_marks)
    if not all(isinstance(m, int) and 0 <= m <= out_of_marks for m in subject_marks):
        raise InvalidMarks(f"Invalid subject marks: {subject_marks}")

def calculate_total_and_percentage(subject_marks, out_of_marks):
    total_marks = sum(subject_marks)
    total_out_of_marks = len(subject_marks) * out_of_marks
    percentage = (total_marks / total_out_of_marks) * 100
    return total_marks, total_out_of_marks, percentage

def create_marks_dict(roll_number, subject_names, subject_marks, out_of_marks):
    # Validate inputs
    validate_roll_number(roll_number)
    validate_marks(subject_marks, out_of_marks)

    # Calculate total marks and percentage
    total_marks, total_out_of_marks, percentage = calculate_total_and_percentage(subject_marks, out_of_marks)

    # Create dictionary
    marks_dict = {
        "roll_number": roll_number,
        "subjects": {}
    }

    for i, name in enumerate(subject_names):
        marks_dict["subjects"][i+1] = {name: f"{subject_marks[i]}/{out_of_marks}"}

    marks_dict["subjects"]["total"] = f"{total_marks}/{total_out_of_marks}"
    marks_dict["subjects"]["percentage"] = f"{percentage:.2f}%"

    return marks_dict

# Get user input
roll_number = int(input("Enter roll number: "))
subject_names = input("Enter subject names (comma-separated): ").split(",")
subject_marks = [int(m) for m in input("Enter subject marks (comma-separated): ").split(",")]
out_of_marks = int(input("Enter out of marks: "))

# Create marks dictionary
marks_dict = create_marks_dict(roll_number, subject_names, subject_marks, out_of_marks)

# Print marks dictionary
print(marks_dict)







