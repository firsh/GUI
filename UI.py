__author__ = 'Admin'
from tkinter import *
import tkinter.messagebox


class MainWin():
    def __init__(self, workspace):
        self.workspace = workspace
        self.menu_base = Menu(workspace, tearoff=0)
        workspace.config(menu=self.menu_base)
        self.content()

    def menu_col(self, title, **kwargs):
        self.menu_col_1 = Menu(self.menu_base, tearoff=0)
        self.menu_base.add_cascade(label=title, menu=self.menu_col_1)
        for i, j in kwargs.items():
            if i == "Exit":
                self.menu_col_1.add_separator()
            self.menu_col_1.add_command(label=i, command=j)
        return self.menu_col_1

    def menu_ins(self, menu_from, index, title, inc_dict):
        self.menu_internal = Menu(menu_from, tearoff=0)
        menu_from.insert_cascade(index, label=title, menu=self.menu_internal)
        for i, j in inc_dict.items():
            self.menu_internal.add_command(label=i, command=j)

    def content(self):
        counter, self.columns_lst, column_titles = 0, [], ['Name', 'Type', 'X', 'Y']
        for column_title in column_titles:
            column = Listbox(self.workspace, selectmode='extended')
            column.grid(row=1, column=counter)
            self.columns_lst.append(column)
            Label(self.workspace, text=column_title, font='Tahoma 10').grid(column=counter, row=0, stick=N)
            counter += 1

    def lstbox(self):
        return self.columns_lst

    def remover(self):
        self.selected_strings = self.columns_lst[0].curselection()
        for selected_string in range(len(self.columns_lst[0].curselection())):
            for listbox_numb in range(4):
                self.columns_lst[listbox_numb].delete(self.selected_strings[-1 - selected_string])


class NewWin():
    def __init__(self, workspace):
        self.workspace = workspace

    def new_win_body(self):
        self.new_win = Toplevel(self.workspace)
        self.new_win.title('Create')
        self.row_counter, self.lst_entrys = 0, []
        Label(self.new_win, text=' ', font='Tahoma 10').grid(column=0, row=6, stick=NW)
        Button(self.new_win, text='Save', command=self.button_save_whatdo).grid(column=1, row=100, stick=N)
        Button(self.new_win, text='Cancel', command=self.new_win.destroy).grid(column=1, row=100, stick=E)

    def new_win_rect(self):
        self.new_win_body()
        labels = ['Name:', 'X:', 'Y:', 'Width:', 'Height:  ']

        for i in labels:
            Label(self.new_win, text=i, font='Tahoma 10').grid(column=0, row=self.row_counter, stick=W)
            entry = Entry(self.new_win)
            entry.grid(column=1, row=self.row_counter, sticky=N)
            if i != 'Width:' or i != 'Height:  ':
                self.lst_entrys.append(entry)
            self.row_counter += 1
        self.lst_entrys.insert(1, 'Rectangle')


    def new_win_oval(self):
        self.new_win_body()
        labels, self.checkbutton_var = ['Name:', 'X:', 'Y:', '[x] Is circle:', 'Radius X:', 'Radius Y:'], IntVar()
        for title in labels:
            self.label = Label(self.new_win, text=title, font='Tahoma 10')
            self.label.grid(column=0, row=self.row_counter, sticky=W)
            if title == '[x] Is circle:':
                Checkbutton(self.new_win, command=self.checkbutton_whatdo, var=self.checkbutton_var).grid(column=1,
                                                                                                          row=self.row_counter,
                                                                                                          stick=NW)
            else:
                self.entry = Entry(self.new_win)
                self.entry.grid(column=1, row=self.row_counter, sticky=N)
                self.lst_entrys.append(self.entry)
            self.row_counter += 1
        self.lst_entrys.insert(1, 'Oval')

    def checkbutton_whatdo(self):
        if self.checkbutton_var.get():
            self.entry.grid_remove()
            self.label.grid_remove()
            self.last_title = Label(self.new_win, text='Radius:  ', font='Tahoma 10').grid(column=0, row=4, sticky=W)
            del self.lst_entrys[-1]
        else:
            self.entry.grid()
            self.label.grid()
            self.last_title = Label(self.new_win, text='Radius X:', font='Tahoma 10').grid(column=0, row=4, sticky=W)
            self.lst_entrys.append(self.entry)

    def button_save_whatdo(self):
        values_entry = []
        for val_entry in self.lst_entrys:
            if isinstance(val_entry, str):
                values_entry.append(val_entry)
            else:
                values_entry.append(val_entry.get())

        for numb_entry in range(len(values_entry)):
            if numb_entry > 1:
                try:
                    int(values_entry[numb_entry])
                    if numb_entry > 3:
                        if values_entry[numb_entry].isdigit():
                            pass
                        else:
                            tkinter.messagebox.showerror('Input error', 'Check that last entered values is positive')
                            break
                except ValueError:
                    tkinter.messagebox.showerror('Input error', 'Check entered values')
                    break
        else:
            self.main_columns = base_win.lstbox()
            for column in range(len(self.main_columns)):
                self.main_columns[column].insert(END, values_entry[column])
            self.new_win.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title('Geometric editor')
    base_win = MainWin(root)
    new_wind = NewWin(root)        #WAGRAAAHHH
    under_menu = base_win.menu_col('File', Exit=root.destroy)
    base_win.menu_ins(under_menu, 0, 'Model',
                      {'Create rectangle': new_wind.new_win_rect,
                       'Create oval': new_wind.new_win_oval,
                       'Remove': base_win.remover})
    root.mainloop()
