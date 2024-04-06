## La aplicación crea un index.html por medio del uso de una API con Python

Al ejectar main.py desde el terminal, se ejecuta la siguiente función:

>       crear_html(html_card(request_get(url)))


* **request_get(url)** : Crea un objeto JSON llamado photos, el cual contiene todas las aves de la API

* **html_card()** : Recibe el objeto photos y crea diferentes cards (formato Bootstrap), adjuntándolas en una variable llamda card

* **crear_html()** : Recibe las cards creadas y las interpola en una plantilla html y crea un archivo index.html listo para ser abierto en el navegador.


