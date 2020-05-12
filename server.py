from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 10
score = 0

flashcards = [
    {
        "id": 1,
        "term": "first position",
        "image": "../static/img/first_feet.jpg",
        "back": ["Heels together with toes pointing outwards.", "Aim for 180 degrees between feet."],
        "alt": "Photo of dancer's lower body with feet in first position",
        "division": "Foot",
    },
    {
        "id": 2,
        "term": "second position",
        "image": "../static/img/second_feet.jpg",
        "back": ["Heels apart.","Think of first position, then slide the heels out.", "Heels should be one to two feet apart.",
        "Keep knees turned out as well."],
        "alt": "Photo of dancer's lower body with feet in second position",
        "division": "Foot",
    },
    {
        "id": 3,
        "term": "third position",
        "image": "../static/img/third_feet.jpg",
        "back": ["Feet are connected with one foot in front of the other.","Place heel of one foot near the arch of the other."],
        "alt": "Photo of dancer's lower body with feet in third position",
        "division": "Foot",
    },
    {
        "id": 4,
        "term": "fourth position",
        "image": "../static/img/fourth_feet.jpg",
        "back": ["Similar to third position, but the feet are not touching.","Keep feet about one foot apart.",
        "Try to center your weight and upper body in between the two legs."],
        "alt": "Photo of dancer's lower body with feet in fourth position",
        "division": "Foot",
    },
    {
        "id": 5,
        "term": "fifth position",
        "image": "../static/img/fifth_feet.jpg",
        "back": ["The toes of one foot are aiming to touch the heel of the other foot.",
        "Think of fourth position, then slide feet so that they touch.",
        "Similar to third position, but more crossed."],
        "alt": "Photo of dancer's lower body with feet in fifth position",
        "division": "Foot",
    },
    {
        "id": 6,
        "term": "first position",
        "image": "../static/img/first_arms.jpg",
        "back": ["Arms are extended to the front in a circle.","Hands are almost touching.", "Wrists and hands should be slightly above the belly button."],
        "alt": "Photo of dancer's upper body with arms in first position",
        "division": "Arm",
    },
    {
        "id": 7,
        "term": "second position",
        "image": "../static/img/second_arms.jpg",
        "back": ["Arms open wide to the sides.", "Elbows slightly rounded and lifted.","Arms held at or slightly below shoulder height."],
        "alt": "Photo of dancer's upper body with arms in second position",
        "division": "Arm",
    },
    {
        "id": 8,
        "term": "third position",
        "image": "../static/img/third_arms.jpg",
        "back": ["One arm rounds in front, similar to first position.","Second arm extends to side similar to second position."],
        "alt": "Photo of dancer's upper body with arms in third position",
        "division": "Arm",
    },
    {
        "id": 9,
        "term": "fourth position",
        "image": "../static/img/fourth_arms.jpg",
        "back": ["One arm rounds in front, similar to first position.",
        "Second arm above head, think of moving one arm from first position until it is almost over the head.",
        "Keep fingers relaxed and elbows slightly bent."],
        "alt": "Photo of dancer's upper body with arms in fourth position",
        "division": "Arm",
    },
    {
        "id": 10,
        "term": "fifth position",
        "image": "../static/img/fifth_arms.jpg",
        "back": ["Both arms rounded, almost over head.", "Move arms from first position up about 80 degrees, keeping elbow position.",
        "Arms remain rounded into a circle.", "Avoid lifting shoulders."],
        "alt": "Photo of dancer's upper body with arms in fifth position",
        "division": "Arm",
    },
]

question = 10
answers = [
"placeholder",
    {
        "num": 1,
        "type": "mc1",
        "q": "Which of the following shows someone standing in first position?",
        "correct": "d",
        "a": "Incorrect. That's actually second position.",
        "b": "Incorrect. That's actually third position.",
        "c": "Incorrect. That's actually fifth position.",
        "d": "Correct!",
        "e": "Incorrect. That's actually fourth position.",
        "wrong": [],
        "choices": [],
        "alt": "",
        "pics": ["../static/img/second_feet.jpg", "../static/img/third_feet.jpg",
        "../static/img/fifth_feet.jpg","../static/img/first_feet.jpg", "../static/img/fourth_feet.jpg"],
        "correct_phrase": "In first position, the heels are together.",
    },
    {
        "num": 2,
        "type": "mc1",
        "q": "Which of the following shows someone standing in second position?",
        "correct": "e",
        "a": "Incorrect. That's actually first position.",
        "b": "Incorrect. That's actually third position.",
        "c": "Incorrect. That's actually fourth position.",
        "d": "Incorrect. That's Actually fifth position.",
        "e": "Correct!",
        "wrong": [],
        "choices" : [],
        "alt": "",
        "pics": ["../static/img/first_feet.jpg", "../static/img/third_feet.jpg",
        "../static/img/fourth_feet.jpg","../static/img/fifth_feet.jpg", "../static/img/second_feet.jpg"],
        "correct_phrase": "In second position, the heels are apart and facing inwards.",
    },
    {
        "num": 3,
        "type": "tf",
        "q": "Third position can be obtained by moving the feet from fifth position until they are fully crossed with the heel of each foot lining up with the toes of the other.",
        "correct": "false",
        "true": "Incorrect.", #This statement is actually reversed. In fifth position the feet are fully crossed, while in third position the heel of the font foot is aligned with the arch of the back foot.",
        "false": "Correct!",
        "wrong": [],
        "choices" : [],
        "pics": ["../static/img/third_feet.jpg", "../static/img/fifth_feet.jpg"],
        "alt": "",
        "correct_phrase": ["Third Position", "Fifth Position"],
    },
    {
        "num": 4,
        "type": "mc2",
        "q": "Which position is this dancer standing in?",
        "correct": "b",
        "a": "Incorrect." ,#Third position looks like this: <img src='../static/img/third_feet.jpg' height='200px' >",
        "b": "Correct!",
        "c": "Incorrect." ,#First position looks like this: <img src='../static/img/first_feet.jpg' height='200px' >",
        "d": "Incorrect.", #Second position looks like this: <img src='../static/img/second_feet.jpg' height='200px' >",
        "e": "Incorrect.", #Fifth position looks like this: <img src='../static/img/fifth_feet.jpg' height='200px' >",
        "choices": ["Third Position", "Fourth Position", "First Position", "Second Position", "Fifth Position"],
        "pics": ["../static/img/fourth_feet.jpg"],
        "alt": "Image of dancer's legs. Feet are turned out and separated with one foot in front of the other,, about 1 foot apart.",
        "wrong": [],
        "correct_phrase": "This is actually fourth position.",
    },
    {
        "num": 5,
        "type": "dd",
        "q": "Place the positions in order from First to Fifth:",
        "correct": ["c", "e", "b", "a", "d"],
        "a": "Incorrect. That's actually A position.",
        "b": "Incorrect. That's actually B position.",
        "c": "Incorrect. That's actually C position.",
        "d": "Incorrect. That's Actually D position.",
        "e": "Correct!",
        "wrong": [],
        "choices": ["First Position", "Second Position", "Third Position", "Fourth Position", "Fifth Position"],
        "pics": ["<img src='../../static/img/fourth_feet.jpg' height='100px'",
        "<img src='../../static/img/third_feet.jpg' height='100px'",
        "<img src='../../static/img/first_feet.jpg' height='100px'",
        "<img src='../../static/img/fifth_feet.jpg' height='100px'",
        "<img src='../../static/img/second_feet.jpg' height='100px'",],
        "alt": "",
        "correct_phrase": "In second position, the heels are apart and facing inwards.",
    },{
        "num": 6,
        "type": "mc1",
        "q": "Which of the following shows someone with their arms in fourth position?",
        "correct": "a",
        "a": "Correct!",
        "b": "Incorrect. That's actually second position.",
        "c": "Incorrect. That's actually first position.",
        "d": "Incorrect. That's actually fifth position.",
        "e": "Incorrect. That's actually third position.",
        "wrong": [],
        "choices": [],
        "alt": "",
        "pics": ["../static/img/fourth_arms.jpg", "../static/img/second_arms.jpg",
        "../static/img/first_arms.jpg","../static/img/fifth_arms.jpg", "../static/img/third_arms.jpg"],
        "correct_phrase": "In first position, the heels are together.",
    },
    {
        "num": 7,
        "type": "tf",
        "q": "In second position, the elbows are slightly bent and over the head in a circular position.",
        "correct": "false",
        "true": "Incorrect. This actually describes fifth position arms. In second position, the arms are wide and out to the sides.",
        "false": "Correct!",
        "wrong": [],
        "choices" : [],
        "pics": ["../static/img/second_arms.jpg", "../static/img/fifth_arms.jpg"],
        "alt": "",
        "correct_phrase": ["Second Position", "Fifth Position"],
    },
    {
        "num": 8,
        "type": "mc2",
        "q": "The dancer is holding their arms in which position?",
        "correct": "c",
        "a": "Incorrect.", #First position looks like this: <img src='../static/img/first_arms.jpg' height='200px' >",
        "b": "Incorrect.", # Second position looks like this: <img src='../static/img/second_arms.jpg' height='200px' >",
        "c": "Correct!",
        "d": "Incorrect.", # Fourth position looks like this: <img src='../static/img/fourth_arms.jpg' height='200px' >",
        "e": "Incorrect.", # Fifth position looks like this: <img src='../static/img/fifth_arms.jpg' height='200px' >",
        "choices": ["First Position", "Second Position", "Third Position", "Fourth Position", "Fifth Position"],
        "pics": ["../static/img/third_arms.jpg"],
        "wrong": ["../static/img/first_arms.jpg", "../static/img/second_arms.jpg", "correct", "../static/img/fourth_arms.jpg",
        "../static/img/fifth_arms.jpg"],
        "alt": "Image of dancer's armms. One arm is extended to the side, the other is rounded with fingertips inline with the bellybutton.",
        "correct_phrase": "This is actually Third position.",
    },
    {
        "num": 9,
        "type": "mc1",
        "q": "Which of the following shows someone with their arms in fifth position?",
        "correct": "c",
        "a": "Incorrect. That's actually second position.",
        "b": "Incorrect. That's actually third position.",
        "c": "Correct!",
        "d": "Incorrect. That's actually first position.",
        "e": "Incorrect. That's actually fourth position.",
        "wrong": [],
        "choices" : [],
        "pics": ["../static/img/second_arms.jpg", "../static/img/fourth_arms.jpg",
        "../static/img/fifth_arms.jpg","../static/img/first_arms.jpg", "../static/img/third_arms.jpg"],
        "alt": ["Image of dancer's arms. Arms are open and extended to the sides.",
        "Image of dancer's arms. One arm is extended to the side, the other is rounded with fingertips inline with the bellybutton.",
        "Image of dancer's arms. Arms are almost rounded and almost overhead.",
        "Image of dancer's arms. Arms are rounded and roughly inline with the bellybutton.",
        "Image of dancer's arms. One arm is rounded over the head, the other is rounded with fingertips inline with the bellybutton."],
        "correct_phrase": "In fifth position, the arms are rounded above the head.",
        "alt": "",
    },
    {
        "num": 10,
        "type": "dd",
        "q": "Match the arm positions to the corresponding foot positions:",
        "correct": ["a", "d", "e", "c", "b"],
        "a": "Incorrect. That's actually A position.",
        "b": "Incorrect. That's actually B position.",
        "c": "Incorrect. That's actually C position.",
        "d": "Incorrect. That's Actually D position.",
        "e": "Correct!",
        "wrong": [],
        "choices": ["../static/img/second_feet2.jpg", "../static/img/fifth_feet2.jpg", "../static/img/third_feet2.jpg",
        "../static/img/fourth_feet2.jpg", "../static/img/first_feet2.jpeg"],
        "pics": ["src='../static/img/second_arms2.jpg' height='120px'",
        "src='../static/img/first_arms2.jpg' height='120px'",
        "src='../static/img/fourth_arms2.jpg' height='120px'",
        "src='../static/img/fifth_arms2.jpg' height='120px'",
        "src='../static/img/third_arms2.jpg' height='120px'",],
        "correct_phrase": "In second position, the heels are apart and facing inwards.",
        "alt": "",
    },

]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def start_quiz(name=None):
    return render_template('quiz.html')

@app.route('/learn')
def learn(name=None):
    return render_template('learn.html')

@app.route('/flashcard/<id>')
def view(id=None):
    index = int(id)
    c = flashcards[0]
    for card in flashcards:
        if card["id"] == index:
            c = card
            break

    term = c["term"]
    image = c["image"]
    back = c["back"]
    division = c["division"]
    back_length = len(back)
    alt = c["alt"]
    return render_template('flashcard.html', id=id, term=term, image=image, alt=alt, back=back, back_length=back_length, division=division)

@app.route('/checkpoint')
def checkpoint(id=None):
    return render_template('checkpoint.html')

@app.route('/review/<num>')
def review(num=None):
    n = str(num)
    if len(n) < 3:
        rev = "review" + n + ".html"
        return render_template(rev)

@app.route('/test')
def test(id=None):
    return render_template('test.html')

@app.route('/quiz/<num>')
def quiz_question(num=None):
    n = str(num)
    p = int(n)
    if len(n) < 3:
        pics = answers[p]["pics"]
        q = answers[p]["q"]
        choices = answers[p]["choices"]
        type = answers[p]["type"]
        correct_phrase = answers[p]["correct_phrase"]
        wrong = answers[p]["wrong"]
        alt = answers[p]["alt"]
        if (p == 3) or (p == 7): # true/false questions
            return render_template("question_tf.html", score=score, pics=pics, n=n, q=q, type=type, correct_phrase=correct_phrase, wrong=wrong, alt=alt)
        elif (p == 5) or (p == 10): # drag/drop questions
            return render_template("question_dd.html", score=score, pics=pics, n=n, q=q, choices=choices, type=type, correct_phrase=correct_phrase,wrong=wrong, alt=alt)
        else: # multiple choice question
            return render_template("question_mc.html", score=score, pics=pics, n=n, q=q, choices=choices, type=type, correct_phrase=correct_phrase, wrong=wrong, alt=alt)

@app.route('/quiz')
def quiz(id=None):
    return render_template("quiz.html")

@app.route('/finish')
def finish(id=None):
    global score
    return render_template("finish.html", score=score)

@app.route('/classes')
def classes(id=None):
    return render_template("classes.html")

@app.route('/drag')
def drag(id=None):
    global non_ppc_people
    global ppc_people
    return render_template("drag.html", non_ppc_people=non_ppc_people, ppc_people=ppc_people)

@app.route('/check_answer', methods=['GET', 'POST'])
def check_answer(id=None):
    global answers
    global score
    global flashcards

    data = request.get_json()
    question = int(data["question"])
    answer = data["answer"]
    feedback = ""
    is_correct = 1
    correct = answers[question]["correct"]
    type = answers[question]["type"]


    if type is "dd":
        feedback = []
        for i in range(5):
            if answer[i] != answers[question]["correct"][i]:
                is_correct = 0
                feedback.append(0)
            else:
                feedback.append(1)

        if is_correct == 1:
            score = score + 1
    else:
        feedback = answers[question][answer]
        if answers[question]["correct"] == answer:
            score = score + 1

    return jsonify(feedback=feedback, score=score, correct=correct)


if __name__ == '__main__':
   app.run(debug = True)
