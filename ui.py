from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        # Score Label
        self.score_label = Label(text=f"Score: {quiz.score}", fg="#fff", bg=THEME_COLOR, font=(FONT_NAME, 15, "bold"))
        self.score_label.grid(row=0, column=1)
        # Question label
        self.question_label = Label(
            bg="#fff",
            fg=THEME_COLOR,
            width=25,
            height=10,
            font=(FONT_NAME, 17, "italic"),
            wraplength=300)
        self.question_label.grid(row=1, column=0, columnspan=2, pady=20)
        # Answer buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,
                                  highlightthickness=0,
                                  border=0,
                                  command=lambda: self.check_answer("true")
                                  )
        self.true_button.grid(column=0, row=2, pady=10)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,
                                   highlightthickness=0,
                                   border=0,
                                   command=lambda: self.check_answer("false"))
        self.false_button.grid(column=1, row=2, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.question_label.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.question_label.config(text=question)
        else:
            self.question_label.config(text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer(self, answer: str):
        self.give_feedback(self.quiz.check_answer(user_answer=answer))

        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(500, func=self.get_next_question)

    def change_background(self):
        self.question_label.config(bg="white")

    def give_feedback(self, is_right: bool):
        if is_right:
            self.question_label.config(bg="green")
        else:
            self.question_label.config(bg="red")
