dag = input('Kies een dag ')

if dag == 'maandag':
    dagen = 1
if dag == 'dinsdag':
    dagen = 2
if dag == 'woensdag':
    dagen = 3
if dag == 'donderdag':
    dagen = 4
if dag == 'vrijdag':
    dagen = 5
if dag == 'zaterdag':
    dagen = 6
if dag == 'zondag':
    dagen = 7
dagNr = 1
while dagNr <= dagen:
    if dagNr == 1:
        naam = 'maandag'
    if dagNr == 2:
        naam = 'dinsdag'
    if dagNr == 3:
        naam = 'woensdag'
    if dagNr == 4:
        naam = 'donderdag'
    if dagNr == 5:
        naam = 'vrijdag'
    if dagNr == 6:
        naam = 'zaterdag'
    if dagNr == 7:
        naam = 'zondag'
    
    print(naam)
    dagNr = dagNr + 1