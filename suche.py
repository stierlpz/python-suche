import time
import webbrowser
print(f'---------------------------------------------------------------------------------------')  
print(f'Suche auf: ')
gw=input(f'g für Google   t für Taschenrechner   w für Wikipedia   c für Wikimedia Commons :   ')
print(f'---------------------------------------------------------------------------------------')
if gw=="g":
    print(f'Suche auf Google')
    print(f'-----------------------------------------------------------------------------------')  
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')  
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')      
    time.sleep(5)
    url='https://www.google.com/search?q='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')
    print(url+s)
    print(f'-----------------------------------------------------------------------------------')      
if gw=="G":
    print(f'Suche auf Google')
    print(f'-----------------------------------------------------------------------------------')
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')  
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')  
    time.sleep(5)
    url='https://www.google.com/search?q='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')
    print(url+s)
    print(f'-----------------------------------------------------------------------------------')       

if gw=="w":
    print(f'Suche auf Wikipedia')
    print(f'-----------------------------------------------------------------------------------')
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')  
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')  
    time.sleep(5)
    url='https://de.wikipedia.org/wiki/'
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')
    print(url+s)
    print(f'-----------------------------------------------------------------------------------')  
if gw=="W":
    print(f'Suche auf Wikipedia')
    print(f'-----------------------------------------------------------------------------------')
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')  
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')  
    time.sleep(5)
    url='https://de.wikipedia.org/wiki/'
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')
    print(url+s)
    print(f'-----------------------------------------------------------------------------------')  

if gw=="c":
    print(f'Suche auf Wikimedia Commons')
    print(f'-----------------------------------------------------------------------------------')
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')  
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')  
    time.sleep(5)
    url='https://commons.wikimedia.org/w/index.php?search='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')
    print(url+s)
    print(f'-----------------------------------------------------------------------------------')  
if gw=="C":
    print(f'Suche auf Wikimedia Commons')
    print(f'-----------------------------------------------------------------------------------')  
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(5)
    url='https://commons.wikimedia.org/w/index.php?search='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')     
    print(url+s)
    print(f'-----------------------------------------------------------------------------------')

if gw=="t":
    print(f'Öffne den Taschenrechner von Google')
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(5)
    url='https://www.google.com/search?q=Taschenrechner'
    webbrowser.open(url)
    print(f'Taschenrechner geöffnet')
    print(url)
    print(f'-----------------------------------------------------------------------------------')

if gw=="T":
    print(f'Öffne den Taschenrechner von Google')
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(5)
    url='https://www.google.com/search?q=Taschenrechner'
    webbrowser.open(url)
    print(f'Taschenrechner geöffnet')
    print(url)
    print(f'-----------------------------------------------------------------------------------')
        
    
    




