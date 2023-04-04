from tkinter import *

class LoginFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.create_widgets()
        self.read_file()

    def create_widgets(self):
        # Labels for security questions
        self.label_question1 = Label(self, text="What was the make of your first car?")
        self.label_question2 = Label(self, text="What high school did you attend?")

        # Entry fields for user's responses
        self.entry_response1 = Entry(self)
        self.entry_response2 = Entry(self)

        # Submit button
        self.submit_button = Button(self, text="Submit", command=self.check_auth)

        # Result label
        self.result_label = Label(self, text="")
        
        # Grid layout
        self.label_question1.grid(row=0, column=0, sticky=W)
        self.entry_response1.grid(row=0, column=1)
        self.label_question2.grid(row=1, column=0, sticky=W)
        self.entry_response2.grid(row=1, column=1)
        self.submit_button.grid(row=2, column=0, columnspan=2)
        self.result_label.grid(row=3, column=0, columnspan=2)

    def read_file(self):
        # Read in security questions and answers from file
        self.question_dict = {}
        with open("authenticate.txt") as fin:
            for line in fin:
                question, response = line.strip().split("?")
                self.question_dict[question] = response

    def check_auth(self):
        # Get user's responses
        response1 = self.entry_response1.get()
        response2 = self.entry_response2.get()

        # Check if responses match stored answers
        if response1 == self.question_dict["What was the make of your first car"] and response2 == self.question_dict["What high school did you attend"]:
            self.result_label.config(text="Authentication successful!")
        else:
            self.result_label.config(text="Authentication failed.")

# Initialize Tkinter window
root = Tk()
root.title("Login System")

# Create LoginFrame and add to window
app = LoginFrame(root)
app.grid()

# Start main event loop
root.mainloop()
