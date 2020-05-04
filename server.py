from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 2
score = 0
non_ppc_people = [
"Phyllis",
"Dwight",
"Oscar",
"Creed",
"Pam",
"Jim",
"Stanley",
"Michael",
"Kevin",
"Kelly"
]
ppc_people = [
"Angela"
]
flashcards = [
    {
        "id": 1,
        "term": "first position",
        "image": "../static/img/first_feet.jpg",
        "back": ["Heels Together with toes pointing outwards", "Aim for 180 degrees between feet","If 180 degrees is not possible, think of defining a large slice of pie between your feet."],
        "tip": "Make sure to turnout your entire leg starting at the hip, not just at your ankles. This may mean the angle between your feet has to be smaller than 180 degrees. It's better to have your feet 90 degrees apart with proper turnout.",
        "division": "Foot",
    },
    {
        "id": 2,
        "term": "second position",
        "image": "../static/img/second_feet.jpg",
        "back": ["Heels Apart","Think of first position, but  moving heels out", "Heels one to two feet apart"],
        "tip": "Keep knees turned out as well.",
        "division": "Foot",
    },
    {
        "id": 3,
        "term": "third position",
        "image": "../static/img/third_feet.jpg",
        "back": ["Feet connected, one foot in front of the other","Heel of one foot near arch of the other"],
        "tip": "You can get into this position by sliding one foot from first position along the inside of the other; this will help you hold your turnout.",
        "division": "Foot",
    },
    {
        "id": 4,
        "term": "fourth position",
        "image": "../static/img/fourth_feet.jpg",
        "back": ["Similar to third position, but feet are not touching","Keep feet about one foot apart"],
        "tip": "Try to center your weight and body in between the two legs.",
        "division": "Foot",
    },
    {
        "id": 5,
        "term": "fifth position",
        "image": "../static/img/fifth_feet.jpg",
        "back": ["Toes of right foot aiming touch heel of left foot and vice versa",
        "Think fourth position, then slide feet so that they touch",
        "Similar to third position, but more crossed"],
        "tip": "Check your turnout by bending knees slightly and checking that your knees track over your toes.",
        "division": "Foot",
    },
    {
        "id": 6,
        "term": "first position",
        "image": "../static/img/first_arms.jpg",
        "back": ["Arms are extended to the front in a circle","Hands almost touching", "Wrists and hands should be slightly above the belly button"],
        "tip": "Check your turnout by bending knees slightly and checking that your knees track over your toes.",
        "division": "Arm",
    },
    {
        "id": 7,
        "term": "second position",
        "image": "../static/img/second_arms.jpg",
        "back": ["Arms open wide to the sides", "Elbows slightly rounded and lifted","Arms held at or slightly below shoulder height"],
        "tip": "Check your turnout by bending knees slightly and checking that your knees track over your toes.",
        "division": "Arm",
    },
    {
        "id": 8,
        "term": "third position",
        "image": "../static/img/third_arms.jpg",
        "back": ["One arm rounds in front, similar to first position","Second arm extends to side similar to second position"],
        "tip": "Check your turnout by bending knees slightly and checking that your knees track over your toes.",
        "division": "Arm",
    },
    {
        "id": 9,
        "term": "fourth position",
        "image": "../static/img/fourth_arms.jpg",
        "back": ["One arm rounds in front, similar to first position",
        "Second arm above head, think of moving one arm from first position until it is almost over the head",
        "Keep fingers relaxes and elbows slightly bent"],
        "tip": "Check your turnout by bending knees slightly and checking that your knees track over your toes.",
        "division": "Arm",
    },
    {
        "id": 10,
        "term": "fifth position",
        "image": "../static/img/fifth_arms.jpg",
        "back": ["Both arms rounded, almost over head", "Move arms from first position up about 80 degrees, keeping elbow position",
        "Arms remain rounded into a circle"],
        "tip": "Check your turnout by bending knees slightly and checking that your knees track over your toes.",
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
        "pics": ["../static/img/first_feet.jpg", "../static/img/third_feet.jpg",
        "../static/img/fourth_feet.jpg","../static/img/fifth_feet.jpg", "../static/img/second_feet.jpg"],
        "correct_phrase": "In second position, the heels are apart and facing inwards.",
    },
    {
        "num": 3,
        "type": "tf",
        "q": "Third position can be obtained by moving the feet from fifth position until they are fully crossed with the heel of each foot lining up with the toes of the other.",
        "correct": "false",
        "true": "Incorrect. This statement is actually reversed. In fifth position the feet are fully crossed, while in third position the heel of the font foot is aligned with the arch of the back foot.",
        "false": "Correct!",
        "wrong": [],
        "choices" : [],
        "pics": ["../static/img/third_feet.jpg", "../static/img/fifth_feet.jpg"],
        "correct_phrase": ["Third Position", "Fifth Position"],
    },
    {
        "num": 4,
        "type": "mc2",
        "q": "Which position is this dancer standing in?",
        "correct": "b",
        "a": "Incorrect. Third position looks like this",
        "b": "Correct!",
        "c": "Incorrect. First position looks like this: ",
        "d": "Incorrect. Second position looks like this: ",
        "e": "Incorrect. Fifth position looks like this: ",
        "choices": ["Third Position", "Fourth Position", "First Position", "Second Position", "Fifth Position"],
        "pics": ["../static/img/fourth_feet.jpg"],
        "wrong": ["../static/img/first_feet.jpg", "../static/img/second_feet.jpg", "../static/img/third_feet.jpg",
        "correct","../static/img/fifth_feet.jpg"],
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
        "pics": ["<img src='../../static/img/fourth_feet.jpg' height='100px'>",
        "<img src='../../static/img/third_feet.jpg' height='100px'>",
        "<img src='../../static/img/first_feet.jpg' height='100px'>",
        "<img src='../../static/img/fifth_feet.jpg' height='100px'>",
        "<img src='../../static/img/second_feet.jpg' height='100px'>",],
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
        "correct_phrase": ["Third Position", "Fifth Position"],
    },
    {
        "num": 8,
        "type": "mc2",
        "q": "The dancer is holding their arms in which position?",
        "correct": "c",
        "a": "Incorrect. First Position arms look like this: ",
        "b": "Incorrect. Second Position arms look like this: ",
        "c": "Correct! This is third position.",
        "d": "Incorrect. Fourth position looks like this: ",
        "e": "Incorrect. Fifth position look like this: ",
        "choices": ["First Position", "Second Position", "Third Position", "Fourth Position", "Fifth Position"],
        "pics": ["../static/img/third_arms.jpg"],
        "wrong": ["../static/img/first_arms.jpg", "../static/img/second_arms.jpg", "correct", "../static/img/fourth_arms.jpg",
        "../static/img/fifth_arms.jpg"],
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
        "correct_phrase": "In fifth position, the arms are rounded above the head.",
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
        "../static/img/fourth_feet2.jpg", "../static/img/first_feet2.jpg"],
        "pics": ["src='../static/img/second_arms2.png' height='70px'",
        "src='../static/img/first_arms2.png' height='70px'",
        "src='../static/img/fourth_arms2.png' height='70px'",
        "src='../static/img/fifth_arms2.png' height='70px'",
        "src='../static/img/third_arms2.png' height='70px'",],
        "correct_phrase": "In second position, the heels are apart and facing inwards.",
    },

]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def start_quiz(name=None):
    return render_template('quiz.html')

@app.route('/faq')
def faq(name=None):
    return render_template('faq.html')

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
    tip = c["tip"]
    division = c["division"]
    back_length = len(back)
    print(image)
    return render_template('flashcard.html', id=id, term=term, image=image, back=back, back_length=back_length, tip=tip, division=division)

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
        if (p == 3) or (p == 7): # true/false questions
            return render_template("question_tf.html", score=score, pics=pics, n=n, q=q, type=type, correct_phrase=correct_phrase, wrong=wrong)
        elif (p == 5) or (p == 10): # drag/drop questions
            return render_template("question_dd.html", score=score, pics=pics, n=n, q=q, choices=choices, type=type, correct_phrase=correct_phrase,wrong=wrong)
        else: # multiple choice question
            return render_template("question_mc.html", score=score, pics=pics, n=n, q=q, choices=choices, type=type, correct_phrase=correct_phrase, wrong=wrong)

@app.route('/quiz')
def quiz(id=None):
    return render_template("quiz.html")

@app.route('/finish')
def finish(id=None):
    return render_template("finish.html")

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


    if question == 5 or question == 10:
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
