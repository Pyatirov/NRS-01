import customtkinter as c
import tkinter as tk
from utilities import Database, EncDecPass, User_Table,Chanel_Table,Material_Table,MathModel_Table,ProcessParams_Table
from databases import User,Chanel,Material,ProcessParams,MathModel
from sqlalchemy import select
from CTkMenuBar import *

width = 500
height = 500
class App(c.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(7, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

ROLE = ''
DATABASES = {
    'users': User,
    'chanel': Chanel,
    'material': Material,
    'math_model': MathModel,
    'process_params': ProcessParams,
}
database = Database()

def clear_frames(tables:list[c.CTkFrame]):
    if len(tables) != 0:
        for frame in tables:
            frame.pack_forget()
    print(f'tables:{len(tables)}')

tables_list:list[c.CTkFrame] = []

def tables_select(choice,frame:c.CTkFrame):
    match choice:
        case 'users':
            try:
                for widget in frame.winfo_children():
                    widget.destroy()
            except Exception as e:
                print(e)
            else:
                result = database.get_users()
                table = result[0]
                columns = result[1]

                table = User_Table(frame, table, columns)
                frame.pack(pady=30)
        case 'chanel':
            try:
                for widget in frame.winfo_children():
                    widget.destroy()
            except Exception as e:
                print(e)
            else:
                result = database.get_chanel_params()
                table = result[0]
                columns = result[1]

                table = Chanel_Table(frame, table, columns)
                frame.pack(pady=30)
        case 'material':
            try:
                for widget in frame.winfo_children():
                    widget.destroy()
            except Exception as e:
                print(e)
            else:
                result = database.get_materials()
                table = result[0]
                columns = result[1]

                table = Material_Table(frame, table, columns)
                frame.pack(pady=30)
        case 'math_model':
            try:
                for widget in frame.winfo_children():
                    widget.destroy()
            except Exception as e:
                print(e)
            else:
                result = database.get_math_module()
                table = result[0]
                columns = result[1]

                table = MathModel_Table(frame, table, columns)
                frame.pack(pady=30)
        case 'process_params':
            try:
                for widget in frame.winfo_children():
                    widget.destroy()
            except Exception as e:
                print(e)
            else:
                result = database.get_process_params()
                table = result[0]
                columns = result[1]

                table = ProcessParams_Table(frame, table, columns)
                frame.pack(pady=30)

def donothing():
    pass

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)



# Login window
class Login(App):
    def __init__(self):
        super().__init__()

        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)

        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.title(" FLOWMODEL")
        self.configure(fg_color='#232E33', pady=80, padx=0)

        # Login label
        self.login = c.CTkLabel(self, text="Авторизация", font=('Bell MT', 30))
        self.login.grid(row=0, pady=10)

        # Username
        # Frame
        self.username_frame = c.CTkFrame(self, fg_color='#232E33')
        self.username_frame.grid_rowconfigure(2, weight=0)
        self.username_frame.grid(row=1, pady=10)

        # Label
        # self.username_label = c.CTkLabel(self.username_frame, text='Username', anchor="w", justify="left",
        #                                  width=200, height=30)
        # self.username_label.grid(row=0)

        # Entry
        self.username = c.CTkEntry(self.username_frame, placeholder_text='Логин', text_color='#000000',
                                   placeholder_text_color='#000000', fg_color='#D9D9D9', border_width=0,
                                   width=200, height=40, corner_radius=30)
        self.username.grid(row=1)

        # Password
        # Frame
        self.password_frame = c.CTkFrame(self, fg_color='#232E33')
        self.password_frame.grid_rowconfigure(2, weight=0)
        self.password_frame.grid(row=2, pady=15)

        # Entry
        self.password = c.CTkEntry(self.password_frame, placeholder_text='Пароль', show='*', text_color='#000000',
                                   placeholder_text_color='#000000', fg_color='#D9D9D9', border_width=0,
                                   width=200, height=40, corner_radius=30)
        self.password.grid(row=1)

        # Admin / user frame
        self.frame = c.CTkFrame(self, fg_color='#232E33')
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid(row=3)

        # radio_var = tkinter.IntVar(value=0)
        # Combobox
        self.combobox_var = c.StringVar(value="Роль")
        self.combobox = c.CTkComboBox(self.frame, values=["Администратор", "Исследователь"], corner_radius=30,
                                      fg_color='#D9D9D9',
                                      command=self.user_select_event, variable=self.combobox_var, width=200,
                                      text_color='#000000', state='readonly', height=40, dropdown_font=('', 20))
        self.combobox.grid(column=0, row=0, pady=10)

        # Login button
        self.login_button = c.CTkButton(self, text='Войти', command=self.login_button, width=200, fg_color='#17203D',
                                        corner_radius=15)
        self.login_button.grid(row=4, pady=5)

        # Invalid user
        self.label = c.CTkLabel(self, text='Пользователь не найден!', text_color='red')

        # No account
        self.no_account_frame = c.CTkFrame(self, fg_color='#232E33', width=200, height=30)
        self.no_account_frame.grid_columnconfigure(2, weight=0)
        self.no_account_frame.grid(row=6)

        # No account label
        self.no_account_label = c.CTkLabel(self.no_account_frame, text='Нет в системе?')
        self.no_account_label.grid(column=0, row=0, padx=5)

        self.signup = c.CTkLabel(self.no_account_frame, text='Регистрация', text_color='#3DB3FF', cursor='mouse')
        self.signup.bind("<Button-1>", self.signup_command)
        self.signup.grid(column=1, row=0)

    def user_select_event(self, selection):
        print(selection)

    def login_button(self):
        database = Database()

        # user = select(User).where(User.username == self.username.get())
        # print(user)
        # result = database.select_user(user)

        username = self.username.get()
        password = self.password.get()
        role = self.combobox.get()
        user = User(username,password,role)

        result = database.select_user(user, self.username.get())
        print(result)
        if result is not None:
            print(f'User password: {result.password}')
            decryptor = EncDecPass()
            user_password = decryptor.decrypt_password(encoded_password=result.password).decode()
            print(f'Decrypted password: {user_password}')

            if password == user_password:
                print('Login success')
                self.destroy()
                main = Main()
                main.mainloop()

        else :
            self.label.grid(row=5)

    def signup_command(self, event):
        try:
            self.destroy()
        except Exception:
            print(Exception)
        finally:
            signup = SignUp()
            signup.mainloop()


# Sign up window
class SignUp(App):
    def __init__(self):
        super().__init__()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)

        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.title("FLOWMODEL")
        self.configure(fg_color='#232E33', pady=80, padx=0)

        # Login label
        self.login = c.CTkLabel(self, text="Регистрация", font=('Bell MT', 30))
        self.login.grid(row=0, pady=10)

        # Username
        # Frame
        self.username_frame = c.CTkFrame(self, fg_color='#232E33')
        self.username_frame.grid_rowconfigure(2, weight=0)
        self.username_frame.grid(row=1, pady=10)

        # Label
        # self.username_label = c.CTkLabel(self.username_frame, text='Username', anchor="w", justify="left",
        #                                  width=200, height=30)
        # self.username_label.grid(row=0)

        # Entry
        self.username = c.CTkEntry(self.username_frame, placeholder_text='Логин', text_color='#000000',
                                   placeholder_text_color='#000000', fg_color='#D9D9D9', border_width=0,
                                   width=200, height=40, corner_radius=30)
        self.username.grid(row=1)

        # Password
        # Frame
        self.password_frame = c.CTkFrame(self, fg_color='#232E33')
        self.password_frame.grid_rowconfigure(2, weight=0)
        self.password_frame.grid(row=2, pady=15)

        # Entry
        self.password = c.CTkEntry(self.password_frame, placeholder_text='Пароль', show='*', text_color='#000000',
                                   placeholder_text_color='#000000', fg_color='#D9D9D9', border_width=0,
                                   width=200, height=40, corner_radius=30)
        self.password.grid(row=1)

        # Admin / user frame
        self.frame = c.CTkFrame(self, fg_color='#232E33')
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid(row=3)

        radio_var = tk.IntVar(value=0)

        # combobox - User role
        self.combobox_var = c.StringVar(value="Роль")
        self.combobox = c.CTkComboBox(self.frame, values=["Администратор", "Исследователь"], corner_radius=30,
                                      fg_color='#D9D9D9',
                                      command=self.user_select_event, variable=self.combobox_var, width=200,
                                      text_color='#000000', state='readonly', height=40, dropdown_font=('', 20))
        self.combobox.grid(column=0, row=0, pady=10)

        # Login button
        self.login_button = c.CTkButton(self, text='Зарегистрироваться', command=self.signup_button_click, width=200,
                                        fg_color='#17203D',
                                        corner_radius=15)
        self.login_button.grid(row=4, pady=5)

        # No account
        self.no_account_frame = c.CTkFrame(self, fg_color='#232E33', width=200, height=30)
        self.no_account_frame.grid_columnconfigure(2, weight=0)
        self.no_account_frame.grid(row=5)

        # No account label
        self.no_account_label = c.CTkLabel(self.no_account_frame, text='Уже в системе?')
        self.no_account_label.grid(column=0, row=0, padx=5)

        self.signup = c.CTkLabel(self.no_account_frame, text='Войти', text_color='#3DB3FF', cursor='mouse')
        self.signup.bind("<Button-1>", self.login_command)
        self.signup.grid(column=1, row=0)

    def user_select_event(self, role):
        print(role)
        global ROLE
        ROLE = role

    def signup_button_click(self):
        global ROLE
        print('Sign up according to the user class')
        username = self.username.get()
        password = self.password.get()
        # role = ROLE
        print((username, password, ROLE))
        user = User(username, password, ROLE)
        database = Database()
        try:
            database.session.add(user)
            database.session.commit()
            print('User successfully added...')
            self.signup_command(True)
        except Exception:
            print(Exception)

    def login_command(self, event):
        self.destroy()
        login = Login()
        login.mainloop()

    def signup_command(self, event: bool):
        pass



