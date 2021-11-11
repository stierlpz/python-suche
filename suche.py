import time
import webbrowser
print(f'---------------------------------------------------------------------------------------')  
print(f'Suche auf: ')
print(f'c für Wikmeidia Comans')
print(f'g für Google')
print(f'm für Goolge Maps')
print(f't für Google Taschenrechner')
print(f'y für Youtube')
gw=input(f'Wo suchst Du? :   ')
print(f'---------------------------------------------------------------------------------------')

if gw=="g":
    print(f'Suche auf Google')
    print(f'-----------------------------------------------------------------------------------')  
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')  
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')      
    time.sleep(0)
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
    time.sleep(0)
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
    time.sleep(0)
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
    time.sleep(0)
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
    time.sleep(0)
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
    time.sleep(0)
    url='https://commons.wikimedia.org/w/index.php?search='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')     
    print(url+s)
    print(f'-----------------------------------------------------------------------------------')

if gw=="t":
    print(f'Öffne den Taschenrechner von Google')
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(0)
    url='https://www.google.com/search?q=Taschenrechner'
    webbrowser.open(url)
    print(f'Taschenrechner geöffnet')
    print(url)
    print(f'-----------------------------------------------------------------------------------')

if gw=="T":
    print(f'Öffne den Taschenrechner von Google')
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(0)
    url='https://www.google.com/search?q=Taschenrechner'
    webbrowser.open(url)
    print(f'Taschenrechner geöffnet')
    print(url)
    print(f'-----------------------------------------------------------------------------------')


if gw=="m":
    print(f'Suche auf Google Maps')
    print(f'-----------------------------------------------------------------------------------')  
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(0)
    url='https://www.google.com/maps/search/'
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')     
    print(url+s)
    print(f'-----------------------------------------------------------------------------------')
if gw=="M":
    print(f'Suche auf Google Maps')
    print(f'-----------------------------------------------------------------------------------')  
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(0)
    url='https://www.google.com/maps/search/'
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')     
    print(url+s)
    print(f'-----------------------------------------------------------------------------------')

if gw=="y":
    print(f'Suche auf Youtube')
    print(f'-----------------------------------------------------------------------------------')  
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(0)
    url='https://www.youtube.com/results?search_query='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')     
    print(url+s)
    print(f'-----------------------------------------------------------------------------------')
if gw=="Y":
    print(f'Suche auf Youtube')
    print(f'-----------------------------------------------------------------------------------')  
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(0)
    url='https://www.youtube.com/results?search_query='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')     
    print(url+s)
    print(f'-----------------------------------------------------------------------------------')    


    
    
    







