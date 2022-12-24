import tkinter as tk
from tkinter import ttk
import json

from calculatorBrain import calculate
from JSONDATA import workers_string

class MyClaculatorGUI: 


    def __init__(self):
        self.loadData()
        self.createInterface()


    def createInterface(self):
        self.root = tk.Tk()
        self.root.geometry("1000x500")
        self.root.title('Leti Faculty TimeSheet')
        self.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.terms = ["15th", "25th"]

        self.titleLabel = tk.Label(self.root, text="Leti Faculty TimeSheet", font=('Arial', 18))
        self.titleLabel.pack(padx=20, pady=20)

        self.horizontalFrame = tk.Frame(self.root)
        self.horizontalFrame.columnconfigure(0, weight=1)
        self.horizontalFrame.columnconfigure(1, weight=1)
        self.horizontalFrame.columnconfigure(2, weight=1)
        self.horizontalFrame.columnconfigure(3, weight=1)
        self.horizontalFrame.columnconfigure(4, weight=1)
        self.horizontalFrame.columnconfigure(5, weight=1)

        self.monthLabel = tk.Label(self.horizontalFrame, text="SelectMonth", font=('Arial', 12))
        self.monthLabel.grid(row=0, column=0)
        self.monthBox = ttk.Combobox(self.horizontalFrame, values=self.months, state="readonly")
        self.monthBox.current(0)
        self.monthBox.grid(row=0, column=1)

        self.yearLabel = tk.Label(self.horizontalFrame, text="SelectYear", font=('Arial', 12))
        self.yearLabel.grid(row=0, column=2)
        self.yearBox = tk.Spinbox(self.horizontalFrame, from_=2000, to=2022, wrap=True, state="readonly")
        self.yearBox.grid(row=0, column=3)

        self.termLabel = tk.Label(self.horizontalFrame, text="SelectTerm", font=('Arial', 12))
        self.termLabel.grid(row=0, column=4)
        self.termBox = ttk.Combobox(self.horizontalFrame, values=self.terms, state="readonly")
        self.termBox.current(0)
        self.termBox.grid(row=0, column=5)
        self.horizontalFrame.pack(fill='x')


        self.resultText = tk.Text(self.root, bd=0, bg="#FFFFFF", fg="black", highlightthickness=0, state="disabled", height=20)
        self.resultText.pack(padx=20, pady=20)

        self.button = tk.Button(
            borderwidth=0,
            font=("Arial", 18 * -1, 'bold'),
            text="Calculate",
            highlightthickness=0,
            command=self.calculate,
            state = "normal",
            relief="flat",    
      )
        self.button.pack(padx=20, pady=20)


        self.root.mainloop()

    def calculate(self):
      month = int(self.months.index(self.monthBox.get())) + 1
      year = int(self.yearBox.get())
      half = int(self.terms.index(self.termBox.get())) + 1
      
      print(f"Month: {month}\tYear: {year}\tHalf: {half}")
      
      result = ""
      
      for department in self.departments:
        print(department['name'])
        result += f"{department['name']}\n"
        
        for worker in department['workers']:
          name, time = worker.values()
          hours = calculate(time, month, year, half, part_time=self.part_time)
          
          print(f"{name}:\t{round(hours, 1)} hours")
          result += f"{name}:\t{round(hours, 1)} hours\n"
          
        print()
        result += "\n"
      
      self.resultText.config(state="normal")
      self.resultText.delete("1.0", tk.END)
      self.resultText.insert(tk.END, result.strip())
      self.resultText.config(state="disabled")
    

    def loadData(self): 
      data = json.loads(workers_string)
        
      self.part_time = data['part_time']
      self.departments = data['departments']



MyClaculatorGUI()