"""
7c12ef1535bb440d9e766d486366bb07
"""

import requests

text ='Identificar los objetivos de negocio: Es importante entender los objetivos clave de la organización y cómo la IA puede ayudar a alcanzarlos. Esto puede incluir mejorar la eficiencia operativa, aumentar la rentabilidad o mejorar la experiencia del cliente. Identificar los datos y recursos disponibles: Es esencial tener acceso a los datos y recursos necesarios para implementar una estrategia de IA efectiva. Esto puede incluir datos internos, como registros.'


response = requests.get(f"http://api.voicerss.org/?key=7c12ef1535bb440d9e766d486366bb07&hl=es-es&src={text}&c=mp3")

file =open("example.mp3", "wb")
file.write(response.content)
file.close()
