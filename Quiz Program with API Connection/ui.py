from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score:", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=f"QUESTION",
            font=("arial", 20, "italic"),
            fill="black"
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=(20,20), pady=(20,20))

        #self. is used when we want the attribute to be available for the class. no self. if
        #we are only using the variable in creating an attribute
        true_button_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2, padx=(20, 20), pady=(20,20))
        false_button_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2, padx=(20, 20), pady=(20,20))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            #.itemconfig if its a canavs item. .config if the change is directly on the canvas
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)



