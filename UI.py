__author__ = 'Admin'
from tkinter import *


class MenuProcess():
    def __init__(self, workspace):
        self.menu_base = Menu(workspace, tearoff=0)
        workspace.config(menu=self.menu_base)

    def menu_col(self, title, inc_dict):
        self.menu_col_1 = Menu(self.menu_base, tearoff=0)
        self.menu_base.add_cascade(label=title, menu=self.menu_col_1)
        for i, j in inc_dict.items():
            if i == "Exit":
                self.menu_col_1.add_separator()
            self.menu_col_1.add_command(label=i, command=j)
        return self.menu_col_1

    def menu_ins(self, menu_from, index, title, inc_dict):
        self.menu_internal = Menu(menu_from, tearoff=0)
        menu_from.insert_cascade(index, label=title, menu=self.menu_internal)
        for i, j in inc_dict.items():
            self.menu_internal.add_command(label=i, command=j)


class New_win():
    def __init__(self, workspace):
        self.workspace = workspace

    def main_rect(self):
        self.new_win = Toplevel(self.workspace)
        self.new_win.title('Create')
        names = ['Name:', 'X:', 'Y:', 'Width:', 'Height:']
        numb_row = 0
        for i in names:
            self.name = LabelProcess(self.new_win, i, 'Tahoma 10', numb_row, 0, W).table()
            numb_row += 1
        for j in range(len(names)):
            self.entry = EntryProcess(self.new_win, 1, j, N)

    def main_oval(self):
        self.new_win = Toplevel(self.workspace)
        self.new_win.title('Create')
        names = ['Name:', 'X:', 'Y:', '[x] Is circle:', 'Radius X:']
        numb_row = 0
        self.var = IntVar()
        for i in names:
            self.name = LabelProcess(self.new_win, i, 'Tahoma 10', numb_row, 0, W).table()
            numb_row += 1
        self.radius_y = Label(self.new_win, text='Radius Y:', font='Tahoma 10')
        self.radius_y.grid(column=0, row=5, sticky=W)
        for j in range(len(names)):
            if j == 3:
                self.checkbutton = CheckButtonProcess(self.new_win, 1, 3, self.checkbutton_var, self.var, NW)
            else:
                self.entry = EntryProcess(self.new_win, 1, j, N)
        self.radius_y_entry = Entry(self.new_win, bd=5)
        self.radius_y_entry.grid(column = 1, row =5)

    def checkbutton_var(self):
        """ TO DO, think how to create method forget in class LabelProcess & EntryProcess"""
        if self.var.get():
            self.radius_y.grid_remove()
            self.radius_y_entry.grid_remove()
            self.name1 = LabelProcess(self.new_win, 'Radius:  ', 'Tahoma 10', 4, 0, W).table()
        else:
            self.radius_y.grid()
            self.radius_y_entry.grid()
            self.name1 = LabelProcess(self.new_win, 'Radius X:', 'Tahoma 10', 4, 0, W).table()


class Actions():
    def __init__(self, workspace, action):
        self.workspace = workspace
        self.action = action

    def crt_geom(self):
        """Temp func"""

    pass

    def destroyer(self):
        self.workspace.destroy()


class ButtonProcess():
    def __init__(self, workspace, text_var, new_text, row, col):
        self.workspace = workspace
        self.new_text = new_text
        self.but = Button(workspace, text=text_var, command=self.func_any)
        self.but.grid(row=row, column=col)

    def func_any(self):
        self.new_but = Button(self.workspace, text=self.new_text, command=self.func_any)
        self.new_but.grid()


class LabelProcess():
    def __init__(self, workspace, text_var, font_var, row, col, stick):
        self.row = row
        self.col = col
        self.stick = stick
        self.label = Label(workspace, text=text_var, font=font_var)

    def table(self):
        self.label.grid(column=self.col, row=self.row, sticky=self.stick)

    def forget_it(self):
        self.label.grid_remove()

        # def position(self):
        #     self.label.place(x=self.col, y=self.row, relx=0.05, rely=0.05)


class ListProcess():
    def __init__(self, workspace, row, col, name):
        if len(name) == 0:
            self.maximum = 2
        else:
            self.maximum = len(max(name, key=len))
        self.listbox = Listbox(workspace, height=len(name), width=self.maximum)
        for i in name:
            self.listbox.insert(END, i)
        self.listbox.grid(column=col, row=row)


class EntryProcess():
    def __init__(self, workspace, col, row, stick):
        self.txt = Entry(workspace, bd=5)
        self.txt.grid(column=col, row=row, sticky=stick)


class CheckButtonProcess():
    def __init__(self, workspace, col, row, command, var, stick):
        self.checkbutton = Checkbutton(workspace, variable=var, command=command)
        self.checkbutton.grid(column=col, row=row, sticky=stick)


def main():
    root = Tk()
    root.title('Geometric editor')
    base_menu = MenuProcess(root)
    act = Actions(root, "<Button-1>")       #WAGRAAAHHH
    new_wind = New_win(root)        #WAGRAAAHHH
    under_menu = base_menu.menu_col('File', {'Exit': act.destroyer})
    base_menu.menu_ins(under_menu, 0, 'Model',
                       {'Create rectangle': new_wind.main_rect,
                        'Create Oval': new_wind.main_oval,
                        'Remove': act.crt_geom})

    column_name = LabelProcess(root, 'Name', 'Tahoma 10', 0, 0, N).table()
    column_type = LabelProcess(root, 'Type', 'Tahoma 10', 0, 1, N).table()
    column_x = LabelProcess(root, 'X', 'Tahoma 10', 0, 2, N).table()
    column_y = LabelProcess(root, 'Y', 'Tahoma 10', 0, 3, N).table()
    def_name = ListProcess(root, 1, 0, ['Figure 1', 'Figure 2', 'Figure 23421', 'Figure 1'])
    def_name = ListProcess(root, 1, 1, ['    ', '', '', ''])
    def_name = ListProcess(root, 1, 2, ['    ', '', '', ''])
    def_name = ListProcess(root, 1, 3, ['    ', '', '', ''])



    #button_1 = ButtonProcess(root, 'Button name_1', "Button-1", 2, 0)
    root.mainloop()


if __name__ == "__main__":
    main()