'''
******************************
CS 1026 - Assignment 3 – YouTube Emotions
Code by: Annas Amar
Student ID: aamar9@uwo.ca
File created: November 16
******************************
This is the emotion file for my assignment. It contains all the functions needed to generate a report about the comments with the parameters from my main file. This file contains 5 functions, with the first's purpose to be to clean a comment into a desired format. The second is to make a dictionary will all our keywords. The third is to classify comments into a specific emotion. The fourth is to make a list of all comments based off their country. The last is to make a report using all the data we have gathered from the previous functions.
'''
# you can not add any import lines to this file

#All possible emotions that can be found
EMOTIONS = ['anger', 'joy', 'fear', 'trust', 'sadness', 'anticipation']

def clean_text(comment):
    #Converts entire string into lowercase characters
    comment = comment.lower()
    #Create new string for the cleaned comment
    cleaned_comments =''
    for element in comment:
        # Check if character is space or letter, and will add it to cleaned string or else it will not add it.
        if element.isspace() or element.isalpha():
            cleaned_comments += element
        else:
            cleaned_comments += ' '
    return cleaned_comments

def make_keyword_dict(keyword_file_name):
    #Creates an empty dictionary to store finished nested data
    key_dict = {}

    #Open keyword_file_name
    with open (keyword_file_name, "r") as file:
        #This whole section reads lines, splits the words so that it can be inserted into the dictionaries
        for line in file:
            if line.strip():
                split = line.strip().split('\t')
                key_dict[split[0]] = {
                    'anger': int(split[1]),
                    'joy': int(split[2]),
                    'fear': int(split[3]),
                    'trust': int(split[4]),
                    'sadness': int(split[5]),
                    'anticipation': int(split[6])
                }
        #Return our keyword dictionary
        return key_dict
    pass

def classify_comment_emotion(comment_text, keywords):
    #Create new dictionary and each key is from EMOTIONS list and all values are initialized at 0
    emotion_scores = {emotion: 0 for emotion in EMOTIONS}

    # Clean the comment text
    cleaned_comment = clean_text(comment_text)

    # Split the cleaned text into words
    words = cleaned_comment.split()

    # Calculate emotion scores based on keywords
    for word in words:
        if word in keywords:
            for emotion, score in keywords[word].items():
                emotion_scores[emotion] += int(score)

    # Determine the dominant emotion using max and lambda
    max_emotion = max(EMOTIONS, key=lambda emotion: (emotion_scores[emotion], -EMOTIONS.index(emotion)))

    return max_emotion

def make_comments_list(filter_country, comments_file_name):
    #Creates list to store comments
    comments = []
    #Open comments_file_name
    with open(comments_file_name, "r") as file:
        #Read all lines
        lines = file.readlines()
        #strip lines and split them by comma
        for line in lines:
            line = line.strip()
            splits = line.split(',', 3)
            comment_id, username, country, text = splits
            text = text.strip()
            #Create a dictionary for comment
            comment_dict = {
                'comment_id': int(comment_id),
                'username': str(username),
                'country': str(country),
                'text': str(text)}

            #Checks for country filter and appends the comment dict to the list
            if filter_country.lower() == 'all':
                comments.append(comment_dict)
            elif country.lower() == filter_country.lower():
                comments.append(comment_dict)

        return comments
    pass

def make_report(comment_list, keywords, report_filename):
    #If there are no comments then throw this error
    if not comment_list:
        raise RuntimeError("No comments in dataset!")

    #Create a dictionary to count the occurrence of emotion for every comment
    emotion_count = dict.fromkeys(EMOTIONS, 0)

    #This will classify every single comment and update our emotion counter
    for comment in comment_list:
        comment_text = comment['text']
        emotion = classify_comment_emotion(comment_text, keywords)
        emotion_count[emotion] += 1

    # Determine the dominant emotion in all our comments using max and lambda
    max_emotion = max(EMOTIONS, key=lambda emotion: (emotion_count[emotion], -EMOTIONS.index(emotion)))

    total_comment_count = sum(emotion_count.values())

    #Make the report content
    report_lines = []
    report_lines.append(f"Most common emotion: {max_emotion}")
    report_lines.append("Emotion Totals")

    for emotion in EMOTIONS:
        #Find percentage
        count = emotion_count[emotion]
        percentage = (count / total_comment_count)*100
        #Round percent
        percentage = round(percentage, 2)

        #Next segment if code will either format percentage to 1 or 2 decimal points
        if percentage.is_integer():
            percentage_string = f"{int(percentage)}.0%"
        else:
            percentage_string = f"{percentage}%"
        report_lines.append(f"{emotion}: {count} ({percentage_string})")

        #This will write the report into another file
        with open(report_filename, 'w') as file:
            for line in report_lines:
                file.write(line + '\n')

    return max_emotion

    pass


