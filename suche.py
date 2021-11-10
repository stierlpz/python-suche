import time
import webbrowser
print(f'----------------------------------------------------------------')
s=input(f'Was suchst du?:   ')
print(f'----------------------------------------------------------------')
print(f'Suche auf:                                                      ')
gw=input(f'g für Google   w für Wikipedia   c für Wikimedia Commons :   ')
print(f'----------------------------------------------------------------')
if gw=="g":
    print(f'Suche auf Google')
    print(f'----------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'----------------------------------------------------------------')      
    time.sleep(5)
    url='https://www.google.com/search?q='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')
    print(url+s)
    print(f'----------------------------------------------------------------')      
if gw=="G":
    print(f'Suche auf Google')
    print(f'----------------------------------------------------------------')      
    print(f'Suche nach ',s)
    print(f'----------------------------------------------------------------')
    time.sleep(5)
    url='https://www.google.com/search?q='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')
    print(url+s)
    print(f'----------------------------------------------------------------')       

if gw=="w":
    print(f'Suche auf Wikipedia')
    print(f'----------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'----------------------------------------------------------------')
    time.sleep(5)
    url='https://de.wikipedia.org/wiki/'
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')
    print(url+s)
    print(f'----------------------------------------------------------------')      
if gw=="W":
    print(f'Suche auf Wikipedia')
    print(f'----------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'----------------------------------------------------------------')
    time.sleep(5)
    url='https://de.wikipedia.org/wiki/'
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')
    print(url+s)
    print(f'----------------------------------------------------------------')

if gw=="c":
    print(f'Suche auf Wikimedia Commons')
    print(f'----------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'----------------------------------------------------------------')
    time.sleep(5)
    url='https://commons.wikimedia.org/w/index.php?search='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')
    print(url+s)
if gw=="C":
    print(f'Suche auf Wikimedia Commons')
    print(f'Suche nach ',s)
    time.sleep(5)
    url='https://commons.wikimedia.org/w/index.php?search='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')     
    print(url+s)
    print(f'----------------------------------------------------------------')      

print(f'---------------------------------------------------------------')
