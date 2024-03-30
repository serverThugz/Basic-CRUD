from tkinter import *
from tkinter import messagebox

manipulating_array_window = None  # Declare as a global variable
def create_array(sizeArray_entry, num_ofArray_entry):
    try:
        size_of_array = int(sizeArray_entry.get())
        elements_in_list = num_ofArray_entry.get().split(',')

        # Convert input elements to integers
        elements_in_list = [int(element) for element in num_ofArray_entry.get().split(',')]


        if len(elements_in_list) != size_of_array:
            messagebox.showerror("Error", "Number of elements does not match the specified size of the array.")
            return

        # Check for presence of numbers
        array = list(range(1, size_of_array + 1))
        all_present = all(num in array for num in elements_in_list)
        some_present = any(num in array for num in elements_in_list)

        if all_present:

            def insert_value():
                def insert_the_value(insert_value_entry):
                    value = int(insert_value_entry.get())
                    elements_in_list.append(value)
                    see_elements = Label(iv_main_frm,text=f"Elements: {elements_in_list}",font=("Poppins", 18, "bold"), fg="white",
                                         bg="black")
                    see_elements.place(x=280, y=330)


                new_window_array.destroy()
                insert_value_window = Tk()
                insert_value_window.title("Create Read Update and Delete")
                insert_value_window.geometry("800x600")
                iv_main_frm = Frame(insert_value_window, width=800, height=600, bg="black")
                iv_main_frm.place(x=0, y=0)

                # This is a Label for Insert value
                insert_value_lbl = Label(iv_main_frm, text="Insert value: ", font=("Poppins", 18, "bold"), fg="white",
                                         bg="black")
                insert_value_lbl.place(x=280, y=220)

                # This is an Entry for Insert label
                insert_value_entry = Entry(iv_main_frm, width=3, font=("Poppins", 18, "bold"), fg="white", bg="black")
                insert_value_entry.place(x=443, y=220)

                # This is for search button
                insert_btn = Button(iv_main_frm, text="INSERT", font=("Poppins", 18, "bold"), fg="black", bg="orange",command=lambda: insert_the_value(insert_value_entry))
                insert_btn.place(x=280, y=270)
                insert_value_window.mainloop()


            def search_value():

                def search_element_value():
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
                        result_lbl = Label(v_main_frm,text=f"Value {value} is found at index {result + 1}",font=("Poppins",18,"bold"),fg="white",bg="black")
                        result_lbl.place(x=280, y=330)


                    search_value_window.destroy() # destroy the previous window

                    # This is the interface of Search Value
                    element_value_window = Tk()
                    element_value_window.title("Create Read Update and Delete")
                    element_value_window.geometry("800x600")

                    # This is for Value main frame
                    v_main_frm = Frame(element_value_window, width=800, height=600, bg="black")
                    v_main_frm.place(x=0,y=0)

                    # This is for search value label
                    search_value_lbl = Label(v_main_frm,text="Search value: ",font=("Poppins",18,"bold"),fg="white",bg="black")
                    search_value_lbl.place(x=280, y=220)

                    # This is for search value label
                    search_value_entry = Entry(v_main_frm,width=3,font=("Poppins",18,"bold"),fg="white",bg="black")
                    search_value_entry.place(x=443, y=220)

                    # This is for search button
                    search_btn = Button(v_main_frm,text="SEARCH",font=("Poppins",18,"bold"),fg="black",bg="orange",command=lambda: find_the_val(search_value_entry))
                    search_btn.place(x=280,y=270)
                    element_value_window.mainloop()

                def search_index_value():
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
                        result_lbl = Label(in_main_frm,text=f"Index {value} is found at value {result + 1}",font=("Poppins",18,"bold"),fg="white",bg="black")
                        result_lbl.place(x=280, y=330)


                    search_value_window.destroy() # destroy the previous window

                    # This is the interface of Search Value
                    element_index_window = Tk()
                    element_index_window.title("Create Read Update and Delete")
                    element_index_window.geometry("800x600")

                    # This is for Value main frame
                    in_main_frm = Frame(element_index_window, width=800, height=600, bg="black")
                    in_main_frm.place(x=0,y=0)

                    # This is for search value label
                    search_index_lbl = Label(in_main_frm,text="Search value: ",font=("Poppins",18,"bold"),fg="white",bg="black")
                    search_index_lbl.place(x=280, y=220)

                    # This is for search value label
                    search_index_entry = Entry(in_main_frm,width=3,font=("Poppins",18,"bold"),fg="white",bg="black")
                    search_index_entry.place(x=443, y=220)

                    # This is for search button
                    search_btn = Button(in_main_frm,text="SEARCH",font=("Poppins",18,"bold"),fg="black",bg="orange",command=lambda: find_the_val(search_index_entry))
                    search_btn.place(x=280,y=270)
                    element_index_window.mainloop()



                new_window_array.destroy()
                search_value_window = Tk()
                search_value_window.title("Create Read Update and Delete")
                search_value_window.geometry("800x600")
                sv_main_frm = Frame(search_value_window, width=800, height=600, bg="black")
                sv_main_frm.place(x=0, y=0)

                # This is for selection frame
                sv_selection_frm = Frame(sv_main_frm,width=300, height=250,bg="white")
                sv_selection_frm.place(x=250,y=100)

                # This is for index button
                index_btn = Button(sv_selection_frm,text="INDEX",font=("Poppins",18,"bold"),fg="white",bg="black",command=search_index_value)
                index_btn.place(x=105, y=40)

                # This is for value button
                val_btn = Button(sv_selection_frm,text="VALUE",font=("Poppins",18,"bold"),fg="white",bg="blue",command=search_element_value)
                val_btn.place(x=100, y=100)

                # This is for back button
                sv_back_btn = Button(sv_selection_frm, text="BACK", font=("Poppins", 18, "bold"), fg="white", bg="red")
                sv_back_btn.place(x=105, y=160)
                search_value_window.mainloop()




            def delete_value():

                def back():
                    delete_value_window.destroy()
                    new_window_array.deiconify()
                def delete_the_value(delete_value_entry):
                    value = int(delete_value_entry.get())
                    for element in elements_in_list:
                        if value == element:
                            del elements_in_list[value - 1]

                    see_elements = Label(del_main_frm,text=f"Elements: {elements_in_list}",font=("Poppins", 18, "bold"), fg="white",
                                         bg="black")
                    see_elements.place(x=280, y=330)
                    back_btn = Button(del_main_frm, text="Back", font=("Poppins", 18, "bold"), fg="white", bg="black", width=5, command=back)
                    back_btn.place(x=280, y=380)




                new_window_array.destroy()
                delete_value_window = Tk()
                delete_value_window.title("Create Read Update and Delete")
                delete_value_window.geometry("800x600")
                del_main_frm = Frame(delete_value_window, width=800, height=600, bg="black")
                del_main_frm.place(x=0, y=0)

                # This is a Label for Insert value
                delete_value_lbl = Label(del_main_frm, text="Delete value: ", font=("Poppins", 18, "bold"), fg="white",
                                         bg="black")
                delete_value_lbl.place(x=280, y=220)

                # This is an Entry for Insert label
                delete_value_entry = Entry(del_main_frm, width=3, font=("Poppins", 18, "bold"), fg="white", bg="black")
                delete_value_entry.place(x=443, y=220)

                # This is for search button
                delete_btn = Button(del_main_frm, text="DELETE", font=("Poppins", 18, "bold"), fg="black", bg="orange",command=lambda: delete_the_value(delete_value_entry))
                delete_btn.place(x=280, y=270)
                delete_value_window.mainloop()


            def back():
                pass


            manipulating_array_window.destroy()
            new_window_array = Tk()
            new_window_array.title("Create Read Update and Delete")
            new_window_array.geometry("800x600")
            main_frm = Frame(new_window_array, width=800, height=600, bg="black")
            main_frm.place(x=0, y=0)

            # This is the frame for Insert value, Search value, Delete value, Back
            selection_frm = Frame(main_frm, width=300, height=280,bg="white")
            selection_frm.place(x=250,y=100)

            # This is the Label for the Inputted Elements of the user
            inputted_elements = Label(new_window_array,text=f"ELEMENTS: {elements_in_list}",font=("Poppins",18,"bold"),fg="black",bg="white")
            inputted_elements.place(x=250,y=400)

            # This is the Button for Insert value
            insert_value_btn = Button(selection_frm,text="INSERT VALUE",font=("Poppins",18,"bold"),fg="white",bg="black",command=insert_value)
            insert_value_btn.place(x=50,y=40)

            # This is the Button for Search value
            search_value_btn = Button(selection_frm,text="SEARCH VALUE",font=("Poppins",18,"bold"),fg="white",bg="blue",command=search_value)
            search_value_btn.place(x=45,y=100)

            # This is the Button for Delete value
            delete_value_btn = Button(selection_frm,text="DELETE VALUE",font=("Poppins",18,"bold"),fg="white",bg="red",command=delete_value)
            delete_value_btn.place(x=47,y=160)

            # This is the Button for Back
            back_btn = Button(selection_frm,text="BACK",font=("Poppins",18,"bold"),fg="white",bg="orange",command=back)
            back_btn.place(x=100,y=220)

            new_window_array.mainloop()

        elif some_present:
            messagebox.showinfo("Result", "Some of the entered numbers are present in the array.")
        else:
            messagebox.showinfo("Result", "None of the entered numbers are present in the array.")

    except ValueError as e:
        messagebox.showinfo("Error","Please Fill Up correctly")
        messagebox.showerror("Error", str(e))

def clear():
    sizeArray_entry.delete(0,END)
    num_ofArray_entry.delete(0,END)

# This is the GUI part
manipulating_array_window = Tk()
manipulating_array_window.title("Create Read Update and Delete")
manipulating_array_window.geometry("800x600")

# This is the main Frame for interface
main_frm = Frame(manipulating_array_window, width=800, height=600, bg="black")
main_frm.place(x=0, y=0)

# This is the label for size of array
sizeArray_lbl = Label(main_frm, text="Size of Array:", font=("Poppins", 18, "bold"), fg="white", bg="black")
sizeArray_lbl.place(x=230, y=180)

# This is the label for Number of array
num_ofArray_lbl = Label(main_frm, text="Enter number  of Array:", font=("Poppins", 18, "bold"),fg="white", bg="black")
num_ofArray_lbl.place(x=120, y=240)

# This is Entry for size of Array
sizeArray_entry = Entry(main_frm, width=20, font=("Poppins", 18, "bold"), fg="white", bg="black")
sizeArray_entry.place(x=400, y=180)

# This is Entry for Number of array
num_ofArray_entry = Entry(main_frm, width=20, font=("Poppins", 18, "bold"), fg="white", bg="black")
num_ofArray_entry.place(x=400, y=240)

# This is for create button
create_btn = Button(main_frm, text="Create", font=("Poppins", 18, "bold"), fg="black",bg="orange", command=lambda: create_array(sizeArray_entry, num_ofArray_entry))
create_btn.place(x=120, y=350)

# This is for back button
clear_btn = Button(main_frm, text="Clear", font=("Poppins", 18, "bold"), fg="white", bg="black", width=5,command=clear)
clear_btn.place(x=270, y=350)

manipulating_array_window.mainloop()
