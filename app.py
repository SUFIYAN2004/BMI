from tkinter import *

def check():
    try:
        # Retrieve values from the entries and convert them to floats
        height_value = float(height.get())
        weight_value = float(weight.get())
        
        # Calculate BMI
        bmi = weight_value / (height_value ** 2)
        
        # Determine the BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 >= bmi < 24.9:
            category = "Normal weight"
        elif 25 >= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        # Display the BMI and category
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
    
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

window = Tk()
window.geometry("500x600+300+10")
window.config(bg="black")
window.title("BMI Calculator")
window.resizable(False, False)

Label(text="BMI Calculator", font=("times new roman", 30, "bold"), bg="black", fg="pink").pack(pady=20)

label_height = Label(window, text="Height (m): ", font=("times new roman", 20, "bold"), bg="black", fg="white")
label_height.place(x=20, y=100)

height = Entry(window, font=("times new roman", 20, "bold"))
height.place(x=170, y=100)

label_weight = Label(window, text="Weight (kg): ", font=("times new roman", 20, "bold"), bg="black", fg="white")
label_weight.place(x=20, y=200)

weight = Entry(window, font=("times new roman", 20, "bold"))
weight.place(x=170, y=200)

submit = Button(window, text="Check", font=("times new roman", 20, "bold"), bg="black", fg="orange", activebackground="orange", activeforeground="black", command=check)
submit.place(x=200, y=300)

result_label = Label(window, text="", font=("times new roman", 20, "bold"), bg="black", fg="white")
result_label.place(x=50, y=400)

window.mainloop()
