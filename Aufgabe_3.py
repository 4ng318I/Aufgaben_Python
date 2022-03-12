'''Schreiben Sie eine Funktion, die einen Punktestand daraufhin prüft, ob dieser einen neuen Highscore darstellt. Das trifft dann zu, wenn die aktuelle Punktzahl größer als der momentane Highscore ist. In den Fall soll eine Meldung auf der Konsole ausgegeben werden. Als Ausgangbassis dienen folgende Anweisungen:

points = 1234
highscore = 1000
if points > highscore:
    print("Congratulation, this is a new highscore")
'''

points = 1234
highscore = 1000


def new_record(points, highscore):
    if points > highscore:
        print("Congratulation, this is a new highscore")
    else:
        print("You don´t reached a new highscore!!")

new_record(1480, 1490)