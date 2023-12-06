from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text=f"Score: {0}", fg="white", font=('Arial', 20, 'bold'), bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=400, height=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.question_text = self.canvas.create_text(
            200, 150, width=380, text="", font=('Arial', 20, 'italic'))

        true_btn_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(
            image=true_btn_img, highlightthickness=0, command=self.check_answer_true)
        self.true_btn.grid(row=2, column=0)

        false_btn_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(
            image=false_btn_img, highlightthickness=0, command=self.check_answer_false)
        self.false_btn.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill="black")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(
                self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(
                self.question_text, text="You're reached the end of the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)
