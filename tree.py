from tkinter import * 
from tkinter import ttk


app = Tk()
app.title("Tree View")
app.iconbitmap('icone_python_green.ico')
app.geometry("500x800")

# Style section
style = ttk.Style()

# Pick a Theme

lis_themes = ['clam', 'default', 'alt', 'vista']
style.theme_use('clam')

# Configure our Treeview color
style.configure('Treeview', 
	background='#D3D3D3', 
	foreground='black', 
	rowheight=35,
	fieldbackground = '#D3D3D3',
)
style.map('Treeview', 
	background=[('selected', 'blue')]
)

tree_frame = Frame(app)
tree_frame.pack(pady=20)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)


my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

tree_scroll.config(command=my_tree.yview)

my_tree['column'] = ('Name', 'ID', 'Favorite Pizza')

my_tree.column('#0', width=0, minwidth=0)
my_tree.column('Name', anchor='w',width=140)
my_tree.column('ID', anchor='center', width=100)
my_tree.column('Favorite Pizza', anchor='w', width=140)

my_tree.heading('#0', text='Label', anchor='w')
my_tree.heading('Name', text='Name', anchor='w')
my_tree.heading('ID', text='ID', anchor='center')
my_tree.heading('Favorite Pizza', text='Favorite Pizza', anchor='w')

data = [
	['Akram', 1, 'Peporoni'],
	['Yasser', 2, 'Hot'],
	['Sami', 2, 'Moutard'],
	['Salwa', 3, 'Flewid'],
	['Akram', 1, 'Peporoni'],
	['Yasser', 2, 'Hot'],
	['Sami', 2, 'Moutard'],
	['Salwa', 3, 'Flewid'],
	['Akram', 1, 'Peporoni'],
	['Yasser', 2, 'Hot'],
	['Sami', 2, 'Moutard'],
	['Akram', 1, 'Peporoni'],
	['Yasser', 2, 'Hot'],
	['Sami', 2, 'Moutard'],
	['Salwa', 3, 'Flewid'],
	['Akram', 1, 'Peporoni'],
	['Yasser', 2, 'Hot'],
	['Sami', 2, 'Moutard'],
	['Salwa', 3, 'Flewid'],
	['Akram', 1, 'Peporoni'],
	['Yasser', 2, 'Hot'],
	['Sami', 2, 'Moutard'],
	['Akram', 1, 'Peporoni'],
	['Yasser', 2, 'Hot'],
	['Sami', 2, 'Moutard'],
	['Salwa', 3, 'Flewid'],
	['Akram', 1, 'Peporoni'],
	['Yasser', 2, 'Hot'],
	['Sami', 2, 'Moutard'],
	['Salwa', 3, 'Flewid'],
	['Akram', 1, 'Peporoni'],
	['Yasser', 2, 'Hot'],
	['Sami', 2, 'Moutard'],
	['Salwa', 3, 'Flewid'],
]

# Create Striped row tags
my_tree.tag_configure('oddrow', background='white')
my_tree.tag_configure('evenrow', background='lightblue')

count = 0
for x in data:
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text='', 
			values=(x[0], x[1], x[2]), tags=('evenrow', ))
	else:
		my_tree.insert(parent='', index='end', iid=count, text='', 
			values=(x[0], x[1], x[2]), tags=('oddrow', ))
	count += 1

my_tree.pack()

add_frame = Frame(app)
add_frame.pack(pady=20)

nl = Label(add_frame, text='Name')
nl.grid(row=0, column=0)

il = Label(add_frame, text='ID')
il.grid(row=0, column=1)

tl = Label(add_frame, text='Topping')
tl.grid(row=0, column=2)


name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

lis_box = [name_box, id_box, topping_box]
def add_record():
	global count
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text='', 
			values=(lis_box[0].get(), lis_box[1].get(), lis_box[2].get()), 
			tags=('evenrow', ))
	else:
		my_tree.insert(parent='', index='end', iid=count, text='', 
			values=(lis_box[0].get(), lis_box[1].get(), lis_box[2].get()), 
			tags=('oddrow', ))
	count += 1
	for x in lis_box:
		x.delete(0, 'end')

def remove_all():
	for record in my_tree.get_children():
		my_tree.delete(record)

def remove_one():
	x = my_tree.selection()[0]
	my_tree.delete(x)

def remove_many():
	x = my_tree.selection()
	for i in x:
		my_tree.delete(i)

def select_record():
	for x in lis_box:
		x.delete(0, 'end')

	# Grab record number 
	selected = my_tree.focus()
	values = my_tree.item(selected, 'values')
	for x in range(len(lis_box)):
		lis_box[x].insert(0, values[x])


def update_record():
	selected = my_tree.focus()
	my_tree.item(selected, text='', values=[x.get() for x in lis_box])
	for x in lis_box:
		x.delete(0, END)


def clicker(e):
	select_record()

def up():
	rows = my_tree.selection()
	for row in rows:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

def down():
	rows = my_tree.selection()
	for row in rows:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)


add_record = Button(app, text='Add record', command=add_record)
add_record.pack(pady=(10, 5))

# Remove all
remove_all = Button(app, text='Remove All Records', command=remove_all)
remove_all.pack(pady=(0,5))

# Remove one
remove_one = Button(app, text='Remove One Selected', command=remove_one)
remove_one.pack(pady=(0,5))

remove_multiple = Button(app, text='Remove Multiple', command=remove_many)
remove_multiple.pack(pady=(0,5))

select_record_button = Button(app, text='Select Record', command=select_record)
select_record_button.pack(pady=(0,5))

update_record = Button(app, text='Save Record', command=update_record)
update_record.pack(pady=(0,5))

# Move row up
move_up = Button(app, text="Move Up", command=up)
move_up.pack(pady=10)

# Move down the row

temp_label = Label(app, text='')
temp_label.pack(pady=20)

#binding
# my_tree.bind("<Double-1>", clicker)
my_tree.bind("<ButtonRelease-1>", clicker)


app.mainloop()