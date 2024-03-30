from tkinter import *
from CRUD import Insert_Value
from CRUD import Search_Value
from CRUD import Delete_Value


def display_array_elements(elements_in_list):
    def back():
        selection_window.destroy()
        import Create_Elements

    def insert_value(elements_in_list):
        selection_window.destroy()
        Insert_Value.insert_value(elements_in_list)  # Pass the elements_in_list parameter to the insert_value function

    def search_value(elements_in_list):
        selection_window.destroy()
        Search_Value.search_value(elements_in_list)
        pass

    def delete_value(elements_in_list):
        selection_window.destroy()
        Delete_Value.delete_the_value(elements_in_list)

        pass

    selection_window = Tk()
    selection_window.title("Create Read Update and Delete")
    selection_window.geometry("800x600")
    main_frm = Frame(selection_window, width=800, height=600, bg="black")
    main_frm.place(x=0, y=0)

    # This is the frame for Insert value, Search value, Delete value, Back
    selection_frm = Frame(main_frm, width=300, height=280, bg="white")
    selection_frm.place(x=250, y=100)

    # This is the Label for the Inputted Elements of the user
    inputted_elements = Label(selection_window, text=f"ELEMENTS: {elements_in_list}", font=("Poppins", 18, "bold"),
                              fg="black", bg="white")
    inputted_elements.place(x=250, y=400)

    # This is the Button for Insert value
    insert_value_btn = Button(selection_frm, text="INSERT VALUE", font=("Poppins", 18, "bold"), fg="white",
                              bg="black", command=lambda: insert_value(elements_in_list))
    insert_value_btn.place(x=50, y=40)

    # This is the Button for Search value
    search_value_btn = Button(selection_frm, text="SEARCH VALUE", font=("Poppins", 18, "bold"), fg="white",
                              bg="blue", command=lambda: search_value(elements_in_list))
    search_value_btn.place(x=45, y=100)

    # This is the Button for Delete value
    delete_value_btn = Button(selection_frm, text="DELETE VALUE", font=("Poppins", 18, "bold"), fg="white",
                              bg="red", command=lambda: delete_value(elements_in_list))
    delete_value_btn.place(x=47, y=160)

    # This is the Button for Back
    back_btn = Button(selection_frm, text="BACK", font=("Poppins", 18, "bold"), fg="white", bg="orange", command=back)
    back_btn.place(x=100, y=220)

    selection_window.mainloop()
