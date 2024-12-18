from owlready2 import get_ontology
from tkinter import *
from tkinter import ttk

# Load the ontology
ontology_file = "AI_ITS.owl"  # Replace with your ontology file path
ontology = get_ontology(ontology_file).load()

# Function to fetch classes
def fetch_classes():
    listbox.delete(0, "end")
    for cls in ontology.classes():
        listbox.insert("end", f"Class: {cls.name}")

# Function to fetch individuals
def fetch_individuals():
    listbox.delete(0, "end")
    for individual in ontology.individuals():
        listbox.insert("end", f"Individual: {individual.name}")

# Function to fetch object properties
def fetch_object_properties():
    listbox.delete(0, "end")
    for prop in ontology.object_properties():
        listbox.insert("end", f"Object Property: {prop.name}")

# Function to fetch data properties
def fetch_data_properties():
    listbox.delete(0, "end")
    for prop in ontology.data_properties():
        listbox.insert("end", f"Data Property: {prop.name}")

# Function to search ontology
def search_ontology():
    query = search_var.get().lower()
    listbox.delete(0, "end")
    for cls in ontology.classes():
        if query in cls.name.lower():
            listbox.insert("end", f"Class: {cls.name}")
    for individual in ontology.individuals():
        if query in individual.name.lower():
            listbox.insert("end", f"Individual: {individual.name}")
    for prop in ontology.object_properties():
        if query in prop.name.lower():
            listbox.insert("end", f"Object Property: {prop.name}")
    for prop in ontology.data_properties():
        if query in prop.name.lower():
            listbox.insert("end", f"Data Property: {prop.name}")

# Initialize Root
root = Tk()
root.title("AI ITS Ontology Viewer")
root.geometry("850x700")
root.configure(bg="#0f172a")  # Dark blue background

# Gradient Header
canvas = Canvas(root, height=100, bg="#0f172a", highlightthickness=0)
canvas.pack(fill=X)
canvas.create_rectangle(0, 0, 850, 100, fill="#2563eb", outline="")  # Blue Header

header = Label(root, text="AI ITS Ontology Viewer", font=("Verdana", 24, "bold"), fg="white", bg="#2563eb")
header.place(x=250, y=20)

# Search Frame
search_frame = Frame(root, bg="#0f172a", pady=10)
search_frame.pack(fill=X)

search_var = StringVar()
search_entry = Entry(search_frame, textvariable=search_var, font=("Arial", 14), width=40, relief="flat", bd=0)
search_entry.pack(side=LEFT, padx=20, pady=5)
search_entry.configure(bg="#1e293b", fg="white", insertbackground="white")

search_button = Button(search_frame, text="Search", font=("Arial", 12, "bold"), bg="#1e40af", fg="white", relief="flat",
                       activebackground="#3b82f6", activeforeground="white", command=search_ontology)
search_button.pack(side=LEFT, padx=10)

# Button Frame
button_frame = Frame(root, bg="#0f172a", pady=10)
button_frame.pack(fill=X)

def create_button(frame, text, command):
    button = Button(frame, text=text, font=("Arial", 12, "bold"), bg="#1e40af", fg="white", relief="flat",
                    activebackground="#3b82f6", activeforeground="white", padx=10, pady=5, command=command)
    button.pack(side=LEFT, padx=10, pady=5)
    return button

create_button(button_frame, "Show Classes", fetch_classes)
create_button(button_frame, "Show Individuals", fetch_individuals)
create_button(button_frame, "Show Object Properties", fetch_object_properties)
create_button(button_frame, "Show Data Properties", fetch_data_properties)

# Listbox Frame with Scrollbar
listbox_frame = Frame(root, bg="#0f172a")
listbox_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(
    listbox_frame, yscrollcommand=scrollbar.set, font=("Courier", 14), bg="#1e293b", fg="#e2e8f0",
    selectbackground="#3b82f6", selectforeground="white", relief="flat", highlightthickness=2, highlightcolor="#3b82f6"
)
listbox.pack(fill=BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Footer
footer = Label(root, text="© 2024 AI ITS Ontology Viewer | Developed with Python", bg="#1e40af", fg="#e2e8f0",
               font=("Arial", 10))
footer.pack(fill=X, pady=5)

# Run the Mainloop
root.mainloop()
