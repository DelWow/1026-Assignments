'''
******************************
CS 1026 - Assignment 3 – YouTube Emotions
Code by: Annas Amar
Student ID: aamar9@uwo.ca
File created: November 16
******************************
This is the main file for my assignment. It contains all the valid country's comments can come from as well as asking the user for keyword filename, comment filename, country and report file name. It then uses all this to generate a report for the comments within set parameters.
'''
# do not add any additional import lines to this file.

import os.path
from emotions import *

#All valid countries
VALID_COUNTRIES = ['bangladesh', 'brazil', 'canada', 'china', 'egypt',
                   'france', 'germany', 'india', 'iran', 'japan', 'mexico',
                   'nigeria', 'pakistan', 'russia', 'south korea', 'turkey',
                   'united kingdom',  'united states']


def ask_user_for_input():
    #Ask user for keyword file name and considers any possible errors
    keyword_filename = input("Input keyword file (ending in .tsv): ")
    if not keyword_filename.endswith('.tsv'):
        raise ValueError("Keyword file does not end in .tsv!")
    if not os.path.exists(keyword_filename):
        raise IOError(f"{keyword_filename} does not exist!")

    # Ask user for comment file name and considers any possible errors
    comment_filename = input("Input comment file (ending in .csv): ")
    if not comment_filename.endswith('.csv'):
        raise ValueError("Comments file does not end in .csv!")
    if not os.path.exists(comment_filename):
        raise IOError(f"{comment_filename} does not exist!")

    # Ask user for country and considers any possible errors
    country = input('Input a country to analyze (or "all" for all countries): ').lower()
    #Check if country is valid
    if country != 'all' and country not in VALID_COUNTRIES:
        raise ValueError(f"{country} is not a valid country to filter by!")

    # Ask user for report file name and considers any possible errors
    report_filename = input("Input the name of the report file (ending in .txt): ")
    if not report_filename.endswith('.txt'):
        raise ValueError("Report file does not end in .txt!")
    if os.path.exists(report_filename):
        raise IOError(f"{report_filename} already exists!")

    #Returns our values as a tuple
    return keyword_filename, comment_filename, country, report_filename

    pass


def main():
    while True:
        try:
            #Ask the user for inputs
            keyword_filename, comment_filename, country, report_filename = ask_user_for_input()
            #If the inputs are valid then we can break from loop
            break
        except Exception as e:
            #Output the error message and continues prompting
            print(f"Error: {e}")
    pass
    try:
        # Create the keywords dictionary
        keywords = make_keyword_dict(keyword_filename)

        # Create the comments list
        comment_list = make_comments_list(country, comment_filename)

        # Create report
        most_common_emotion = make_report(comment_list, keywords, report_filename)

        # Print most common emotion
        print(f"Most common emotion is: {most_common_emotion}")

    except RuntimeError as e:
        # make_report raises a RuntimeError, output the message
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
