airoma = '''
<!DOCTYPE html>
<html style= 'font-size: 30px; font-family: Futura; background-color: lightblue;' lang= 'en''>
    <head>
        <Link data-default-icon='https://i.pinimg.com/564x/d2/7f/0c/d27f0c1e1342736dacb3174e4d735a55.jpg' rel='icon' size='192x192' href='https://i.pinimg.com/564x/d2/7f/0c/d27f0c1e1342736dacb3174e4d735a55.jpg'>
        <title> Airoma </title>
    </head>

    <body style = 'font-size: 30px; font-family: Helvatica; text-align: center; color: white'>
        Welcome to Airoma
        <br>
        <h1 style= 'font-size: 20px; text-align: left;'> 1. What is Airoma?
        </h1>

        <h6 style= 'font-size: 20px; text-align: right;'> Social Medias: <br>
        Here is our <a style='color: Pink-Purple;' href='https://www.instagram.com/airoma.official/'>Instagram Page</a>
        <br>
        </h6>
        
        <img src= 'https://i.kym-cdn.com/photos/images/newsfeed/001/275/715/010.png' width='374' height='376' alt= 'Confused cat'>
    </body>
</html>
'''
Airoma = open('Airoma.html', 'w')
Airoma.write(airoma)
Airoma.close()