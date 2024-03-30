from tkinter import *
from CRUD import Selection_Window


def search_value(elements_in_list):
    def search_element_value():
        def get_back():
            element_value_window.destroy()
            Selection_Window.display_array_elements(elements_in_list)
        def linear_search(value):
            value = int(search_value_entry.get())
            elements = elements_in_list
            for i in range(len(elements)):
                if elements[i] == value:
                    return i
            return -1

        def find_the_val(search_value_entry):
            value = int(search_value_entry.get())
            result = linear_search(value)
            result_lbl = Label(v_main_frm, text=f"Value {value} is found at index {result + 1}",
                               font=("Poppins", 18, "bold"), fg="white", bg="black")
            result_lbl.place(x=280, y=330)

        # This is the interface of Search Value
        search_value_window.destroy()
        element_value_window = Tk()
        element_value_window.title("Create Read Update and Delete")
        element_value_window.geometry("800x600")

        # This is for Value main frame
        v_main_frm = Frame(element_value_window, width=800, height=600, bg="black")
        v_main_frm.place(x=0, y=0)

        # This is for search value label
        search_value_lbl = Label(v_main_frm, text="Search value: ", font=("Poppins", 18, "bold"), fg="white",
                                 bg="black")
        search_value_lbl.place(x=280, y=220)

        # This is for search value label
        search_value_entry = Entry(v_main_frm, width=3, font=("Poppins", 18, "bold"), fg="white", bg="black")
        search_value_entry.place(x=443, y=220)

        # This is for search button
        search_btn = Button(v_main_frm, text="SEARCH", font=("Poppins", 18, "bold"), fg="black", bg="orange",
                            command=lambda: find_the_val(search_value_entry))
        search_btn.place(x=280, y=270)
        back_btn = Button(v_main_frm, text="BACK", font=("Poppins", 16, "bold"), fg="white", bg="black", command=get_back)
        back_btn.place(x=450, y=280)
        element_value_window.mainloop()

    def search_index_value():
        def get_back():
            element_index_window.destroy()
            Selection_Window.display_array_elements(elements_in_list)

        def linear_search(value):
            value = int(search_index_entry.get())
            elements = elements_in_list
            for i in range(len(elements)):
                if value == elements[i]:
                    return i
            return -1

        def find_the_val(search_index_entry):
            value = int(search_index_entry.get())
            result = linear_search(value)
            result_lbl = Label(in_main_frm, text=f"Index {value} is found at value {result + 1}",
                               font=("Poppins", 18, "bold"), fg="white", bg="black")
            result_lbl.place(x=280, y=330)

        search_value_window.destroy()  # destroy the previous window

        # This is the interface of Search Value
        element_index_window = Tk()
        element_index_window.title("Create Read Update and Delete")
        element_index_window.geometry("800x600")

        # This is for Value main frame
        in_main_frm = Frame(element_index_window, width=800, height=600, bg="black")
        in_main_frm.place(x=0, y=0)

        # This is for search value label
        search_index_lbl = Label(in_main_frm, text="Search value: ", font=("Poppins", 18, "bold"), fg="white",
                                 bg="black")
        search_index_lbl.place(x=280, y=220)

        # This is for search value label
        search_index_entry = Entry(in_main_frm, width=3, font=("Poppins", 18, "bold"), fg="white", bg="black")
        search_index_entry.place(x=443, y=220)

        # This is for search button
        search_btn = Button(in_main_frm, text="SEARCH", font=("Poppins", 18, "bold"), fg="black", bg="orange",
                            command=lambda: find_the_val(search_index_entry))
        search_btn.place(x=280, y=270)
        back_btn = Button(in_main_frm, text="BACK", font=("Poppins", 16, "bold"), fg="white", bg="black", command=get_back)
        back_btn.place(x=450, y=270)
        element_index_window.mainloop()

    def back():
        search_value_window.destroy()
        Selection_Window.display_array_elements(elements_in_list)

    # This is the Interface of Search Value
    search_value_window = Tk()
    search_value_window.title("Create Read Update and Delete")
    search_value_window.geometry("800x600")
    sv_main_frm = Frame(search_value_window, width=800, height=600, bg="black")
    sv_main_frm.place(x=0, y=0)

    # This is for selection frame
    sv_selection_frm = Frame(sv_main_frm, width=300, height=250, bg="white")
    sv_selection_frm.place(x=250, y=100)

    # This is for index button
    index_btn = Button(sv_selection_frm, text="INDEX", font=("Poppins", 18, "bold"), fg="white", bg="black",
                       command=search_index_value)
    index_btn.place(x=105, y=40)

    # This is for value button
    val_btn = Button(sv_selection_frm, text="VALUE", font=("Poppins", 18, "bold"), fg="white", bg="blue",
                     command=search_element_value)
    val_btn.place(x=100, y=100)

    # This is for back button
    sv_back_btn = Button(sv_selection_frm, text="BACK", font=("Poppins", 18, "bold"), fg="white", bg="red",command=back)
    sv_back_btn.place(x=105, y=160)
    search_value_window.mainloop()


