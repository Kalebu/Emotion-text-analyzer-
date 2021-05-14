from textblob import TextBlob

feedbacks = ['I love the app is amazing ',
             "The experience was bad as hell",
             "This app is really helpful",
             "Damn the app tastes like shit ",
             'Please don\'t download the app you will regret it ']

positive_feedbacks = []
negative_feedbacks = []

for feedback in feedbacks:
    feedback_polarity = TextBlob(feedback).sentiment.polarity
    if feedback_polarity > 0:
        positive_feedbacks.append(feedback)
        continue
    negative_feedbacks.append(feedback)

print('Positive_feebacks Count : {}'.format(len(positive_feedbacks)))
print(positive_feedbacks)
print('Negative_feedback Count : {}'.format(len(negative_feedbacks)))
print(negative_feedbacks)
