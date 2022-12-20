import requests

if __name__ == '__main__':
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos"
    args = {'api_key':'ifuzosKzHYyT9T3PMj0ERbgNzpAgHg1rjdB7X61Q'}
    
    response = requests.get(url,params=args)

    if response.status_code == 200:
        
        diccionario = response.json()
        lista = diccionario['latest_photos'][0:20]
        
        length = len(lista)

        imageslist = ""
        for i in range(length):
            imageslist += "<li><img src='"+lista[i]['img_src']+"'></li>"


        def build_web_page(titulo,imagelist):

            mitexto = """<html>
            <head>
            <title>"""+titulo+"""</title>
            </head> 
            <body>
            <h1>Welcome Nasa Rover Image</h1>           
            <ul>
            """+imagelist+"""
            </ul>
            </body>
            </html>"""

            file_html = open("demo.html", "w")
            # Adding the input data to the HTML file
            file_html.write(mitexto)
            # Saving the data into the HTML file
            file_html.close()

        build_web_page("MI NUEVA PAGINA",imageslist)
        
