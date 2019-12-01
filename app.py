'''
Copyright 2019 
© Ramon Romero   @RamonRomeroQro

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from tkinter import *
from usc import UniformCostSearch
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename

def show_answer():
    search = UniformCostSearch(str(start_input.get()), str(goal_input.get()))
    path = str(blank.get())
    search.parse_file(path)
    p, len_p= search.solve()
    s="->".join(p)
    calc.insert(0, "time: "+str(len_p)+"; "+s)

def askopenfile():
    global filename
    filename = askopenfilename()
    blank.insert(0, filename)


filename = ""
main = Tk()
Label(main, text = " Start 1:").grid(row=0)
Label(main, text = " Goal 2:").grid(row=1)
Label(main, text = "File:").grid(row=2)
Button(main, text='Browse', command=askopenfile).grid(row=3)
Label(main, text = "Calc:").grid(row=4)


start_input = Entry(main)
goal_input = Entry(main)
blank = Entry(main)
calc = Entry(main)


start_input.grid(row=0, column=1)
goal_input.grid(row=1, column=1)
blank.grid(row=2, column=1)
calc.grid(row=4, column=1)


Button(main, text='Quit', command=main.destroy).grid(row=5, column=0, sticky=W, pady=4)
Button(main, text='Show', command=show_answer).grid(row=5, column=1, sticky=W, pady=4)

mainloop()