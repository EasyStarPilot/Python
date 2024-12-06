import tkinter as tk

root = tk.Tk()
root.geometry("300x200")


# print(eingabefeld_wert.get())
# textausgabe = tk.Label(root, text=kelvin, bg="yellow")
# textausgabe.pack()''
def logic(x ,y):
buttonscoulor[0][0]="white"
for x in range(3):
	for y in range(3):
		buttonscoulor[x][y]="white"
i=0
while i in range(0,3):
	j = 0
	while j in 3:
		if buttonscoulor[x][y]=="white":
			if player == 1:
				buttonscoulor[x][y]="yellow"
				player = 2
			else:
				buttonscoulor[x][y]="red"
				player = 1
			
			textlos = tk.Label(root, text="", bg="white")
			textlos.pack

			h = 0
			g=0
			while g in range(3):
				if (([g][h] != "white")& (buttonscoulor[g][h]) == (buttonscoulor[g][h + 1])& (buttonscoulor[g][h + 1]) == (buttonscoulor[g][h + 2])						#Zeile abchecken
				| (buttonscoulor[h][g] != "white")& (buttonscoulor[h][g]) == (buttonscoulor[h + 1][g])& (buttonscoulor[h + 1][g]) == (buttonscoulor[h + 2][g])			#Spalte abchecken
				| (buttonscoulor[1][1] != "white")& (buttonscoulor[0][0]) == (buttonscoulor[1][1])& (buttonscoulor[1][1]) == (buttonscoulor[2][2])						#Diagonale1 abchecken
				| (buttonscoulor[1][1] != "white")& (buttonscoulor[0][2]) == (buttonscoulor[1][1])& (buttonscoulor[1][1]) == (buttonscoulor[2][0])):					#Diagonale2 abchecken
					if player == 1:
						P1won = tk.Label(root, text="Spieler 1 hat gewonnen!", bg="yellow")
						P1won.pack
					else: 
						P2won = tk.Label(root,  text="Spieler 2 hat gewonnen!", bg="red")
						P2won.pack
		j=+1			
	i=+1		
	if buttonscoulor[x][y]!="white": 
		textausgabe = tk.Label(root, text="Das darfst du nicht!!!", bg="green")
		textausgabe.pack

schaltf0 = tk.Button(root, bg="white", command=logic(0,0))
schaltf1 = tk.Button(root, bg="white", command=logic(0,1))
schaltf2 = tk.Button(root, bg="white", command=logic(0,2))
schaltf3 = tk.Button(root, bg="white", command=logic(1,0))
schaltf4 = tk.Button(root, bg="white", command=logic(1,1))
schaltf5 = tk.Button(root, bg="white", command=logic(1,2))
schaltf6 = tk.Button(root, bg="white", command=logic(2,0))
schaltf7 = tk.Button(root, bg="white", command=logic(2,1))
schaltf8 = tk.Button(root, bg="white", command=logic(2,2))
schaltf0.pack()
schaltf1.pack()
schaltf2.pack()
schaltf3.pack()
schaltf4.pack()
schaltf5.pack()
schaltf6.pack()
schaltf7.pack()
schaltf8.pack()

root.mainloop()