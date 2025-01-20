# program the will draw a "+-------+" box a set ammount of times

def the_box(title):
    top_line = "+" + (len(title))*"-" + "+"
    text_line = "|" + title + "|"
    bottom_line = top_line
    return top_line + "\n" + (text_line) + "\n" + bottom_line

print(the_box("Hello"))