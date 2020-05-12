'''
generates set of randomised mcq papers for list of indian states
'''

import random
import os

noOfQuestions = 25
noOfSets = 2

capitals = {'Andhra Pradesh':'Hyderabad (Proposed Amaravati)', 'Arunachal Pradesh':'Itanagar', 'Assam':'Dispur', 'Bihar':'Patna', 'Chhattisgarh':'Raipur', 'Goa':'Panaji', 'Gujarat':'Gandhinagar', 'Haryana':'Chandigarh', 'Himachal Pradesh':'Shimla', 'Jammu and Kashmir':'Srinagar/Jammu', 'Jharkhand':'Ranchi', 'Karnataka':'Bengaluru', 'Kerala':'Thiruvananthapuram', 'Madhya Pradesh':'Bhopal', 'Maharashtra':'Mumbai', 'Manipur':'Imphal', 'Meghalaya':'Shillong', 'Mizoram':'Aizawl', 'Nagaland':'Kohima', 'Odisha':'Bhubaneswar', 'Punjab':'Chandigarh', 'Rajasthan':'Jaipur', 'Sikkim':'Gangtok', 'Tamil Nadu':'Chennai', 'Telangana':'Hyderabad', 'Tripura':'Agartala', 'Uttar Pradesh':'Lucknow', 'Uttarakhand':'Dehradun', 'West Bengal':'Kolkata', 'Andaman and Nicobar Islands':'Port Blair', 'Chandigarh':'Chandigarh', 'Dadar and Nagar Haveli':'Silvassa', 'Daman and Diu':'Daman', 'Delhi':'Delhi', 'Lakshadweep':'Kavaratti', 'Puducherry':'Pondicherry', }

os.makedirs('raw_data/quiz_texts/')
#genarate 'noOfSets' quiz files
for quizNum in range(noOfSets):
    #create the files
    quizFile=open('raw_data/quiz_texts/capitals_quiz%s.txt' %(quizNum+1), 'w')
    answFile=open('raw_data/quiz_texts/capitals_quiz_answers%s.txt' %(quizNum+1), 'w')

    #add quiz headers
    quizFile.write('*****INDIA CAPITALS QUIZ*****\n\n')
    quizFile.write('Name:\n\nDate:\n\nNumber:\n\n')
    quizFile.write((' ' * 30) + 'Question Set: %s\n\n' %(quizNum + 1))

    #add answer headers
    answFile.write('answers for question set number %s\n\n' %(quizNum + 1))

    # TODO: shuffle order of states
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: loop through states 'noOfQuestions' times and generate 4 options
    for questionNum in range(noOfQuestions):
        #generate 4 options
        correctAns = capitals[states[questionNum]]
        wrongAns = list(capitals.values())
        wrongAns.remove(correctAns)
        random.shuffle(wrongAns)
        wrongAns = wrongAns[:3]
        answerOptions = wrongAns + [correctAns]
        random.shuffle(answerOptions)

        # write qs and answerOptions to file
        quizFile.write('%s. What is the capital of ' %(questionNum+1) + states[questionNum] + '?\n')
        for i in range(len(answerOptions)):
            quizFile.write('    ' + 'ABCD'[i] + '. ' + answerOptions[i] + '\n')
        quizFile.write('\n')

        # write answer key
        answFile.write('%s. %s\n' %(questionNum + 1, 'ABCD'[answerOptions.index(correctAns)]))

quizFile.close()
answFile.close()
