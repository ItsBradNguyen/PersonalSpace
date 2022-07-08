airoma = '''
<!DOCTYPE html>
<html style= 'font-size: 30px; font-family: Futura; background-color: lightblue;' lang = 'en' dark = 'true'">
<head>
<Link data-default-icon='https://i.pinimg.com/564x/d2/7f/0c/d27f0c1e1342736dacb3174e4d735a55.jpg' rel='icon' size='192x192' href='https://i.pinimg.com/564x/d2/7f/0c/d27f0c1e1342736dacb3174e4d735a55.jpg'>
<title> Airoma </title>
</head>
<body style = "font-size: 15px; font-family: Helvatica;">
Welcome to Airoma
<img src= 'https://i.kym-cdn.com/photos/images/newsfeed/001/275/715/010.png' width='374' height='376' alt= 'Confused cat'>
</body>
</html>
'''
Airoma = open('Airoma.html', 'w')
Airoma.write(airoma)
Airoma.close()