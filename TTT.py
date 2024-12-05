import tkinter as tk

root = tk.Tk()

def grad_nach_kelvin():
    # print(eingabefeld_wert.get())
    grad = int(eingabefeld_wert.get())
    kelvin = grad + 273
    textausgabe = tk.Label(root, text=kelvin, bg="yellow")
    textausgabe.pack()
def logic(buttons[][],x ,y):
    i = 0 
    for i in 3:
        j = 0
        for j in 3:
			if buttons[x][y]=="White":
                if player == 1:
					button.setBackground(Color.YELLOW)
					player = 2
				else:
					button.setBackground(Color.RED)
					player = 1
                
                textlos = tk.Label(root, text="", bg="white")
                textlos.pack

				h = 0
				for (int g = 0 g < 2; g+=1
					if ((buttons[g][h].getBackground() != Color.WHITE)&& (buttons[g][h].getBackground()) == (buttons[g][h + 1].getBackground())&& (buttons[g][h + 1].getBackground()) == (buttons[g][h + 2].getBackground())		//Zeile abchecken
						|| (buttons[h][g].getBackground() != Color.WHITE)&& (buttons[h][g].getBackground()) == (buttons[h + 1][g].getBackground())&& (buttons[h + 1][g].getBackground()) == (buttons[h + 2][g].getBackground())		//Spalte abchecken
						|| (buttons[1][1].getBackground() != Color.WHITE)&& (buttons[0][0].getBackground()) == (buttons[1][1].getBackground())&& (buttons[1][1].getBackground()) == (buttons[2][2].getBackground())					//Diagonale1 abchecken
						|| (buttons[1][1].getBackground() != Color.WHITE)&& (buttons[0][2].getBackground()) == (buttons[1][1].getBackground())&& (buttons[1][1].getBackground()) == (buttons[2][0].getBackground())) 				//Diagonale2 abchecken
						if (player == true) 
							textfield_output.setText("Spieler 1 hat gewonen!!!")
							for (int x = 0 x < 3; x=+1) 
								for (int y = 0 y < 3; y=+1) 
									buttons[x][y].setEnabled(false)
								
							
						 else if (player == false) 
							textfield_output.setText("Spieler 2 hat gewonen!!!")
							for (int x = 0 x < 3; x=+1) 
								for (int y = 0 y < 3; y=+1) 
									buttons[x][y].setEnabled(false)
                        g+=1
			j=+1			
        i=+1		
					 else: 
                        textausgabe = tk.Label(root, text="Das darfst du nicht!!!", bg="white")
                        textausgabe.pack

eingabefeld_wert=tk.StringVar()
eingabefeld=tk.Entry(root, textvariable=eingabefeld_wert)
eingabefeld.pack()
x=0
y=0
for x in 3:
    for y in 3:
        schaltf1 = tk.Button(root, bg="white", command=logic([x][y],x,y))
        schaltf1.pack()
        y=+1
    x=+1

root.mainloop()