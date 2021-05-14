# [Emotion-text-analyzer](https://kalebujordan.dev/how-to-detect-emotions-associated-with-text-using-python/)

This project demostrates how to approach building a program that can help in analyzing emotions or sometimes known as sentiment associated with textual data.

## Getting started

To get started with this script, you have to clone or download the repository just as shown below;

```bash
git clone https://github.com/Kalebu/Emotion-text-analyzer-
cd Emotion-text-analyzer-
Emotion-text-analyzer--> 
```

## Dependencies

In this project, I used [textblob](https://textblob.readthedocs.io/en/dev/) as natural language processing library(NLP),therefor you to make sure it installed before running.

```bash
pip install textblob
```

## textblob ?

With textblob you can detect the sentiment analysis of a text in just one line, just as shown below;

```python
>>> from textblob import TextBlob
>>> TextBlob('cool just like this').sentiment.polarity
0.35
```

## Demo Project

The [app.py](https://github.com/Kalebu/Emotion-text-analyzer-/blob/master/app.py) demostrates how you can use that simplicity in real life by analyzing customer reviews or feebacks. 

### Examples of feedbacks 

Feebacks Examples are included directly in the source code but in mostly cases you may be reading data from somewhere in your file system or even from cloud, this is just to show you hows it done.

```python
feedbacks = ['I love the app is amazing ',
             "The experience was bad as hell",
             "This app is really helpful",
             "Damn the app tastes like shit ",
             'Please don\'t download the app you will regret it ']

```

### Running

Now your script and you will realize textblob has correctly grouped and counted negative reviews vs positive reviews 

```bash
Positive_feebacks Count : 2
['I love the app is amazing ', 'This app is really helpful']
Negative_feedback Count : 3
['The experience was bad as hell', 'Damn the app tastes like shit ', "Please don't download the app you will regret it "]

```

## Issues ?

Did you face any issue while trying to run the project, raise one and I'm looking forward fixing it as soon as I can.


## Contribution ?

Have something to add to the source code to make it more legit;

- fork it
- add your changes
- update documentation
- submit a pull request

## Credits

All the credits to [Kalebu](https://github.com/Kalebu)

## Where to find me ?

- [Personal Blog](https://kalebujordan.dev/)
- [Telegram](https://t.me/kalebujordan) 
- [LinkedIn](https://www.linkedin.com/in/kalebu-gwalugano/) 
- [Twitter](https://twitter.com/j_kalebu) 
- [Instagram](https://www.instagram.com/kalebu_jordan/) 
- [Facebook](https://web.facebook.com/kalebu.jordan)
- isaackeinstein(at)gmail.com