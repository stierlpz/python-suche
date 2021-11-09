
import webbrowser
print(f'------------------------------------')
print(f'Suche auf:                          ')
gw=input(f'g für Google   w fürWikipedia:   ')
print(f'------------------------------------')
if gw=="g":
    print(f'Suche auf Google----------------')
    s=input(f'Was suchst du?:               ')
    print(f'Suche nach ',s,'----------------')
    url='https://www.google.com/search?q='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen-------------')
if gw=="G":
    print(f'Suche auf Google----------------')
    s=input(f'Was suchst du?:               ')
    print(f'Öffne Google--------------------')
    url='https://www.google.com/search?q='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen-------------')
print(f'------------------------------------')    

if gw=="w":
    print(f'Suche auf Wikipedia-------------')
    s=input(f'Was suchst du?:               ')
    print(f'Suche nach ',s,'----------------')
    url='https://de.wikipedia.org/wiki/'
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen-------------')
if gw=="W":
    print(f'Suche auf Wikipedia-------------')
    s=input(f'Was suchst du?:               ')
    print(f'Öffne Wikipedia-----------------')
    url='https://de.wikipedia.org/wiki/'
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen-------------')
print(f'------------------------------------')
