import tkinter as tk
from PIL import Image, ImageTk
from config import image_path, btn_rust, btn_life
import pygame

pygame.mixer.init()
pygame.mixer.music.load(image_path() + "\\clan_player.mp3")


class CreateBtns:
    def __init__(self, master):
        self.master = master
        image_btns_path = image_path()
        image_btn_on = Image.open(image_btns_path + "\\btn_on.png")
        self.on_btn = ImageTk.PhotoImage(image_btn_on)
        image_btn_off = Image.open(image_btns_path + "\\btn_off.png")
        self.off_btn = ImageTk.PhotoImage(image_btn_off)
        self.btn_rust_on = False
        self.btn_life_on = False
        self.create_btn_rust(btn_rust["cords"])
        self.create_btn_life(btn_life["cords"])

    def create_btn_rust(self, cord):
        self.button_rust = tk.Button(self.master,
                           image=self.off_btn,
                           borderwidth=0,
                           highlightthickness=0,
                           bg='white',
                           activebackground='white',
                           relief='flat'
                           )
        self.button_rust.image = self.off_btn
        self.btn_rust_on = False
        self.button_rust.config(command=self.toggle_rust)
        self.button_rust.place(x=cord[0],
                     y=cord[1])

    def toggle_rust(self):
        if self.btn_life_on == True and self.btn_rust_on == False:
            self.toggle_life()
        if self.btn_rust_on:
            pygame.mixer.music.stop()

            self.button_rust.config(image=self.off_btn)
            self.button_rust.image = self.off_btn
        else:
            pygame.mixer.music.play()
            self.button_rust.config(image=self.on_btn)
            self.button_rust.image = self.on_btn
        self.btn_rust_on = not self.btn_rust_on

    def create_btn_life(self, cord):
        self.button_life = tk.Button(self.master,
                           image=self.off_btn,
                           borderwidth=0,
                           highlightthickness=0,
                           bg='white',
                           activebackground='white',
                           relief='flat'
                           )
        self.button_life.image = self.off_btn
        self.btn_life_on = False
        self.button_life.config(command=self.toggle_life)
        self.button_life.place(x=cord[0],
                                y=cord[1])

    def toggle_life(self):
        if self.btn_rust_on == False:
            if self.btn_life_on:
                self.button_life.config(image=self.off_btn)
                self.button_life.image = self.off_btn
            else:
                self.button_life.config(image=self.on_btn)
                self.button_life.image = self.on_btn
            self.btn_life_on = not self.btn_life_on
