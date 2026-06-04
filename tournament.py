import os
import random
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

# Отключаем лимит на размер изображения
Image.MAX_IMAGE_PIXELS = None 

class TournamentApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Фото-Турнир")
        self.root.geometry("900x700")
        self.root.minsize(700, 500)
        
        self.style = ttk.Style()
        self.is_dark = True
        self.lang = 'ru' # Текущий язык ('ru' или 'en')
        self.set_theme_colors()
        self.init_texts() # Инициализация переводов

        self.folder_path = ""
        self.current_round_photos = []
        self.next_round_photos = []
        self.round_losers = []
        self.round_number = 1
        self.total_initial_photos = 0
        
        self.current_pair = (None, None)
        self.tk_img1 = None
        self.tk_img2 = None
        self.tk_img_winner = None

        self.setup_ui()

    def init_texts(self):
        self.texts = {
            'ru': {
                'theme_btn': "☀️ Светлая тема",
                'theme_btn_dark': "🌙 Тёмная тема",
                'lang_btn': " EN",
                'lang_btn_en': "🌐 RU",
                'progress_lbl': "Осталось в турнире: ",
                'select_folder_btn': "Выбрать папку с фото",
                'error_title': "Ошибка",
                'error_not_enough': "В папке недостаточно фотографий (нужно минимум 2).",
                'choose_left': "Выбрать левое",
                'choose_right': "Выбрать правое",
                'view_full': "Открыть в полном размере",
                'round_lbl': "Раунд ",
                'winner_title': "🏆 Турнир завершен! 🏆",
                'winner_lbl': "Абсолютный победитель: ",
                'view_winner': "Открыть победителя в полном размере",
                'restart_btn': "Выбрать новую папку / Начать заново"
            },
            'en': {
                'theme_btn': "☀️ Light Theme",
                'theme_btn_dark': "🌙 Dark Theme",
                'lang_btn': " RU",
                'lang_btn_en': " EN",
                'progress_lbl': "Remaining in tournament: ",
                'select_folder_btn': "Select Folder with Photos",
                'error_title': "Error",
                'error_not_enough': "Not enough photos in the folder (need at least 2).",
                'choose_left': "Choose Left",
                'choose_right': "Choose Right",
                'view_full': "View Full Size",
                'round_lbl': "Round ",
                'winner_title': "🏆 Tournament Finished! 🏆",
                'winner_lbl': "Absolute Winner: ",
                'view_winner': "View Winner in Full Size",
                'restart_btn': "Select New Folder / Restart"
            }
        }

    def t(self, key):
        # Вспомогательная функция для получения текста
        return self.texts[self.lang][key]

    def set_theme_colors(self):
        if self.is_dark:
            self.bg_color = "#2b2b2b"
            self.fg_color = "#ffffff"
            self.btn_bg = "#3c3f41"
            self.btn_fg = "#ffffff"
            self.accent_bg = "#4CAF50"
            self.progress_trough = "#3c3f41"
        else:
            self.bg_color = "#f0f0f0"
            self.fg_color = "#000000"
            self.btn_bg = "#e0e0e0"
            self.btn_fg = "#000000"
            self.accent_bg = "#d4edda"
            self.progress_trough = "#e0e0e0"

    def setup_ui(self):
        self.root.configure(bg=self.bg_color)
        self.style.theme_use('clam')
        self.style.configure("Horizontal.TProgressbar", 
                             troughcolor=self.progress_trough, 
                             background=self.accent_bg,
                             bordercolor=self.bg_color)

        # Верхняя панель
        self.top_frame = tk.Frame(self.root, bg=self.bg_color)
        self.top_frame.pack(fill='x', pady=10, padx=20)

        self.btn_theme = tk.Button(self.top_frame, text=self.t('theme_btn') if self.is_dark else self.t('theme_btn_dark'), 
                                   command=self.toggle_theme, bg=self.btn_bg, fg=self.btn_fg, font=("Arial", 10), relief='flat')
        self.btn_theme.pack(side='left', padx=5)

        self.btn_lang = tk.Button(self.top_frame, text=self.t('lang_btn'), 
                                  command=self.toggle_lang, bg=self.btn_bg, fg=self.btn_fg, font=("Arial", 10), relief='flat')
        self.btn_lang.pack(side='left', padx=5)

        self.progress_bar = ttk.Progressbar(self.top_frame, orient='horizontal', length=250, mode='determinate')
        self.progress_bar.pack(side='right', padx=15)

        self.lbl_progress = tk.Label(self.top_frame, text=self.t('progress_lbl') + "0", font=("Arial", 11), bg=self.bg_color, fg=self.fg_color)
        self.lbl_progress.pack(side='right')

        # Центральная область
        self.center_frame = tk.Frame(self.root, bg=self.bg_color)
        self.center_frame.pack(expand=True, fill='both', padx=20, pady=10)
        self.center_frame.columnconfigure(0, weight=1)
        self.center_frame.columnconfigure(1, weight=1)
        self.center_frame.rowconfigure(0, weight=1)

        self.btn_select = tk.Button(self.center_frame, text=self.t('select_folder_btn'), command=self.select_folder, 
                                    font=("Arial", 14, "bold"), bg=self.btn_bg, fg=self.btn_fg, padx=20, pady=10)
        self.btn_select.grid(row=0, column=0, columnspan=2)

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.set_theme_colors()
        self.style.configure("Horizontal.TProgressbar", troughcolor=self.progress_trough, background=self.accent_bg, bordercolor=self.bg_color)
        self.btn_theme.config(text=self.t('theme_btn') if self.is_dark else self.t('theme_btn_dark'), bg=self.btn_bg, fg=self.btn_fg)
        self.apply_theme_to_ui()
        self.refresh_current_screen()

    def toggle_lang(self):
        self.lang = 'en' if self.lang == 'ru' else 'ru'
        self.btn_lang.config(text=self.t('lang_btn'))
        self.apply_theme_to_ui() # Обновляем цвета, если нужно
        self.refresh_current_screen() # Перерисовываем экран с новыми текстами

    def apply_theme_to_ui(self):
        self.root.configure(bg=self.bg_color)
        self.top_frame.configure(bg=self.bg_color)
        self.center_frame.configure(bg=self.bg_color)
        self.lbl_progress.config(bg=self.bg_color, fg=self.fg_color, text=self.t('progress_lbl') + str(len(self.current_round_photos) + len(self.next_round_photos)))
        if hasattr(self, 'btn_select'):
            self.btn_select.config(bg=self.btn_bg, fg=self.btn_fg, text=self.t('select_folder_btn'))

    def refresh_current_screen(self):
        # Перерисовка текущего экрана при смене темы или языка
        if not self.folder_path:
            return
        if self.current_pair[0]:
            self.show_battle(self.current_pair[0], self.current_pair[1])
        elif len(self.current_round_photos) == 1 and len(self.next_round_photos) == 0:
            # Если мы на экране победителя (он уже pop-нут, но мы знаем, что турнир кончился)
            # В данном случае проще просто показать кнопку выбора папки, если мы не храним имя победителя отдельно,
            # но так как мы в show_final_winner переименовываем файл, мы можем просто показать экран рестарта.
            self.restart_tournament() 
        else:
            self.btn_select.config(text=self.t('select_folder_btn'))

    def update_progress(self):
        remaining = len(self.current_round_photos) + len(self.next_round_photos)
        self.lbl_progress.config(text=self.t('progress_lbl') + str(remaining))
        if self.total_initial_photos > 0:
            eliminated = self.total_initial_photos - remaining
            progress_percent = (eliminated / self.total_initial_photos) * 100
            self.progress_bar['value'] = progress_percent

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if not self.folder_path:
            return
            
        valid_exts = {'.jpg', '.jpeg', '.png', '.webp'}
        all_photos = [f for f in os.listdir(self.folder_path) if os.path.splitext(f)[1].lower() in valid_exts]
        
        if len(all_photos) < 2:
            from tkinter import messagebox
            messagebox.showwarning(self.t('error_title'), self.t('error_not_enough'))
            return
            
        random.shuffle(all_photos)
        self.current_round_photos = all_photos
        self.total_initial_photos = len(all_photos)
        self.round_number = 1
        self.next_round_photos = []
        self.round_losers = []
        
        self.btn_select.grid_forget()
        self.update_progress()
        self.prepare_next_battle()

    def prepare_next_battle(self):
        if len(self.current_round_photos) == 1 and len(self.next_round_photos) == 0:
            winner = self.current_round_photos.pop(0)
            self.show_final_winner(winner)
            return

        if len(self.current_round_photos) < 2:
            if len(self.current_round_photos) == 1:
                self.next_round_photos.append(self.current_round_photos.pop(0))
            self.finalize_round()
            return

        photo1 = self.current_round_photos.pop(0)
        photo2 = self.current_round_photos.pop(0)
        self.current_pair = (photo1, photo2)
        self.show_battle(photo1, photo2)

    def finalize_round(self):
        prefix = "zz_" if self.round_number == 1 else f"{self.round_number - 1}_"
        for loser in self.round_losers:
            self.rename_file(loser, prefix)
            
        self.round_losers = []
        self.current_round_photos = self.next_round_photos
        self.next_round_photos = []
        self.round_number += 1
        
        self.update_progress()
        self.prepare_next_battle()

    def show_battle(self, p1, p2):
        for widget in self.center_frame.winfo_children():
            widget.destroy()
            
        lbl_round = tk.Label(self.center_frame, text=self.t('round_lbl') + str(self.round_number), font=("Arial", 18, "bold"), bg=self.bg_color, fg=self.fg_color)
        lbl_round.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        def draw_side(photo_name, col_index, choice_text_key):
            path = os.path.join(self.folder_path, photo_name)
            img = Image.open(path)
            img.thumbnail((350, 350), Image.Resampling.BILINEAR)
            tk_img = ImageTk.PhotoImage(img)
            
            if col_index == 0: self.tk_img1 = tk_img
            else: self.tk_img2 = tk_img
                
            lbl = tk.Label(self.center_frame, image=tk_img, bg=self.bg_color)
            lbl.grid(row=1, column=col_index, padx=30, pady=5)
            
            lbl_name = tk.Label(self.center_frame, text=photo_name, font=("Arial", 10), wraplength=300, bg=self.bg_color, fg=self.fg_color)
            lbl_name.grid(row=2, column=col_index, padx=30, pady=2)
            
            btn_view = tk.Button(self.center_frame, text=self.t('view_full'), command=lambda: os.startfile(path), font=("Arial", 10), bg=self.btn_bg, fg=self.btn_fg)
            btn_view.grid(row=3, column=col_index, padx=30, pady=2)
            
            btn_choose = tk.Button(self.center_frame, text=self.t(choice_text_key), command=lambda: self.choose_winner(photo_name), font=("Arial", 12, "bold"), bg=self.accent_bg, fg="#000000", width=18, pady=5)
            btn_choose.grid(row=4, column=col_index, padx=30, pady=5)

        draw_side(p1, 0, 'choose_left')
        draw_side(p2, 1, 'choose_right')

    def show_final_winner(self, winner_name):
        final_winner_name = self.rename_file(winner_name, "WIN_")
        for widget in self.center_frame.winfo_children():
            widget.destroy()
            
        lbl_title = tk.Label(self.center_frame, text=self.t('winner_title'), font=("Arial", 24, "bold"), bg=self.bg_color, fg=self.fg_color)
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        path = os.path.join(self.folder_path, final_winner_name)
        img = Image.open(path)
        img.thumbnail((500, 500), Image.Resampling.BILINEAR)
        self.tk_img_winner = ImageTk.PhotoImage(img)
        
        lbl_img = tk.Label(self.center_frame, image=self.tk_img_winner, bg=self.bg_color)
        lbl_img.grid(row=1, column=0, columnspan=2, pady=10)
        
        lbl_name = tk.Label(self.center_frame, text=self.t('winner_lbl') + final_winner_name, font=("Arial", 14, "bold"), wraplength=600, bg=self.bg_color, fg=self.fg_color)
        lbl_name.grid(row=2, column=0, columnspan=2, pady=10)
        
        btn_view = tk.Button(self.center_frame, text=self.t('view_winner'), command=lambda: os.startfile(path), font=("Arial", 11), bg=self.btn_bg, fg=self.btn_fg, padx=15, pady=5)
        btn_view.grid(row=3, column=0, columnspan=2, pady=5)
        
        btn_restart = tk.Button(self.center_frame, text=self.t('restart_btn'), command=self.restart_tournament, font=("Arial", 14, "bold"), bg=self.accent_bg, fg="#000000", padx=20, pady=10)
        btn_restart.grid(row=4, column=0, columnspan=2, pady=30)

    def restart_tournament(self):
        self.folder_path = ""
        self.current_round_photos = []
        self.next_round_photos = []
        self.round_losers = []
        self.round_number = 1
        self.total_initial_photos = 0
        self.current_pair = (None, None)
        
        for widget in self.center_frame.winfo_children():
            widget.destroy()
            
        self.btn_select = tk.Button(self.center_frame, text=self.t('select_folder_btn'), command=self.select_folder, font=("Arial", 14, "bold"), bg=self.btn_bg, fg=self.btn_fg, padx=20, pady=10)
        self.btn_select.grid(row=0, column=0, columnspan=2)
        
        self.lbl_progress.config(text=self.t('progress_lbl') + "0")
        self.progress_bar['value'] = 0

    def choose_winner(self, winner_name):
        p1, p2 = self.current_pair
        loser_name = p2 if winner_name == p1 else p1
        self.next_round_photos.append(winner_name)
        self.round_losers.append(loser_name)
        self.update_progress()
        self.prepare_next_battle()

    def rename_file(self, filename, prefix):
        old_path = os.path.join(self.folder_path, filename)
        name, ext = os.path.splitext(filename)
        new_name = f"{prefix}{name}{ext}"
        new_path = os.path.join(self.folder_path, new_name)
        try:
            os.rename(old_path, new_path)
            return new_name
        except FileExistsError:
            new_name = f"{prefix}{name}_{random.randint(10, 99)}{ext}"
            new_path = os.path.join(self.folder_path, new_name)
            os.rename(old_path, new_path)
            return new_name

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TournamentApp()
    app.run()