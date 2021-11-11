<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Index</title>
</head>

<body>
<p><a href="https://github.com/stierlpz/python-suche-wikipedia-und-google" title="https://github.com/stierlpz/python-suche-wikipedia-und-google" target="new">Github</a>
</p>
<p>&nbsp;</p>
<p>import time<br>
  import webbrowser<br>
  print(f'---------------------------------------------------------------------------------------') <br>
  print(f'Suche auf: ')<br>
  print(f'c für Wikmeidia Comans')<br>
  print(f'g für Google')<br>
  print(f'm für Goolge Maps')<br>
  print(f't für Google Taschenrechner')<br>
  print(f'y für Youtube')<br>
  gw=input(f'Wo suchst Du? :   ')<br>
  print(f'---------------------------------------------------------------------------------------')</p>
<p>if gw==&quot;g&quot;:<br>
  print(f'Suche auf Google')<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  s=input(f'Was suchst du?:   ')<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  print(f'Suche nach ',s)<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  time.sleep(0)<br>
  url='https://www.google.com/search?q='<br>
  webbrowser.open(url+s)<br>
  print(f'Suche abgeschlossen')<br>
  print(url+s)<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  if gw==&quot;G&quot;:<br>
  print(f'Suche auf Google')<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  s=input(f'Was suchst du?:   ')<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  print(f'Suche nach ',s)<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  time.sleep(0)<br>
  url='https://www.google.com/search?q='<br>
  webbrowser.open(url+s)<br>
  print(f'Suche abgeschlossen')<br>
  print(url+s)<br>
  print(f'-----------------------------------------------------------------------------------') </p>
<p>if gw==&quot;w&quot;:<br>
  print(f'Suche auf Wikipedia')<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  s=input(f'Was suchst du?:   ')<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  print(f'Suche nach ',s)<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  time.sleep(0)<br>
  url='https://de.wikipedia.org/wiki/'<br>
  webbrowser.open(url+s)<br>
  print(f'Suche abgeschlossen')<br>
  print(url+s)<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  if gw==&quot;W&quot;:<br>
  print(f'Suche auf Wikipedia')<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  s=input(f'Was suchst du?:   ')<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  print(f'Suche nach ',s)<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  time.sleep(0)<br>
  url='https://de.wikipedia.org/wiki/'<br>
  webbrowser.open(url+s)<br>
  print(f'Suche abgeschlossen')<br>
  print(url+s)<br>
  print(f'-----------------------------------------------------------------------------------') </p>
<p>if gw==&quot;c&quot;:<br>
  print(f'Suche auf Wikimedia Commons')<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  s=input(f'Was suchst du?:   ')<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  print(f'Suche nach ',s)<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  time.sleep(0)<br>
  url='https://commons.wikimedia.org/w/index.php?search='<br>
  webbrowser.open(url+s)<br>
  print(f'Suche abgeschlossen')<br>
  print(url+s)<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  if gw==&quot;C&quot;:<br>
  print(f'Suche auf Wikimedia Commons')<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  s=input(f'Was suchst du?:   ')<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  print(f'Suche nach ',s)<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  time.sleep(0)<br>
  url='https://commons.wikimedia.org/w/index.php?search='<br>
  webbrowser.open(url+s)<br>
  print(f'Suche abgeschlossen') <br>
  print(url+s)<br>
  print(f'-----------------------------------------------------------------------------------')</p>
<p>if gw==&quot;t&quot;:<br>
  print(f'Öffne den Taschenrechner von Google')<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  time.sleep(0)<br>
  url='https://www.google.com/search?q=Taschenrechner'<br>
  webbrowser.open(url)<br>
  print(f'Taschenrechner geöffnet')<br>
  print(url)<br>
  print(f'-----------------------------------------------------------------------------------')</p>
<p>if gw==&quot;T&quot;:<br>
  print(f'Öffne den Taschenrechner von Google')<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  time.sleep(0)<br>
  url='https://www.google.com/search?q=Taschenrechner'<br>
  webbrowser.open(url)<br>
  print(f'Taschenrechner geöffnet')<br>
  print(url)<br>
  print(f'-----------------------------------------------------------------------------------')<br>
</p>
<p>if gw==&quot;m&quot;:<br>
  print(f'Suche auf Google Maps')<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  s=input(f'Was suchst du?:   ')<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  print(f'Suche nach ',s)<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  time.sleep(0)<br>
  url='https://www.google.com/maps/search/'<br>
  webbrowser.open(url+s)<br>
  print(f'Suche abgeschlossen') <br>
  print(url+s)<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  if gw==&quot;M&quot;:<br>
  print(f'Suche auf Google Maps')<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  s=input(f'Was suchst du?:   ')<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  print(f'Suche nach ',s)<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  time.sleep(0)<br>
  url='https://www.google.com/maps/search/'<br>
  webbrowser.open(url+s)<br>
  print(f'Suche abgeschlossen') <br>
  print(url+s)<br>
  print(f'-----------------------------------------------------------------------------------')</p>
<p>if gw==&quot;y&quot;:<br>
  print(f'Suche auf Youtube')<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  s=input(f'Was suchst du?:   ')<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  print(f'Suche nach ',s)<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  time.sleep(0)<br>
  url='https://www.youtube.com/results?search_query='<br>
  webbrowser.open(url+s)<br>
  print(f'Suche abgeschlossen') <br>
  print(url+s)<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  if gw==&quot;Y&quot;:<br>
  print(f'Suche auf Youtube')<br>
  print(f'-----------------------------------------------------------------------------------') <br>
  s=input(f'Was suchst du?:   ')<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  print(f'Suche nach ',s)<br>
  print(f'-----------------------------------------------------------------------------------')<br>
  time.sleep(0)<br>
  url='https://www.youtube.com/results?search_query='<br>
  webbrowser.open(url+s)<br>
  print(f'Suche abgeschlossen') <br>
  print(url+s)<br>
  print(f'-----------------------------------------------------------------------------------') <br>
</p>
<p> <br>
  <br>
  <br>
</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p></p>
</body>
</html>