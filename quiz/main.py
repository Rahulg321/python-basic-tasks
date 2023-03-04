def main():
    quiz = {
        'question1':{
            "question":"What is the capital of France?",
            "answer":"Paris"
        },
        'question2':{
            "question":"What is the capital of Germany?",
            "answer":"Berlin"
        },
        'question3':{
            "question":"What is the capital of India?",
            "answer":"Delhi"
        },
        'question4':{
            "question":"What is the capital of U.S.A?",
            "answer":"WASHINGTON DC"
        },
        'question5':{
            "question":"What is the capital of Italy?",
            "answer":"Rome"
        },
        'question6':{
            "question":"What is the capital of Spain?",
            "answer":"Madrid"
        },
        'question7':{
            "question":"What is the capital of Portugal?",
            "answer":"Lisbon"
        },
        'question8':{
            "question":"What is the capital of Austria?",
            "answer":"Vienna"
        }
    }

    score = 0
    for key,value in quiz.items():
        print(value['question'])
        answer = input("Answer: ")
        
        if answer.lower() == value['answer'].lower():
            score += 1
            
    print(f'Your score is {score}/8')
        
        
main()