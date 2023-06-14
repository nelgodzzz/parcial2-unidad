temas_dificiles = [
    {"tema": "Normalizacion de base de datos", "motivo": "es por que cuando nos da clase no c mira bien la pantalla se apaga el microfono a media clase y cuando ya se da cuenta ya va adelatado en el tema es muy dificil recordar cada paso si no hemos visto los primeros pasos bien "},
    {"tema": "consola de gitbash,commits y repositorios", "motivo": "Hay demasiada infomacion para recordar y los mismo problemas de camara y microfono."},
    {"tema": "listas ", "motivo": "Dificil de entender cuando no c ve bien la pantalla y el audio mal "}
]

print("Temas que me han costado durante el año:")
for tema in temas_dificiles:
    print("- {} (Motivo: {})".format(tema["tema"], tema["motivo"]))
