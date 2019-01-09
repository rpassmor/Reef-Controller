import tkinter as tk
import time

LARGE_FONT = ("Verdana", 12)

class reef_controller(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (start_page, data_page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(start_page)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



        
class start_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def tick(time1=''):
            time2 = time.strftime('%H:%M:%S')
            if time2 != time1:
                time1=time2
                clock.config(text=time2)
            clock.after(200, tick)

        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        data_button = tk.Button(self, text="Visit Data Page", command=lambda: controller.show_frame(data_page))
        data_button.pack()

        clock =tk.Label(self, font=('times', 20, 'bold'), bg='green')
        clock.pack(fill='both', expand=1)
        tick()

    
        
        

        
class data_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Data Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        home_button = tk.Button(self, text="Visit Start Page", command=lambda: controller.show_frame(start_page))
        home_button.pack()

        

app = reef_controller()
app.mainloop()
