#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
import pozycja_startowa
from time import sleep


class Main_Window(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title(f'SUDOKU MASTER')

        self.container = tk.Canvas()
        self.container.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.geometry('1000x800')

        # główna ramka programu
        self.main_frame = Main_frame(self.container, self)
        self.main_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

        # ramka menu programu
        self.menu_frame = Menu_frame(self.container, self)
        self.menu_frame.place(relx=0, rely=0, relwidth=0.2, relheight=1)

class Main_frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#140c0c')
        self.entries_matrix = []
        self.create_square_frames()
        self.create_minisquare_entries()
        self.solution_matrix = self.create_empty_dict('')
        self.wypelnij_poczatek() #przykładowe sudoku wzięte z książki

    def solve_sudoku(self):

        try_count = 0
        puste_pola = 91
        while True:
            self.possibilities_matrix = self.create_empty_dict('')
            self.zgromadz_dane()
            print(f'PUSTE POLA: {self.policz_puste_pola()}')
            if self.policz_puste_pola() < puste_pola:
                puste_pola = self.policz_puste_pola()
                try_count = 0
            else:
                try_count += 1
            self.sprawdz_puste_pola()

            self.wypelnij_pola_pewne()
            self.possibilities_matrix = self.create_empty_dict('')


            if self.policz_puste_pola() == 0:
                print('ROZWIĄZANE :)')
                break
            elif try_count == 10:
                print('NIE UDAŁO SIĘ :(')
                break

    def create_square_frames(self):
        self.square_frame_0x0 = tk.Frame(self)
        self.square_frame_0x0.configure(bg='#140c0c')
        self.square_frame_0x0.place(relx=0.01, rely=0.01, relwidth=0.96/3, relheight=0.96/3)
        self.square_frame_0x1 = tk.Frame(self)
        self.square_frame_0x1.configure(bg='#140c0c')
        self.square_frame_0x1.place(relx=0.02 + 0.96 / 3, rely=0.01, relwidth=0.96 / 3, relheight=0.96 / 3)
        self.square_frame_0x2 = tk.Frame(self)
        self.square_frame_0x2.configure(bg='#140c0c')
        self.square_frame_0x2.place(relx=0.03 + (0.96 / 3)*2, rely=0.01, relwidth=0.96 / 3, relheight=0.96 / 3)
        self.square_frame_1x0 = tk.Frame(self)
        self.square_frame_1x0.configure(bg='#140c0c')
        self.square_frame_1x0.place(relx=0.01, rely=0.02 + 0.96 / 3, relwidth=0.96 / 3, relheight=0.96 / 3)
        self.square_frame_1x1 = tk.Frame(self)
        self.square_frame_1x1.configure(bg='#140c0c')
        self.square_frame_1x1.place(relx=0.02 + 0.96 / 3, rely=0.02 + 0.96 / 3, relwidth=0.96 / 3, relheight=0.96 / 3)
        self.square_frame_1x2 = tk.Frame(self)
        self.square_frame_1x2.configure(bg='#140c0c')
        self.square_frame_1x2.place(relx=0.03 + (0.96 / 3) * 2, rely=0.02 + 0.96 / 3, relwidth=0.96 / 3, relheight=0.96 / 3)
        self.square_frame_2x0 = tk.Frame(self)
        self.square_frame_2x0.configure(bg='#140c0c')
        self.square_frame_2x0.place(relx=0.01, rely=0.03 + (0.96 / 3)*2, relwidth=0.96 / 3, relheight=0.96 / 3)
        self.square_frame_2x1 = tk.Frame(self)
        self.square_frame_2x1.configure(bg='#140c0c')
        self.square_frame_2x1.place(relx=0.02 + 0.96 / 3, rely=0.03 + (0.96 / 3)*2, relwidth=0.96 / 3, relheight=0.96 / 3)
        self.square_frame_2x2 = tk.Frame(self)
        self.square_frame_2x2.configure(bg='#140c0c')
        self.square_frame_2x2.place(relx=0.03 + (0.96 / 3) * 2, rely=0.03 + (0.96 / 3)*2, relwidth=0.96 / 3,
                                    relheight=0.96 / 3)

    def create_minisquare_entries(self):
        #kwadrat 0x0
        self.ms_0x0_0x0 = tk.Entry(self.square_frame_0x0, justify='center',bg='#6b685f', fg='white')
        self.ms_0x0_0x0.place(relx=0, rely=0, relwidth=0.98/3, relheight=0.98/3)
        self.ms_0x0_0x1 = tk.Entry(self.square_frame_0x0, justify='center', bg='#6b685f', fg='white')
        self.ms_0x0_0x1.place(relx=0.01 + 0.98 / 3, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x0_0x2 = tk.Entry(self.square_frame_0x0, justify='center', bg='#6b685f', fg='white')
        self.ms_0x0_0x2.place(relx=0.02 + (0.98 / 3)*2, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x0_1x0 = tk.Entry(self.square_frame_0x0, justify='center', bg='#6b685f', fg='white')
        self.ms_0x0_1x0.place(relx=0, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x0_1x1 = tk.Entry(self.square_frame_0x0, justify='center', bg='#6b685f', fg='white')
        self.ms_0x0_1x1.place(relx=0.01 + 0.98 / 3, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x0_1x2 = tk.Entry(self.square_frame_0x0, justify='center', bg='#6b685f', fg='white')
        self.ms_0x0_1x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x0_2x0 = tk.Entry(self.square_frame_0x0, justify='center', bg='#6b685f', fg='white')
        self.ms_0x0_2x0.place(relx=0, rely=0.02 + (0.98 / 3)*2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x0_2x1 = tk.Entry(self.square_frame_0x0, justify='center', bg='#6b685f', fg='white')
        self.ms_0x0_2x1.place(relx=0.01 + 0.98 / 3, rely=0.02 + (0.98 / 3)*2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x0_2x2 = tk.Entry(self.square_frame_0x0, justify='center', bg='#6b685f', fg='white')
        self.ms_0x0_2x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.02 + (0.98 / 3)*2, relwidth=0.98 / 3, relheight=0.98 / 3)

        # kwadrat 0x1
        self.ms_0x1_0x0 = tk.Entry(self.square_frame_0x1, justify='center', bg='#6b685f', fg='white')
        self.ms_0x1_0x0.place(relx=0, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x1_0x1 = tk.Entry(self.square_frame_0x1, justify='center', bg='#6b685f', fg='white')
        self.ms_0x1_0x1.place(relx=0.01 + 0.98 / 3, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x1_0x2 = tk.Entry(self.square_frame_0x1, justify='center', bg='#6b685f', fg='white')
        self.ms_0x1_0x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x1_1x0 = tk.Entry(self.square_frame_0x1, justify='center', bg='#6b685f', fg='white')
        self.ms_0x1_1x0.place(relx=0, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x1_1x1 = tk.Entry(self.square_frame_0x1, justify='center', bg='#6b685f', fg='white')
        self.ms_0x1_1x1.place(relx=0.01 + 0.98 / 3, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x1_1x2 = tk.Entry(self.square_frame_0x1, justify='center', bg='#6b685f', fg='white')
        self.ms_0x1_1x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x1_2x0 = tk.Entry(self.square_frame_0x1, justify='center', bg='#6b685f', fg='white')
        self.ms_0x1_2x0.place(relx=0, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x1_2x1 = tk.Entry(self.square_frame_0x1, justify='center', bg='#6b685f', fg='white')
        self.ms_0x1_2x1.place(relx=0.01 + 0.98 / 3, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x1_2x2 = tk.Entry(self.square_frame_0x1, justify='center', bg='#6b685f', fg='white')
        self.ms_0x1_2x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3,
                              relheight=0.98 / 3)

        # kwadrat 0x2
        self.ms_0x2_0x0 = tk.Entry(self.square_frame_0x2, justify='center', bg='#6b685f', fg='white')
        self.ms_0x2_0x0.place(relx=0, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x2_0x1 = tk.Entry(self.square_frame_0x2, justify='center', bg='#6b685f', fg='white')
        self.ms_0x2_0x1.place(relx=0.01 + 0.98 / 3, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x2_0x2 = tk.Entry(self.square_frame_0x2, justify='center', bg='#6b685f', fg='white')
        self.ms_0x2_0x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x2_1x0 = tk.Entry(self.square_frame_0x2, justify='center', bg='#6b685f', fg='white')
        self.ms_0x2_1x0.place(relx=0, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x2_1x1 = tk.Entry(self.square_frame_0x2, justify='center', bg='#6b685f', fg='white')
        self.ms_0x2_1x1.place(relx=0.01 + 0.98 / 3, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x2_1x2 = tk.Entry(self.square_frame_0x2, justify='center', bg='#6b685f', fg='white')
        self.ms_0x2_1x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x2_2x0 = tk.Entry(self.square_frame_0x2, justify='center', bg='#6b685f', fg='white')
        self.ms_0x2_2x0.place(relx=0, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x2_2x1 = tk.Entry(self.square_frame_0x2, justify='center', bg='#6b685f', fg='white')
        self.ms_0x2_2x1.place(relx=0.01 + 0.98 / 3, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_0x2_2x2 = tk.Entry(self.square_frame_0x2, justify='center', bg='#6b685f', fg='white')
        self.ms_0x2_2x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3,
                              relheight=0.98 / 3)

        # kwadrat 1x0
        self.ms_1x0_0x0 = tk.Entry(self.square_frame_1x0, justify='center', bg='#6b685f', fg='white')
        self.ms_1x0_0x0.place(relx=0, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x0_0x1 = tk.Entry(self.square_frame_1x0, justify='center', bg='#6b685f', fg='white')
        self.ms_1x0_0x1.place(relx=0.01 + 0.98 / 3, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x0_0x2 = tk.Entry(self.square_frame_1x0, justify='center', bg='#6b685f', fg='white')
        self.ms_1x0_0x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x0_1x0 = tk.Entry(self.square_frame_1x0, justify='center', bg='#6b685f', fg='white')
        self.ms_1x0_1x0.place(relx=0, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x0_1x1 = tk.Entry(self.square_frame_1x0, justify='center', bg='#6b685f', fg='white')
        self.ms_1x0_1x1.place(relx=0.01 + 0.98 / 3, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x0_1x2 = tk.Entry(self.square_frame_1x0, justify='center', bg='#6b685f', fg='white')
        self.ms_1x0_1x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x0_2x0 = tk.Entry(self.square_frame_1x0, justify='center', bg='#6b685f', fg='white')
        self.ms_1x0_2x0.place(relx=0, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x0_2x1 = tk.Entry(self.square_frame_1x0, justify='center', bg='#6b685f', fg='white')
        self.ms_1x0_2x1.place(relx=0.01 + 0.98 / 3, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x0_2x2 = tk.Entry(self.square_frame_1x0, justify='center', bg='#6b685f', fg='white')
        self.ms_1x0_2x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3,
                              relheight=0.98 / 3)

        # kwadrat 1x1
        self.ms_1x1_0x0 = tk.Entry(self.square_frame_1x1, justify='center', bg='#6b685f', fg='white')
        self.ms_1x1_0x0.place(relx=0, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x1_0x1 = tk.Entry(self.square_frame_1x1, justify='center', bg='#6b685f', fg='white')
        self.ms_1x1_0x1.place(relx=0.01 + 0.98 / 3, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x1_0x2 = tk.Entry(self.square_frame_1x1, justify='center', bg='#6b685f', fg='white')
        self.ms_1x1_0x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x1_1x0 = tk.Entry(self.square_frame_1x1, justify='center', bg='#6b685f', fg='white')
        self.ms_1x1_1x0.place(relx=0, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x1_1x1 = tk.Entry(self.square_frame_1x1, justify='center', bg='#6b685f', fg='white')
        self.ms_1x1_1x1.place(relx=0.01 + 0.98 / 3, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x1_1x2 = tk.Entry(self.square_frame_1x1, justify='center', bg='#6b685f', fg='white')
        self.ms_1x1_1x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x1_2x0 = tk.Entry(self.square_frame_1x1, justify='center', bg='#6b685f', fg='white')
        self.ms_1x1_2x0.place(relx=0, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x1_2x1 = tk.Entry(self.square_frame_1x1, justify='center', bg='#6b685f', fg='white')
        self.ms_1x1_2x1.place(relx=0.01 + 0.98 / 3, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x1_2x2 = tk.Entry(self.square_frame_1x1, justify='center', bg='#6b685f', fg='white')
        self.ms_1x1_2x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3,
                              relheight=0.98 / 3)

        # kwadrat 1x2
        self.ms_1x2_0x0 = tk.Entry(self.square_frame_1x2, justify='center', bg='#6b685f', fg='white')
        self.ms_1x2_0x0.place(relx=0, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x2_0x1 = tk.Entry(self.square_frame_1x2, justify='center', bg='#6b685f', fg='white')
        self.ms_1x2_0x1.place(relx=0.01 + 0.98 / 3, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x2_0x2 = tk.Entry(self.square_frame_1x2, justify='center', bg='#6b685f', fg='white')
        self.ms_1x2_0x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x2_1x0 = tk.Entry(self.square_frame_1x2, justify='center', bg='#6b685f', fg='white')
        self.ms_1x2_1x0.place(relx=0, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x2_1x1 = tk.Entry(self.square_frame_1x2, justify='center', bg='#6b685f', fg='white')
        self.ms_1x2_1x1.place(relx=0.01 + 0.98 / 3, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x2_1x2 = tk.Entry(self.square_frame_1x2, justify='center', bg='#6b685f', fg='white')
        self.ms_1x2_1x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x2_2x0 = tk.Entry(self.square_frame_1x2, justify='center', bg='#6b685f', fg='white')
        self.ms_1x2_2x0.place(relx=0, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x2_2x1 = tk.Entry(self.square_frame_1x2, justify='center', bg='#6b685f', fg='white')
        self.ms_1x2_2x1.place(relx=0.01 + 0.98 / 3, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_1x2_2x2 = tk.Entry(self.square_frame_1x2, justify='center', bg='#6b685f', fg='white')
        self.ms_1x2_2x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3,
                              relheight=0.98 / 3)

        # kwadrat 2x0
        self.ms_2x0_0x0 = tk.Entry(self.square_frame_2x0, justify='center', bg='#6b685f', fg='white')
        self.ms_2x0_0x0.place(relx=0, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x0_0x1 = tk.Entry(self.square_frame_2x0, justify='center', bg='#6b685f', fg='white')
        self.ms_2x0_0x1.place(relx=0.01 + 0.98 / 3, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x0_0x2 = tk.Entry(self.square_frame_2x0, justify='center', bg='#6b685f', fg='white')
        self.ms_2x0_0x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x0_1x0 = tk.Entry(self.square_frame_2x0, justify='center', bg='#6b685f', fg='white')
        self.ms_2x0_1x0.place(relx=0, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x0_1x1 = tk.Entry(self.square_frame_2x0, justify='center', bg='#6b685f', fg='white')
        self.ms_2x0_1x1.place(relx=0.01 + 0.98 / 3, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x0_1x2 = tk.Entry(self.square_frame_2x0, justify='center', bg='#6b685f', fg='white')
        self.ms_2x0_1x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x0_2x0 = tk.Entry(self.square_frame_2x0, justify='center', bg='#6b685f', fg='white')
        self.ms_2x0_2x0.place(relx=0, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x0_2x1 = tk.Entry(self.square_frame_2x0, justify='center', bg='#6b685f', fg='white')
        self.ms_2x0_2x1.place(relx=0.01 + 0.98 / 3, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x0_2x2 = tk.Entry(self.square_frame_2x0, justify='center', bg='#6b685f', fg='white')
        self.ms_2x0_2x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3,
                              relheight=0.98 / 3)

        # kwadrat 2x1
        self.ms_2x1_0x0 = tk.Entry(self.square_frame_2x1, justify='center', bg='#6b685f', fg='white')
        self.ms_2x1_0x0.place(relx=0, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x1_0x1 = tk.Entry(self.square_frame_2x1, justify='center', bg='#6b685f', fg='white')
        self.ms_2x1_0x1.place(relx=0.01 + 0.98 / 3, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x1_0x2 = tk.Entry(self.square_frame_2x1, justify='center', bg='#6b685f', fg='white')
        self.ms_2x1_0x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x1_1x0 = tk.Entry(self.square_frame_2x1, justify='center', bg='#6b685f', fg='white')
        self.ms_2x1_1x0.place(relx=0, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x1_1x1 = tk.Entry(self.square_frame_2x1, justify='center', bg='#6b685f', fg='white')
        self.ms_2x1_1x1.place(relx=0.01 + 0.98 / 3, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x1_1x2 = tk.Entry(self.square_frame_2x1, justify='center', bg='#6b685f', fg='white')
        self.ms_2x1_1x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x1_2x0 = tk.Entry(self.square_frame_2x1, justify='center', bg='#6b685f', fg='white')
        self.ms_2x1_2x0.place(relx=0, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x1_2x1 = tk.Entry(self.square_frame_2x1, justify='center', bg='#6b685f', fg='white')
        self.ms_2x1_2x1.place(relx=0.01 + 0.98 / 3, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x1_2x2 = tk.Entry(self.square_frame_2x1, justify='center', bg='#6b685f', fg='white')
        self.ms_2x1_2x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3,
                              relheight=0.98 / 3)

        # kwadrat 2x2
        self.ms_2x2_0x0 = tk.Entry(self.square_frame_2x2, justify='center', bg='#6b685f', fg='white')
        self.ms_2x2_0x0.place(relx=0, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x2_0x1 = tk.Entry(self.square_frame_2x2, justify='center', bg='#6b685f', fg='white')
        self.ms_2x2_0x1.place(relx=0.01 + 0.98 / 3, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x2_0x2 = tk.Entry(self.square_frame_2x2, justify='center', bg='#6b685f', fg='white')
        self.ms_2x2_0x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x2_1x0 = tk.Entry(self.square_frame_2x2, justify='center', bg='#6b685f', fg='white')
        self.ms_2x2_1x0.place(relx=0, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x2_1x1 = tk.Entry(self.square_frame_2x2, justify='center', bg='#6b685f', fg='white')
        self.ms_2x2_1x1.place(relx=0.01 + 0.98 / 3, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x2_1x2 = tk.Entry(self.square_frame_2x2, justify='center', bg='#6b685f', fg='white')
        self.ms_2x2_1x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.01 + 0.98 / 3, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x2_2x0 = tk.Entry(self.square_frame_2x2, justify='center', bg='#6b685f', fg='white')
        self.ms_2x2_2x0.place(relx=0, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x2_2x1 = tk.Entry(self.square_frame_2x2, justify='center', bg='#6b685f', fg='white')
        self.ms_2x2_2x1.place(relx=0.01 + 0.98 / 3, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3, relheight=0.98 / 3)
        self.ms_2x2_2x2 = tk.Entry(self.square_frame_2x2, justify='center', bg='#6b685f', fg='white')
        self.ms_2x2_2x2.place(relx=0.02 + (0.98 / 3) * 2, rely=0.02 + (0.98 / 3) * 2, relwidth=0.98 / 3,
                              relheight=0.98 / 3)

        self.entries_matrix = [
            [
                [
                    [self.ms_0x0_0x0, self.ms_0x0_0x1, self.ms_0x0_0x2],
                    [self.ms_0x0_1x0, self.ms_0x0_1x1, self.ms_0x0_1x2],
                    [self.ms_0x0_2x0, self.ms_0x0_2x1, self.ms_0x0_2x2]
                ],
                [
                    [self.ms_0x1_0x0, self.ms_0x1_0x1, self.ms_0x1_0x2],
                    [self.ms_0x1_1x0, self.ms_0x1_1x1, self.ms_0x1_1x2],
                    [self.ms_0x1_2x0, self.ms_0x1_2x1, self.ms_0x1_2x2]
                ],
                [
                    [self.ms_0x2_0x0, self.ms_0x2_0x1, self.ms_0x2_0x2],
                    [self.ms_0x2_1x0, self.ms_0x2_1x1, self.ms_0x2_1x2],
                    [self.ms_0x2_2x0, self.ms_0x2_2x1, self.ms_0x2_2x2]
                ]
            ],
            [
                [
                    [self.ms_1x0_0x0, self.ms_1x0_0x1, self.ms_1x0_0x2],
                    [self.ms_1x0_1x0, self.ms_1x0_1x1, self.ms_1x0_1x2],
                    [self.ms_1x0_2x0, self.ms_1x0_2x1, self.ms_1x0_2x2]
                ],
                [
                    [self.ms_1x1_0x0, self.ms_1x1_0x1, self.ms_1x1_0x2],
                    [self.ms_1x1_1x0, self.ms_1x1_1x1, self.ms_1x1_1x2],
                    [self.ms_1x1_2x0, self.ms_1x1_2x1, self.ms_1x1_2x2]
                ],
                [
                    [self.ms_1x2_0x0, self.ms_1x2_0x1, self.ms_1x2_0x2],
                    [self.ms_1x2_1x0, self.ms_1x2_1x1, self.ms_1x2_1x2],
                    [self.ms_1x2_2x0, self.ms_1x2_2x1, self.ms_1x2_2x2]
                ]
            ],
            [
                [
                    [self.ms_2x0_0x0, self.ms_2x0_0x1, self.ms_2x0_0x2],
                    [self.ms_2x0_1x0, self.ms_2x0_1x1, self.ms_2x0_1x2],
                    [self.ms_2x0_2x0, self.ms_2x0_2x1, self.ms_2x0_2x2]
                ],
                [
                    [self.ms_2x1_0x0, self.ms_2x1_0x1, self.ms_2x1_0x2],
                    [self.ms_2x1_1x0, self.ms_2x1_1x1, self.ms_2x1_1x2],
                    [self.ms_2x1_2x0, self.ms_2x1_2x1, self.ms_2x1_2x2]
                ],
                [
                    [self.ms_2x2_0x0, self.ms_2x2_0x1, self.ms_2x2_0x2],
                    [self.ms_2x2_1x0, self.ms_2x2_1x1, self.ms_2x2_1x2],
                    [self.ms_2x2_2x0, self.ms_2x2_2x1, self.ms_2x2_2x2]
                ]
            ]
        ]

    def zgromadz_dane(self):
        self.solution_matrix = self.create_empty_dict('')

        for dy in range(3):
            for dx in range(3):
                for my in range(3):
                    for mx in range(3):
                        if self.entries_matrix[dy][dx][my][mx].get() == '':
                            self.solution_matrix[f'{dy}{dx}{my}{mx}'] = ''
                        else:
                            self.solution_matrix[f'{dy}{dx}{my}{mx}'] = int(self.entries_matrix[dy][dx][my][mx].get())

    def wypelnij_poczatek(self):
        self.solution_matrix = self.create_empty_dict('')
        start_matrix = pozycja_startowa.start_matrix

        for dy in range (3):
            for dx in range (3):
                for my in range (3):
                    for mx in range (3):
                        if start_matrix[dy][dx][my][mx] != 0:
                            self.entries_matrix[dy][dx][my][mx].insert(0, start_matrix[dy][dx][my][mx])
                            self.solution_matrix[f'{dy}{dx}{my}{mx}'] = start_matrix[dy][dx][my][mx]
                        else:
                            pass

    def create_empty_dict(self, insert):
        dict = {}
        for dy in range (3):
            for dx in range (3):
                for my in range (3):
                    for mx in range (3):
                        dict[f'{dy}{dx}{my}{mx}'] = insert
        return dict

    def sprawdz_puste_pola(self):
        for dy in range (3):
            for dx in range (3):
                for my in range (3):
                    for mx in range (3):
                        if self.solution_matrix[f'{dy}{dx}{my}{mx}'] == '':
                            for n in range (1,10):
                                # print(n, dy, dx, my, mx, self.sprawdz_linie_pion(dy, dx, my, mx, n), self.sprawdz_linie_poziom(dy, dx, my, mx, n), self.sprawdz_kwadrat(dy, dx, my, mx, n))
                                pion = self.sprawdz_linie_pion(dy, dx, my, mx, n)
                                poziom = self.sprawdz_linie_poziom(dy, dx, my, mx, n)
                                kwadrat = self.sprawdz_kwadrat(dy, dx, my, mx, n)
                                if  pion == True and poziom == True and kwadrat == True:
                                    if str(n) not in self.possibilities_matrix[f'{dy}{dx}{my}{mx}']:
                                        self.possibilities_matrix[f'{dy}{dx}{my}{mx}'] += str(n)

    def policz_puste_pola(self):
        puste_pola = 0
        for dy in range (3):
            for dx in range (3):
                for my in range (3):
                    for mx in range (3):
                        if self.solution_matrix[f'{dy}{dx}{my}{mx}'] == '':
                            puste_pola += 1
        return puste_pola

    def sprawdz_linie_pion(self, dy, dx, my, mx, n_szukany):
        for dy_ in range (3):
            for my_ in range (3):
                if self.solution_matrix[f'{dy_}{dx}{my_}{mx}'] != n_szukany:
                    pass
                else:
                    return False
        return True

    def sprawdz_linie_poziom(self, dy, dx, my, mx, n_szukany):
        for dx_ in range (3):
            for mx_ in range (3):
                if self.solution_matrix[f'{dy}{dx_}{my}{mx_}'] != n_szukany:
                    pass
                else:
                    return False
        return True

    def sprawdz_kwadrat(self, dy, dx, my, mx, n_szukany):
        for my_ in range (3):
            for mx_ in range (3):
                if self.solution_matrix[f'{dy}{dx}{my_}{mx_}'] != n_szukany:
                    pass
                else:
                    return False
        return True

    def wypelnij_pola_pewne(self):
        for dy in range (3):
            for dx in range (3):
                for my in range (3):
                    for mx in range (3):
                        if len(self.possibilities_matrix[f'{dy}{dx}{my}{mx}']) == 1:
                            # print(f'{dy}{dx}{my}{mx}', int(self.possibilities_matrix[f'{dy}{dx}{my}{mx}']))
                            self.solution_matrix[f'{dy}{dx}{my}{mx}'] = int(self.possibilities_matrix[f'{dy}{dx}{my}{mx}'])
                            self.entries_matrix[dy][dx][my][mx].insert(0, self.possibilities_matrix[f'{dy}{dx}{my}{mx}'])
                        else:
                            for n in self.possibilities_matrix[f'{dy}{dx}{my}{mx}']:
                                ilosc_w_kwadracie = 0
                                for my_ in range (3):
                                    for mx_ in range (3):
                                        if n in self.possibilities_matrix[f'{dy}{dx}{my_}{mx_}']:
                                            ilosc_w_kwadracie += 1
                                if ilosc_w_kwadracie == 1:
                                    self.solution_matrix[f'{dy}{dx}{my}{mx}'] = n
                                    self.entries_matrix[dy][dx][my][mx].insert(0, n)

    def wyczysc_pola(self):
        for dy in range (3):
            for dx in range (3):
                for my in range (3):
                    for mx in range (3):
                        self.entries_matrix[dy][dx][my][mx].delete(0,'end')

class Menu_frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#3b1a1a')
        self.create_buttons()

    def create_buttons(self):
        self.wyczysc_button = tk.Button(self, text='WYCZYŚĆ POLA', bg='#694141', fg='#1a0626',
                                        command = self.controller.main_frame.wyczysc_pola)
        self.wyczysc_button.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

        self.solve_buttto = tk.Button(self, text='ROZWIĄŻ', bg='#694141', fg='#1a0626',
                                        command = self.controller.main_frame.solve_sudoku)
        self.solve_buttto.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.1)


if __name__ == "__main__":
    app = Main_Window()
    app.mainloop()