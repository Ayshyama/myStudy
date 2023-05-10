# 09.05.2023
# Task - Highscore

participants = ['Brian', 'Britney', 'Ben']
scores = {
  'brian': 25,
  'britney': 80,
  'ben': 50
}



def get_score(name):
    lowercase_name = name.lower()
    if lowercase_name not in scores:
        print(f"{name} did not participate")
    else:
        score = scores[lowercase_name]
        print(f"{name} scored {score} points")

get_score('Paul')
get_score('Britney')