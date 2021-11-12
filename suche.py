import time
import webbrowser
print(f'---------------------------------------------------------------------------------------')  
print(f'Suche auf: ')
print(f'b für Google Bilder')
print(f'c für Wikmeidia Comans')
print(f'g für Google')
print(f'm für Goolge Maps')
print(f's für Google Shopping')
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


if gw=="m":
    print(f'Suche auf Google Maps')
    print(f'-----------------------------------------------------------------------------------')  
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(5)
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
    time.sleep(5)
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
    time.sleep(5)
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
    time.sleep(5)
    url='https://www.youtube.com/results?search_query='
    webbrowser.open(url+s)
    print(f'Suche abgeschlossen')     
    print(url+s)
    print(f'-----------------------------------------------------------------------------------')

if gw=="b":
    print(f'Suche auf Google Bilder')
    print(f'-----------------------------------------------------------------------------------')  
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(5)
    url='https://www.google.de/search?q='
    url2='&hl=de&authuser=0&tbm=isch&sxsrf=AOaemvIy0b1tErToWnyfge9YuociFQM9lA%3A1636633673968&source=hp&biw=1366&bih=625&ei=SQyNYcTGN8H67_UPvua4yAs&iflsig=ALs-wAMAAAAAYY0aWSs5aCcdJj6xqgZpqcFw4KP89eKh&oq=5&gs_lcp=CgNpbWcQAzIHCCMQ7wMQJzIHCCMQ7wMQJzIFCAAQgAQyCAgAEIAEELEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCxAxCDATIFCAAQgAQyCAgAEIAEELEDUABYAGD2A2gAcAB4AIABPYgBPZIBATGYAQCgAQGqAQtnd3Mtd2l6LWltZw&sclient=img&ved=0ahUKEwiEj4vGp5D0AhVB_bsIHT4zDrkQ4dUDCAY&uact=5'
    webbrowser.open(url+s+url2)
    print(f'Suche abgeschlossen')     
    print(url+s+url2)
    print(f'-----------------------------------------------------------------------------------')      
if gw=="B":
    print(f'Suche auf Google Bilder')
    print(f'-----------------------------------------------------------------------------------')  
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(5)
    url='https://www.google.de/search?q='
    url2='&hl=de&authuser=0&tbm=isch&sxsrf=AOaemvIy0b1tErToWnyfge9YuociFQM9lA%3A1636633673968&source=hp&biw=1366&bih=625&ei=SQyNYcTGN8H67_UPvua4yAs&iflsig=ALs-wAMAAAAAYY0aWSs5aCcdJj6xqgZpqcFw4KP89eKh&oq=5&gs_lcp=CgNpbWcQAzIHCCMQ7wMQJzIHCCMQ7wMQJzIFCAAQgAQyCAgAEIAEELEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCxAxCDATIFCAAQgAQyCAgAEIAEELEDUABYAGD2A2gAcAB4AIABPYgBPZIBATGYAQCgAQGqAQtnd3Mtd2l6LWltZw&sclient=img&ved=0ahUKEwiEj4vGp5D0AhVB_bsIHT4zDrkQ4dUDCAY&uact=5'
    webbrowser.open(url+s+url2)
    print(f'Suche abgeschlossen')     
    print(url+s+url2)
    print(f'-----------------------------------------------------------------------------------')

if gw=="s":
    print(f'Suche auf Google Shopping')
    print(f'-----------------------------------------------------------------------------------')  
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(5)
    url='https://www.google.de/search?q='
    url2='&source=lmns&tbm=shop&authuser=0&bih=625&biw=1366&hl=de&sa=X&ved=2ahUKEwi7n5nwqJD0AhUbgv0HHZv8DzsQ_AUoAHoECAEQBw'
    webbrowser.open(url+s+url2)
    print(f'Suche abgeschlossen')     
    print(url+s+url2)
    print(f'-----------------------------------------------------------------------------------')      
if gw=="S":
    print(f'Suche auf Google Shopping')
    print(f'-----------------------------------------------------------------------------------')  
    s=input(f'Was suchst du?:   ')
    print(f'-----------------------------------------------------------------------------------')
    print(f'Suche nach ',s)
    print(f'-----------------------------------------------------------------------------------')
    time.sleep(5)
    url='https://www.google.de/search?q='
    url2='&source=lmns&tbm=shop&authuser=0&bih=625&biw=1366&hl=de&sa=X&ved=2ahUKEwi7n5nwqJD0AhUbgv0HHZv8DzsQ_AUoAHoECAEQBw'
    webbrowser.open(url+s+url2)
    print(f'Suche abgeschlossen')     
    print(url+s+url2)
    print(f'-----------------------------------------------------------------------------------')      





