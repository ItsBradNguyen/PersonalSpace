portfolio= '''
<!DOCTYPE html>
<html style='background-color:Navy;font-family:Monolisa;' lang='en-US'>
    <head>
        <title> Brad Nguyen - Portfolio </title>
        <Link data-default-icon=''>
    </head>

    <body>
        <img style='height:500px;width:500px;float:left' src=' https://media-exp2.licdn.com/dms/image/C5603AQEBKlARw0IdQw/profile-displayphoto-shrink_400_400/0/1620145788993?e=1662595200&v=beta&t=VNoVcPEYgusQ5tdbxJZAP2GGziQdTRAgRxbqBfyxJ9o'> 
        <h1 style='font-size:100px;color:#00dcdc;text-align:center;'> Hello </h1>
        <p style='font-size:50px;color:#D9B48FFF;text-align:center;'> I'm Nguyen </p>

    </body>
</html>
'''

Portfolio = open('portfolio.html','w')
Portfolio.write(portfolio)
Portfolio.close()