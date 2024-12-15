from customtkinter import *
from PIL import Image

global app 

# TODO: keep on debuging

def show_answer(app, button, correct, next_func=None):
    if correct:
        button.configure(fg_color="green", hover_color="#00FFFFFF")
        button.configure(hover_color=str())
        
    else:
        button.configure(fg_color="red", hover_color="#00FFFFFF")
        
        
    if next_func:
        app.after(2000, lambda: [widget.destroy() for widget in app.winfo_children()])
        app.after(2000, next_func)


def clear(button, next_func, config_func, app=None):
    if app is None:
        raise ValueError("The 'app' parameter cannot be None")
    
    for widget in app.winfo_children():
        if widget != button:
            widget.destroy()
    app.after(500, button.destroy)
    app.after(500, lambda: next_func(app))
    app.after(500, lambda: config_func(app))



app = CTk()
app.geometry("800x900")

set_appearance_mode("dark")


def create_pandas_widgets(app):
    
    lbl1 = CTkLabel(master=app, 
                    text="Du hast Panda´s genommen",
                    text_color="white", font=('Impact', 30)
    )
    lbl1.place(relx=0.5, rely=0.2, anchor="n")

    def show_first_question():
        lbl1.destroy()
        lbl2 = CTkLabel(master=app, text="Frage 1", text_color="white", font=('Impact', 30))
        lbl2.place(relx=0.5, rely=0.3, anchor="n")

        def show_final_label():
            lbl3 = CTkLabel(master=app, text="Wie viele Pandas gibt es weltweit?", text_color="white", font=('Impact', 30))
            lbl3.place(relx=0.5, rely=0.4, anchor="center")

            def show_buttons():
                

                btn4 = CTkButton(master=app, 
                                 text="Weniger als 1000", 
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="dark green",
                                 border_color="light green",
                                 border_width=4,
                                 height=100, 
                                 width=250,
                                 command=lambda: show_answer(app, btn4, False, show_second_question))

                
                btn4.place(relx=0.3, rely=0.6, anchor="center")
                




                btn5 = CTkButton(master=app, 
                                 text="Zwischen 1000 und 2000",
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="dark green",
                                 border_color="light green",
                                 border_width=4,
                                 height=100,
                                 width=250, 
                                 command=lambda: show_answer(app, btn5, False, show_second_question)
)
                
                                 
                btn5.place(relx=0.3, rely=0.75, anchor="center")
                
                
                

                btn6 = CTkButton(master=app, 
                                 text="Mehr als 2000", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="dark green",
                                 border_color="light green",
                                 border_width=4, 
                                 height=100,
                                 width=250, 
                                 command=lambda: show_answer(app, btn6, False, show_second_question)

                )
                
                btn6.place(relx=0.7, rely=0.6, anchor="center")
                
                
                
                btn7 = CTkButton(master=app,
                                 text="Mehr als 3000",
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="dark green",
                                 border_color="light green",
                                 border_width=4, 
                                 height=100, 
                                 width=250,
                                 command=lambda: show_answer(btn7, False, app, show_second_question)
                )
                
                btn7.place(relx=0.7, rely=0.75, anchor="center")
               
                

            app.after(3000, show_buttons)

        app.after(3000, show_final_label)

    def show_second_question():
        lbl2 = CTkLabel(master=app, text="Frage 2", text_color="white", font=('Impact', 30))
        lbl2.place(relx=0.5, rely=0.3, anchor="n")

        def show_final_label():
            lbl3 = CTkLabel(master=app, text="In welchem Land leben die meisten Pandas?", text_color="white", font=('Impact', 30))
            lbl3.place(relx=0.5, rely=0.4, anchor="center")

            def show_buttons():

                
                
                btn4 = CTkButton(master=app, 
                                 text="China", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="dark green", 
                                 border_color="light green",
                                 border_width=4, 
                                 height=100,
                                 width=250,
                                 command=lambda: show_answer(btn4, True, app, show_third_question)
                )
                
                btn4.place(relx=0.3, rely=0.6, anchor="center")
                



                btn5 = CTkButton(master=app, 
                                 text="Indien",
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="dark green", 
                                 border_color="light green",
                                 border_width=4,
                                 height=100,
                                 width=250, 
                                 command=lambda: show_answer(btn5, False, app, show_third_question)
                )
                
                btn5.place(relx=0.3, rely=0.75, anchor="center")
                



                btn6 = CTkButton(master=app, 
                                 text="Japan",
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="dark green", 
                                 border_color="light green",
                                 border_width=4, 
                                 height=100,
                                 width=250,
                                 command=lambda: show_answer(btn6, False, app, show_third_question)
                )
                
                btn6.place(relx=0.7, rely=0.6, anchor="center")
                
                
                
                
                btn7 = CTkButton(master=app,
                                 text="Mongolei",
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="dark green",
                                 border_color="light green",
                                 border_width=4,
                                 height=100, 
                                 width=250,
                                 command=lambda: show_answer(btn7, False, app, show_third_question)
                )
                
                btn7.place(relx=0.7, rely=0.75, anchor="center")
                
                
            app.after(3000, show_buttons)

        app.after(3000, show_final_label)
                          
    def show_third_question():
        lbl2 = CTkLabel(master=app, text="Frage 3", text_color="white", font=('Impact', 30))
        lbl2.place(relx=0.5, rely=0.3, anchor="n")

        def show_final_label():
            lbl3 = CTkLabel(master=app, text="Wie alt werden pandas in der Wildnis durchschnittlich?", text_color="white", font=('Impact', 30))
            lbl3.place(relx=0.5, rely=0.4, anchor="center")

            def show_buttons():
            
                
                btn4 = CTkButton(master=app, 
                                 text="10 Jahre", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="dark green", 
                                 border_color="light green",
                                 border_width=4, 
                                 height=100,
                                 width=250,
                                 command=lambda: show_answer(btn4, False, app, show_menu) 
                )
                
                btn4.place(relx=0.3, rely=0.6, anchor="center")



                btn5 = CTkButton(master=app, 
                                 text="20 Jahre",
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="dark green", 
                                 border_color="light green",
                                 border_width=4,
                                 height=100,
                                 width=250, 
                                 command=lambda: show_answer(btn5, True, app, show_menu)
                )
                
                btn5.place(relx=0.3, rely=0.75, anchor="center")



                btn6 = CTkButton(master=app, 
                                 text="30 Jahre",
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="dark green", 
                                 border_color="light green",
                                 border_width=4, 
                                 height=100,
                                 width=250,
                                 command=lambda: show_answer(btn6, False, app, show_menu)
                )
                
                btn6.place(relx=0.7, rely=0.6, anchor="center")
                
                
                
                btn7 = CTkButton(master=app,
                                 text="Keins davon ist richtig",
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="dark green",
                                 border_color="light green",
                                 border_width=4,
                                 height=100, 
                                 width=250,
                                 command=lambda: show_answer(btn7, False, app, show_menu)
                )
                
                btn7.place(relx=0.7, rely=0.75, anchor="center")
                

            app.after(3000, show_buttons)

        app.after(3000, show_final_label)

    app.after(3000, show_first_question)

def create_nfs_widgets(app):
    
    lbl1 = CTkLabel(master=app,
                    text="Du hast Need For Speed Heat genommen", 
                    text_color="white", 
                    font=('Impact', 30)
    )
    lbl1.place(relx=0.5, rely=0.2, anchor="n")

    def show_first_question():
    
        lbl1.destroy()
        lbl2 = CTkLabel(master=app, 
                        text="Frage 1", 
                        text_color="white", 
                        font=('Impact', 30)
        )
        
        lbl2.place(relx=0.5, rely=0.3, anchor="n")

        def show_final_label():
            
            lbl3 = CTkLabel(master=app,
                            text="Wie heißt die Stadt, in der sich NFS Heat befindet?",
                            text_color="white", 
                            font=('Impact', 30))
            
            lbl3.place(relx=0.5, rely=0.4, anchor="center")

            def show_buttons():

                
                
                
                btn4 = CTkButton(master=app,
                                 text="Palm City",
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="#8a1d86",
                                 border_color="dark blue",
                                 border_width=4,
                                 height=100,
                                 width=250,
                                 command=lambda: show_answer(btn4, True, app, show_second_question))
                
                btn4.place(relx=0.3, rely=0.6, anchor="center")

                btn5 = CTkButton(master=app,
                                 text="Las Vegas",
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="#8a1d86",
                                 border_color="dark blue",
                                 border_width=4,
                                 height=100, 
                                 width=250, 
                                 command=lambda: show_answer(btn5, False, app, show_second_question))
                
                btn5.place(relx=0.3, rely=0.75, anchor="center")

                btn6 = CTkButton(master=app, 
                                 text="San Andreas", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#8a1d86",
                                 border_color="dark blue",
                                 border_width=4, 
                                 height=100, 
                                 width=250, 
                                 command=lambda: show_answer(btn6, False, app, show_second_question))
                
                btn6.place(relx=0.7, rely=0.6, anchor="center")

                btn7 = CTkButton(master=app, 
                                 text="Miami", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#8a1d86", 
                                 border_color="dark blue",
                                 border_width=4, 
                                 height=100, 
                                 width=250, 
                                 command=lambda: show_answer(btn7, False, app, show_second_question))
                
                btn7.place(relx=0.7, rely=0.75, anchor="center")

            app.after(3000, show_buttons)

        app.after(3000, show_final_label)

    def show_second_question():
        
        lbl2 = CTkLabel(master=app,
                        text="Frage 2",
                        text_color="white",
                        font=('Impact', 30)
        )
        
        lbl2.place(relx=0.5, rely=0.3, anchor="n")

        def show_final_label():
            
            lbl3 = CTkLabel(master=app, 
                            text="Welches Auto wird auf dem Cover von NFS Heat gezeigt?",
                            text_color="white", 
                            font=('Impact', 30)
            )
            
            lbl3.place(relx=0.5, rely=0.4, anchor="center")

            def show_buttons():
    
                
                
                btn4 = CTkButton(master=app,
                                 text="BMW M3 GTR",
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="#8a1d86", 
                                 border_color="dark blue",
                                 border_width=4,
                                 height=100,
                                 width=250, 
                                 command=lambda: show_answer(btn4, False, app, show_third_question)
                )
                
                btn4.place(relx=0.3, rely=0.6, anchor="center")

                btn5 = CTkButton(master=app, 
                                 text="Nissan Skyline GT-R", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#8a1d86",
                                 border_color="dark blue",
                                 border_width=4, 
                                 height=100,
                                 width=250, 
                                 command=lambda: show_answer(btn5, False, app, show_third_question)
                )
                
                btn5.place(relx=0.3, rely=0.75, anchor="center")

                btn6 = CTkButton(master=app,
                                 text="Ford Mustang",
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#8a1d86",
                                 border_color="dark blue",
                                 border_width=4,
                                 height=100, 
                                 width=250, 
                                 command=lambda: show_answer(btn6, True, app, show_third_question)
                )
                
                btn6.place(relx=0.7, rely=0.6, anchor="center")

                btn7 = CTkButton(master=app,
                                 text="Chevrolet Corvette", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#8a1d86",
                                 border_color="dark blue",
                                 border_width=4, height=100,
                                 width=250, 
                                 command=lambda: show_answer(btn7, False, app, show_third_question)
                )
                
                btn7.place(relx=0.7, rely=0.75, anchor="center")

            app.after(3000, show_buttons)

        app.after(3000, show_final_label)
        
    def show_third_question():
        
        lbl2 = CTkLabel(master=app,
                        text="Frage 3",
                        text_color="white",
                        font=('Impact', 30)
        )
        
        lbl2.place(relx=0.5, rely=0.3, anchor="n")

        def show_final_label():
            
            lbl3 = CTkLabel(master=app, 
                            text="Wann ist Need for Speed Heat erschienen?",
                            text_color="white", 
                            font=('Impact', 30)
            )
            
            lbl3.place(relx=0.5, rely=0.4, anchor="center")

            def show_buttons():
                

                
                btn4 = CTkButton(master=app,
                                 text="2012",
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="#8a1d86", 
                                 border_color="dark blue",
                                 border_width=4,
                                 height=100,
                                 width=250, 
                                 command=lambda: show_answer(btn4, False, app, show_menu)
                )
                
                btn4.place(relx=0.3, rely=0.6, anchor="center")

                btn5 = CTkButton(master=app, 
                                 text="1989", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#8a1d86",
                                 border_color="dark blue",
                                 border_width=4, 
                                 height=100,
                                 width=250, 
                                 command=lambda: show_answer(btn5, False, app, show_menu)
                )
                
                btn5.place(relx=0.3, rely=0.75, anchor="center")

                btn6 = CTkButton(master=app,
                                 text="2019",
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#8a1d86",
                                 border_color="dark blue",
                                 border_width=4,
                                 height=100, 
                                 width=250, 
                                 command=lambda: show_answer(btn6, True, app, show_menu)
                )
                
                btn6.place(relx=0.7, rely=0.6, anchor="center")

                btn7 = CTkButton(master=app,
                                 text="2023", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#8a1d86",
                                 border_color="dark blue",
                                 border_width=4, height=100,
                                 width=250,
                                 command=lambda: show_answer(btn7, False, app, show_menu)
                )
                
                btn7.place(relx=0.7, rely=0.75, anchor="center")

                app.after(3000, show_buttons)

            app.after(3000, show_final_label)

        app.after(3000, show_first_question )

def create_f1_widgets(app):
    
    
    lbl1 = CTkLabel(master=app, 
                    text="Du hast Formel 1 genommen", 
                    text_color="white",
                    font=('Impact', 30)
    )
    lbl1.place(relx=0.5, rely=0.2, anchor="n")
    

    def show_first_question():
        lbl1.destroy()
        lbl2 = CTkLabel(master=app, text="Frage 1", text_color="white", font=('Impact', 30))
        lbl2.place(relx=0.5, rely=0.2, anchor="n")

        def show_final_label():
            lbl3 = CTkLabel(master=app, text="Wer hat die meisten", text_color="white", font=('Impact', 30))
            lbl3.place(relx=0.5, rely=0.3, anchor="center")
            
            lbl4 = CTkLabel(master=app, text="F1-Weltmeisterschaften gewonnen (Im Jahr 2000)?", text_color="white", font=('Impact', 30))
            lbl4.place(relx=0.5, rely=0.4, anchor="center")


            def show_buttons():
                
                
                btn4 = CTkButton(master=app, 
                                 text="Michael Schumacher", 
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="#5c615e", 
                                 border_color="dark red",
                                 border_width=4,
                                 height=100,
                                 width=250, 
                                 command=lambda: show_answer(btn4, True, app, show_second_question)
                )
                
                btn4.place(relx=0.3, rely=0.6, anchor="center")



                btn5 = CTkButton(master=app, 
                                 text="Lewis Hamilton", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#5c615e", 
                                 border_color="dark red",
                                 border_width=4, 
                                 height=100, 
                                 width=250, 
                                 command=lambda: show_answer(btn5, False, app, show_second_question)
                )
                
                btn5.place(relx=0.3, rely=0.75, anchor="center")



                btn6 = CTkButton(master=app,
                                 text="Ayrton Senna",
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="#5c615e", 
                                 border_color="dark red",
                                 border_width=4,
                                 height=100, width=250, 
                                 command=lambda: show_answer(btn6, False, app, show_second_question)
                )
                
                btn6.place(relx=0.7, rely=0.6, anchor="center")


                btn7 = CTkButton(master=app,
                                 text="Juan Manuel Fangio", 
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="#5c615e", 
                                 border_color="dark red",
                                 border_width=4,
                                 height=100, 
                                 width=250,
                                 command=lambda: show_answer(btn7, False, app, show_second_question)
                )
                
                btn7.place(relx=0.7, rely=0.75, anchor="center")

            app.after(3000, show_buttons)

        app.after(3000, show_final_label)

    def show_second_question():
        lbl2 = CTkLabel(master=app,
                        text="Frage 2",
                        text_color="white", 
                        font=('Impact', 30))
        
        lbl2.place(relx=0.5, rely=0.2, anchor="n")

        def show_final_label():
            
            lbl3 = CTkLabel(master=app, 
                            text="Welches Team hat die meisten ", 
                            text_color="white", 
                            font=('Impact', 30))
            
            lbl3.place(relx=0.5, rely=0.3, anchor="center")
            
            
            lbl4 = CTkLabel(master=app, 
                            text="Konstrukteursmeisterschaften gewonnen?", 
                            text_color="white", 
                            font=('Impact', 30))
            
            lbl4.place(relx=0.5, rely=0.4, anchor="center")

            def show_buttons():
                
                btn4 = CTkButton(master=app, 
                                 text="Ferrari", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#5c615e", 
                                 border_color="dark red",
                                 border_width=4,
                                 height=100, 
                                 width=250, 
                                 command=lambda: show_answer(btn4, True, app, show_third_question)
                )
                
                btn4.place(relx=0.3, rely=0.6, anchor="center")

                btn5 = CTkButton(master=app, 
                                 text="McLaren", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#5c615e",
                                 border_color="dark red",
                                 border_width=4,
                                 height=100, 
                                 width=250,
                                 command=lambda: show_answer(btn5, False, app, show_third_question)
                )
                
                btn5.place(relx=0.3, rely=0.75, anchor="center")

                btn6 = CTkButton(master=app, 
                                 text="Mercedes", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#5c615e", 
                                 border_color="dark red",
                                 border_width=4, 
                                 height=100, 
                                 width=250, 
                                 command=lambda: show_answer(btn6, False, app, show_third_question)
                )
                btn6.place(relx=0.7, rely=0.6, anchor="center")

                btn7 = CTkButton(master=app,
                                 text="Red Bull Racing", 
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="#5c615e",
                                 border_color="dark red",
                                 border_width=4, 
                                 height=100, 
                                 width=250, 
                                 command=lambda: show_answer(btn7, False, app, show_third_question)
                )
                btn7.place(relx=0.7, rely=0.75, anchor="center")

            app.after(3000, show_buttons)

        app.after(3000, show_final_label)
    
    def show_third_question():
            
            lbl2 = CTkLabel(master=app,
                        text="Frage 2",
                        text_color="white", 
                        font=('Impact', 30))
        
            lbl2.place(relx=0.5, rely=0.3, anchor="n")

            def show_final_label():
            
                lbl3 = CTkLabel(master=app, 
                            text="Welcher Fahrer hat die WM NICHT am meisten gewonnen?", 
                            text_color="white", 
                            font=('Impact', 30))
            
                lbl3.place(relx=0.5, rely=0.4, anchor="center")

                def show_buttons():
                    

                    btn4 = CTkButton(master=app, 
                                 text="Michael Schumacher", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#5c615e", 
                                 border_color="dark red",
                                 border_width=4,
                                 height=100, 
                                 width=250, 
                                 command=lambda: show_answer(btn4, False, app, show_menu)
                     )
                
                    btn4.place(relx=0.3, rely=0.6, anchor="center")

                    btn5 = CTkButton(master=app, 
                                 text="Lewis Hamilton", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#5c615e",
                                 border_color="dark red",
                                 border_width=4,
                                 height=100, 
                                 width=250,
                                 command=lambda: show_answer(btn5, False, app, show_menu)
                )
                
                    btn5.place(relx=0.3, rely=0.75, anchor="center")

                    btn6 = CTkButton(master=app, 
                                 text="Max Verstappen", 
                                 corner_radius=25, 
                                 fg_color="black",
                                 hover_color="#5c615e", 
                                 border_color="dark red",
                                 border_width=4, 
                                 height=100, 
                                 width=250, 
                                 command=lambda: show_answer(btn6, True, app, show_menu)
                )
                    btn6.place(relx=0.7, rely=0.6, anchor="center")

                    btn7 = CTkButton(master=app,
                                 text="Logan Sargent", 
                                 corner_radius=25,
                                 fg_color="black",
                                 hover_color="#5c615e",
                                 border_color="dark red",
                                 border_width=4, 
                                 height=100, 
                                 width=250, 
                                 command=lambda: show_answer(btn7, True, app, show_menu)
                )
                    btn7.place(relx=0.7, rely=0.75, anchor="center")

                app.after(3000, show_buttons)

            app.after(3000, show_final_label)
    
    app.after(3000, show_first_question)
    


def show_menu():

    img = Image.open(r"")
    img2 = Image.open(r"")
    img3 = Image.open(r"")

    def config():
       app.after(0, lambda: (btn.configure(state="disabled", fg_color="gray")))

    lbl = CTkLabel(
               master=app,
               text="Wähle eine der drei möglichen aus:",
               text_color="white",
               font=('Impact', 30)
               )


    btn = CTkButton(
                master=app, 
                text="Panda´s", 
                corner_radius=25, 
                fg_color="black",
                hover_color="dark green", 
                border_color="light green",
                border_width=4,
                height=100, 
                width=250,
                image=CTkImage(dark_image=img, light_image=img),
                command=lambda: clear(btn, create_pandas_widgets, app)            
)

    btn2 = CTkButton(master=app, text="F1",
                 corner_radius=25, 
                 fg_color="black",
                 hover_color="#5c615e", 
                 border_color="dark red",
                 border_width=4,
                 height=100,
                 width=250,
                 image=CTkImage(dark_image=img2, light_image=img2),
                 command=lambda: clear(btn2, create_f1_widgets, app)
                 

)

    btn3 = CTkButton(master=app,text="NFS Heat",corner_radius=25, fg_color="black",hover_color="#8a1d86", border_color="dark blue",border_width=4,height=100, width=250,image=CTkImage(dark_image=img3, light_image=img3), command=lambda: clear(btn3, create_nfs_widgets, app)


                 

)

    lbl.place(relx=0.5, rely=0.2, anchor="center")
    btn.place(relx=0.5, rely=0.4, anchor="center")
    btn2.place(relx=0.5, rely=0.6, anchor="center")
    btn3.place(relx=0.5, rely=0.8, anchor="center")
    


app.after(0, show_menu)

app.mainloop()
