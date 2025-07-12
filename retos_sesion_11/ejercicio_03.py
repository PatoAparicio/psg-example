print("Crea un diccionario con la siguiente tupla de especies animales: (('canino', '🐶') , ('felino','🐱') , ('aves',['🐦','🦅']))")
especies = dict((
    ('canino', '🐶'),
    ('felino','🐱'),
    ('aves',['🐦','🦅'])
))
especies.pop('aves')
print("Elimina el valor de la clave 'aves':", especies)
especies['felino'] = '🐈'
print("Modifica el valor de la clave 'felino' por '🐈'", especies)
especies['caninos'] = ['🐶','🐕']
especies.pop('canino')
print("Cambia la clave canino por caninos y su valor por ['🐶','🐕']", especies)