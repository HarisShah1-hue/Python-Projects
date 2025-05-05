import time

q = [
    {
        "Topic": "Strings",
        "Question": "How would you count the number of vowels in a given string in Python?",
        "Key": ["count()", "for loop", "if char in 'aeiou'", ".lower()"]
    },
    {
        "Topic": "List",
        "Question": "How do you add a new element to the end of a list?",
        "Key": [".append()", "list.append(value)", "mutable", "in-place operation"]
    },
    {
        "Topic": "Tuple",
        "Question": "How do you access the first element of a tuple?",
        "Key": ["Tuple[0]", "indexing", "zero-based index", "immutable"]
    },
    {
        "Topic": "Function",
        "Question": "How do you define a function that adds two numbers?",
        "Key": ["sum()", "def", "return", "parameters"]
    }
]



user_key = []
d_score = []
def evaluate(answer,key):
  score = 0
  for k in key:
    if k.lower() in answer.lower():
      score +=1
  return round((score / len(key)) * 100)

def WelCome():
  print("Welcome To The Mock Interview...!\n")
  for i in q:
    print("Topic :",i['Topic'], "\n")
    print("Question: ", i['Question'], "\n")
    user = input("Answer the above question: ")
    user_key.append(user)
    s = evaluate(user,i['Key'])
    d_score.append(s)
    print(f"\nConfidence score is : {s}% \n ")
    print("________________________________________", "\n")
    time.sleep(0.5)

  print("Feedback from Model on Interview: \n ")
  for j, r in enumerate(q):
    print(f"{j + 1} Topic: {r['Topic']} \n")
    print(f"Question: {r['Question']}")
    print(f"Your answer is : {user_key[j]}")
    print(f"Expected Keywords: {r['Key']}")
    print(f"Confidence score of this question: {d_score[j]}% \n")

WelCome()
