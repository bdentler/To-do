# To-do
Python version of a to do script. Combine with Geektool, Dropbox, and Quicksilver on a Mac for a handy way 
to keep up with the things you need to do.

In its basic form you can type commands at the command line and the script adds numbers and tasks (to do items) to a text
file. Optionally you can insert, delete or even add a date that the task should be added to the to do text file. 

For example: 

$ todo.py a "Thing to do"
This command will number "Thing to do" as the next task number and add it to the bottom of the to do text file.

$ todo.py d 5
Will delete task #5 from the to do text file

By itself this isn't really all that great but if you combine it with the following it becomes a convenient tool
for keeping track of what you need to do:

Geektool - to display the to do text file on your desktop so you can always see it
Dropbox or some other cloud drive - to sync your tasks across devices
Quicksilver - create a to do action with a simple apple script to manage your list by simply invoking Quicksilver
