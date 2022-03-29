from tkinter import *
from random import *
import random

user_answer = []

root = Tk()

root.title("QUIZ MANIA")
root.geometry("650x600")
root.config(background="#ffffff")
root.resizable(0, 0)
ques = 1


def start_quiz():
    play_type = Label(
        root,
        text="How would you like to play?",
        font=("Centaur", 30, "bold"),
        foreground="brown",
        width=500,
        anchor="center",
        justify="center",
        wraplength=400,
    )
    play_type.pack()

    def show_result():
        Qprompt.destroy()
        Option_A.destroy()
        Option_B.destroy()
        Option_C.destroy()
        Option_D.destroy()
        global score
        if score > 2:
            label_result_text = Label(
                root,
                text=f"Good Job",
                background="#ffffff",
                font=('Times', 30),
            )
        else:
            label_result_text = Label(
                root,
                text=f"Better luck next time",
                background="#ffffff",
                font=('Times', 30),
            )
        stop=Button(
            text="Quit",
            font=("Times",24),
            command=quit,
            background="black",
            foreground="yellow"
        )
        stop.pack(pady=(20,20))
        label_result_text.pack(pady=(100, 20))
        label_result_text.configure(text=f"Your score is {score}")

    def calc():
        global indexes, user_answer, Answers, Questions,score
        x = 0
        result = []
        for i in indexes:
            if int(user_answer[i]) == int(Answers[i]):
                result.append('c')
        score=len(result)
        show_result()

    def selected():
        global radio, user_answer, Questions
        global indexes, Answers, ques
        global Qprompt, Option_A, Option_B, Option_C, Option_D
        ans_list = []
        for j in indexes:
            ans_list.append(Answers[j])
            x = radio.get()
            user_answer.append(x)
            radio.set(-1)
        if ques < 5:
            Qprompt.config(text=Questions[indexes[ques]][0])
            Option_A['text'] = Questions[indexes[ques]][1]
            Option_B['text'] = Questions[indexes[ques]][2]
            Option_C['text'] = Questions[indexes[ques]][3]
            Option_D['text'] = Questions[indexes[ques]][4]
            ques = ques + 1
        else:
            calc()

    def admin_menu():
        quiz_bank = Label(
            root,
            text="Quiz Banks",
            font=("Centaur", 30, "bold"),
            background="grey",
            foreground="brown",
            anchor="center"
        )
        quiz_bank.pack()
        Computer = Button(
            root,
            text="Computer",
            font=("Centaur", 30, "bold"),
            background="black",
            foreground="yellow",
            justify="center",
        )
        Computer.pack(pady=(20, 0))
        Science = Button(
            root,
            text="Science",
            font=("Centaur", 30, "bold"),
            background="black",
            foreground="yellow",
            justify="center",

        )
        Science.pack(pady=(10, 0))

    def authenticate():
        play_type.destroy()
        player.destroy()
        shut_down.destroy()
        admin.destroy()
        admin_menu()

    admin = Button(
        root,
        text="administrator",
        font=("Centaur", 30, "bold"),
        background="black",
        foreground="yellow",
        justify="center",
        command=authenticate,

    )
    admin.pack(pady=(10, 0))

    def player_menu():
        play_type.destroy()
        player.destroy()
        shut_down.destroy()
        admin.destroy()
        quiz_bank = Label(
            root,
            text="Quiz Bank Choices",
            font=("Centaur", 30, "bold"),
            background="grey",
            foreground="brown",
            anchor="center"
        )

        quiz_bank.pack()

        def BrainTeasers():
            Science.destroy()
            mix.destroy()
            quiz_bank.destroy()
            computer.destroy()
            hq = open("brainteasers.txt")
            global Qprompt, Option_A, Option_B, Option_C, Option_D, indexes, radio, Answers, Questions
            Qstring = hq.read()
            Questions = eval(Qstring)
            ha = open("brainteasers_ans.txt")
            ans_string = ha.read()
            Answers = eval(ans_string)
            indexes = []
            j = (len(Questions) - 1)
            i=0
            while i < 5:
                num = int(random.randint(0, j))
                if num not in indexes:
                    indexes.append(num)
                    i += 1
                else:
                    pass
            radio = IntVar()
            radio.set(-1)
            Qprompt = Label(
                root,
                text=Questions[indexes[0]][0],
                font=("Centaur", 24, "bold"),
                background="grey",
                foreground="brown",
                justify="center",
                wraplength=700,
            )

            Qprompt.pack(pady=(40, 20))
            Option_A = Radiobutton(
                root,
                text=Questions[indexes[0]][1],
                font=("Centaur", 24, "bold"),
                value=1,
                background="#ffffff",
                variable=radio,
                command=selected,
            )
            Option_A.pack(pady=(10, 0))
            Option_B = Radiobutton(
                root,
                text=Questions[indexes[0]][2],
                font=("Centaur", 24, "bold"),
                value=2,
                background="#ffffff",
                variable=radio,
                command=selected,
            )
            Option_B.pack(pady=(10, 0))
            Option_C = Radiobutton(
                root,
                text=Questions[indexes[0]][3],
                font=("Centaur", 24, "bold"),
                value=3,
                background="#ffffff",
                variable=radio,
                command=selected,
            )
            Option_C.pack(pady=(10, 0))
            Option_D = Radiobutton(
                root,
                text=Questions[indexes[0]][4],
                font=("Centaur", 24, "bold"),
                value=4,
                background="#ffffff",
                variable=radio,
                command=selected,
            )
            Option_D.pack(pady=(10, 0))

        computer = Button(
            root,
            text="COMPUTER",
            font=("Centaur", 30, "bold"),
            background="black",
            foreground="yellow",
            justify="center",
            command=BrainTeasers,
        )
        computer.pack(pady=(20, 0))
        def Science():
            Science.destroy()
            mix.destroy()
            quiz_bank.destroy()
            computer.destroy()
            hq = open("Sq.txt")
            global Qprompt, Option_A, Option_B, Option_C, Option_D, indexes, radio, Answers, Questions
            Qstring = hq.read()
            Questions = eval(Qstring)
            ha = open("Sa.txt")
            ans_string = ha.read()
            Answers = eval(ans_string)
            indexes = []
            j = (len(Questions) - 1)
            i=1
            while i < 11: 
                num_=random.randint(0,len(Questions)-1)
                if num_ not in indexes:
                    indexes.append(num_)
                    i+=1      
            radio = IntVar()
            radio.set(-1)
            Qprompt = Label(
                root,
                text=Questions[indexes[0]][0],
                font=("Centaur", 24, "bold"),
                background="grey",
                foreground="brown",
                justify="center",
                wraplength=700,
            )

            Qprompt.pack(pady=(40, 20))
            Option_A = Radiobutton(
                root,
                text=Questions[indexes[0]][1],
                font=("Centaur", 24, "bold"),
                value=0,
                variable=radio,
                command=selected,
            )
            Option_A.pack(pady=(10, 0))
            Option_B = Radiobutton(
                root,
                text=Questions[indexes[0]][2],
                font=("Centaur", 24, "bold"),
                value=1,
                variable=radio,
                command=selected,
            )
            Option_B.pack(pady=(10, 0))
            Option_C = Radiobutton(
                root,
                text=Questions[indexes[0]][3],
                font=("Centaur", 24, "bold"),
                value=2,
                variable=radio,
                command=selected,
            )
            Option_C.pack(pady=(10, 0))
            Option_D = Radiobutton(
                root,
                text=Questions[indexes[0]][4],
                font=("Centaur", 24, "bold"),
                value=3,
                variable=radio,
                command=selected,
            )
            Option_D.pack(pady=(10, 0))

        Science = Button(
            root,
            text="SCIENCE",
            font=("Centaur", 30, "bold"),
            background="black",
            foreground="yellow",
            justify="center",

        )
        Science.pack(pady=(10, 0))
        mix = Button(
            root,
            text="MIX",
            font=("Centaur", 30, "bold"),
            background="black",
            foreground="yellow",
            justify="center",

        )
        mix.pack(pady=(10, 0))

    player = Button(
        root,
        text="player",
        font=("Centaur", 30, "bold"),
        background="black",
        foreground="yellow",
        justify="center",
        command=player_menu,

    )
    player.pack(pady=(10, 0))

    shut_down = Button(
        root,
        text="quit",
        font=("Centaur", 30, "bold"),
        background="black",
        foreground="yellow",
        justify="center",
        command=quit,
    )
    shut_down.pack(pady=(10, 0))


def play_press():
    Logo.destroy()
    Catchphrase.destroy()
    FrontImage.destroy()
    start_button.destroy()
    start_quiz()


Logo = Label(
    root,
    text="Quiz Mania",
    font=("Centaur", 40, "bold"),
    background="grey",
    foreground="brown",
)
Logo.pack()

Catchphrase = Label(
    root,
    text="Test Your Brain",
    font=("Centaur", 30, "bold"),
    background="grey",
    foreground="brown",
)
Catchphrase.pack(pady=(30, 0))
front_image = PhotoImage(file="Gui Images/Quizlaptop.png")
FrontImage = Label(
    root,
    image=front_image,

)
FrontImage.pack(pady=(30, 0))
start_image = PhotoImage(file="Gui Images/start.png")
start_button = Button(
    root,
    image=start_image,
    background='black',
    command=play_press,
)

start_button.pack(pady=(50, 0))
root.mainloop()
