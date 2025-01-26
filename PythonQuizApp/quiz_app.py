import tkinter as tk
from tkinter import messagebox

# Question data
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 1  # Position in the options array (1-indexed)
    },
    {
        "topic": "Lists",
        "question": "What is the output of this code?",
        "code": "my_list = [1, 2, 3]\nprint(my_list[1])",
        "options": ["1", "2", "3", "IndexError"],
        "answer": 2
    },
    # Add more questions as needed
]


# Generate Question Function
def generate_question():
    topic = topic_input.get().strip().capitalize()
    filtered_questions = [q for q in questions if q["topic"].lower() == topic.lower()]
    
    if not filtered_questions:
        feedback_label.config(text="No questions found for the selected topic.")
        return
    
    question = filtered_questions[0]
    display_question(question)

# Display Question
def display_question(question):
    global current_question
    current_question = question
    topic_label.config(text=f"Topic: {question['topic']}")
    question_label.config(text=question["question"])
    code_text.config(state="normal")
    code_text.delete(1.0, tk.END)
    code_text.insert(tk.END, question.get("code", ""))
    code_text.config(state="disabled")

    # Display options
    for widget in options_frame.winfo_children():
        widget.destroy()

    for idx, option in enumerate(question["options"], 1):
        rb = tk.Radiobutton(
            options_frame, text=option, variable=selected_option, value=idx, wraplength=300
        )
        rb.pack(anchor="w")

# Submit Answer
def submit_answer():
    if not current_question:
        feedback_label.config(text="Please generate a question first!")
        return

    selected = selected_option.get()
    if selected == current_question["answer"]:
        feedback_label.config(text="Correct! Well done!")
    else:
        feedback_label.config(text=f"Incorrect. The correct answer is {current_question['options'][current_question['answer'] - 1]}.")

# Tkinter Setup
root = tk.Tk()
root.title("Python Quiz App")
root.geometry("500x500")

current_question = None
selected_option = tk.IntVar(value=0)

# Input and Buttons
topic_input = tk.Entry(root)
topic_input.pack(pady=10)

generate_btn = tk.Button(root, text="Generate Python Question", command=generate_question)
generate_btn.pack(pady=10)

# Question Display
topic_label = tk.Label(root, text="Topic: ", font=("Helvetica", 12, "bold"))
topic_label.pack(pady=5)

question_label = tk.Label(root, text="", wraplength=400)
question_label.pack(pady=5)

code_text = tk.Text(root, height=5, width=50, state="disabled", wrap="none")
code_text.pack(pady=5)

options_frame = tk.Frame(root)
options_frame.pack(pady=5)

# Submit Button and Feedback
submit_btn = tk.Button(root, text="Submit", command=submit_answer)
submit_btn.pack(pady=10)

feedback_label = tk.Label(root, text="", font=("Helvetica", 10))
feedback_label.pack(pady=5)

# Run the app
root.mainloop()
