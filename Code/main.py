from tkinter import *
from tkinter import messagebox
import re

class app:
	"""This class powers the calculator"""
	def __init__(self, master):
		self.master=master
		master.config(bg="#a6a6a6")
		master.geometry('400x464+200+100')
		master.maxsize(400, 464)
		master.minsize(400, 464)
		master.title("Calculator")
		master.iconbitmap("icon.ico")
		master.protocol("WM_DELETE_WINDOW", self.exit)
		self.status = "entering"
		self.current_value = "0"
		self.first_num = "0"
		self.calculation = '0'
		self.second_num = "0"

	def exit(self):
		ask = messagebox.askyesno("Exit", "Are you sure that you want to exit?")
		if ask == 1:
			self.master.destroy()

	def answer(self, a, b, c):
		try:
			try:
				a = int(a)
				b = int(b)
			except:
				a = float(a)
				b = float(b)
			if c == "+":
				answer = "{0:.2f}".format(a+b)
				answer = str(answer)
				if answer[-2:] == "00":
					return answer[:-3]
				return answer
			elif c == "-":
				answer = "{0:.2f}".format(a-b)
				answer = str(answer)
				if answer[-2:] == "00":
					return answer[:-3]
				return answer
			elif c == "*":
				answer = "{0:.2f}".format(a*b)
				answer = str(answer)
				if answer[-2:] == "00":
					return answer[:-3]
				return answer
			elif c == "/":
				answer = "{0:.2f}".format(a/b)
				answer = str(answer)
				if answer[-2:] == "00":
					return answer[:-3]
				return answer
			else:
				return 0
		except:
			reply = messagebox.showinfo("Invalid Statement", "That is a invalid statement.")
			self.current_value="0"
			self.calculation = "0"
			self.first_num = "0"
			self.second_num="0"
			return 0
	def control_input(self, enter):
		if enter=="clear":
			self.current_value="0"
			self.calculation = "0"
			self.first_num = "0"
			self.second_num="0"
		elif enter=="=":
			self.status = "calculated"
			self.second_num = re.sub(self.first_num + "[+|/|*]", "", self.current_value)
			self.second_num = re.sub(self.first_num + "-", "", self.second_num)
			self.current_value = str(self.answer(self.first_num, self.second_num, self.calculation))
			self.calculation = "0"
			self.first_num = "0"
			self.second_num="0"
		elif self.current_value!="0":
			if enter.isdigit()==True:
				self.current_value += enter
			elif self.calculation == "0":
				self.first_num = self.current_value
				self.current_value += enter
				self.status = "calculating"
				self.calculation = enter
		elif enter.isdigit()==True:
			self.current_value=enter
		self.entry_value.set(self.current_value)

	def setting_up(self):
		self.entry_value = StringVar()
		self.entry_value.set(self.current_value)
		self.entry_frame = Frame(self.master, relief="sunken", borderwidth=2, width=400, height=100)
		self.entry_box = Entry(self.entry_frame, justify="right", textvariable=self.entry_value, font=("Helvetica", "50"), state="readonly")
		self.btn_frame = Frame(self.master, width=400, height=380)
		self.btn_1 = Button(self.btn_frame, text="1", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("1"))
		self.btn_2 = Button(self.btn_frame, text="2", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("2"))
		self.btn_3 = Button(self.btn_frame, text="3", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("3"))
		self.btn_4 = Button(self.btn_frame, text="4", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("4"))
		self.btn_5 = Button(self.btn_frame, text="5", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("5"))
		self.btn_6 = Button(self.btn_frame, text="6", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("6"))
		self.btn_7 = Button(self.btn_frame, text="7", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("7"))
		self.btn_8 = Button(self.btn_frame, text="8", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("8"))
		self.btn_9 = Button(self.btn_frame, text="9", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("9"))
		self.btn_0 = Button(self.btn_frame, text="0", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("0"))
		self.btn_add = Button(self.btn_frame, text="+", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("+"))
		self.btn_sub = Button(self.btn_frame, text="-", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("-"))
		self.btn_mult = Button(self.btn_frame, text="*", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("*"))
		self.btn_div = Button(self.btn_frame, text="/", width=11, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("/"))
		self.btn_clear = Button(self.btn_frame, text="clear", width=23, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("clear"))
		self.btn_equal = Button(self.btn_frame, text="=", width=23, height=2, font=("Helvetica", "15"), command=lambda:self.control_input("="))
		self.btn_1.grid(row=0, column=0)
		self.btn_2.grid(row=0, column=1)
		self.btn_3.grid(row=0, column=2)
		self.btn_4.grid(row=1, column=0)
		self.btn_5.grid(row=1, column=1)
		self.btn_6.grid(row=1, column=2)
		self.btn_7.grid(row=2, column=0)
		self.btn_8.grid(row=2, column=1)
		self.btn_9.grid(row=2, column=2)
		self.btn_0.grid(row=3, column=1)
		self.btn_add.grid(row=3, column=0)
		self.btn_sub.grid(row=3, column=2)
		self.btn_mult.grid(row=4, column=2)
		self.btn_div.grid(row=5, column=2)
		self.btn_clear.grid(row=4, column=0, columnspan=2)
		self.btn_equal.grid(row=5, column=0, columnspan=2)
		self.entry_frame.pack()
		self.btn_frame.pack()
		self.entry_box.pack()

	def run(self):
		self.setting_up()
		self.master.mainloop()


win = Tk()
calculator= app(win)
calculator.run()