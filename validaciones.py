from wtforms import Form
from wtforms import StringField,IntegerField,DateField,EmailField, TextAreaField,FileField

from wtforms import validators

def NoVacio(form,field):
    if len(str(field.data)) == 0:
        raise validators.ValidationError('El campo no tiene datos')
def NoNumeros(form,field):
    if len(field.data) != 0:
        for c in str(field.data):
            if c.isalpha() != True and c != ' ' or c in [0,1,2,3,4,5,6,7,8,9]:
                raise validators.ValidationError('El campo no debe contener números')
            
def NoEspacios(form,field):
    if len(field.data) != 0:
        if ' ' in str(field.data):
            raise validators.ValidationError('El campo no debe contener números ni espacios')
def Numeros(form,field):
    if len(field.data) != 0:
        if ' ' in str(field.data) or str(field.data).isnumeric() == False:
            raise validators.ValidationError('El campo debe contener solo números y sin espacios')



class productos(Form):
    id_producto = IntegerField('id_producto')
    nombre = StringField('Nombre',[validators.DataRequired(message='Dato requerido')])

    cantidad = IntegerField('Cantidad (Existencias)',[validators.DataRequired(message='Dato requerido'),validators.number_range(min=1,message='El campo no puede ser 0')])
    cantidad_min = IntegerField('Cantidad Minima',[validators.DataRequired(message='Dato requerido'),validators.number_range(min=1,message='El campo no puede ser 0')])
    precio_U = IntegerField('Precio por Unidad',[validators.DataRequired(message='Dato requerido'),validators.number_range(min=1,message='El campo no puede ser 0')])
    precio_M = IntegerField('Precio Mayoreo',[validators.DataRequired(message='Dato requerido'),validators.number_range(min=1,message='El campo no puede ser 0')])
    img = FileField('Imagen')
    proceso = TextAreaField('Proceso',[validators.DataRequired(message='Dato requerido')])
    descripcion = TextAreaField('Descripcion',[validators.DataRequired(message='Dato requerido')])


class insumos(Form):
    nombre = StringField('Mombre',[validators.length(min=4,max=32,message='El nombre debe tener entre 8 y 32 caracteres')])
    cantidad = IntegerField('Cantidad',[validators.number_range(min=1,message='El valor no puede ser menor a 1')])
    cantidad_min = IntegerField('Cantidad Mínima',[validators.number_range(min=1,message='El valor no puede ser menor a 1')])
    caducidad = DateField('Fechas de Caducidad',[validators.optional()])



class UserForm(Form):
    id = IntegerField('id',
        [validators.number_range
        (min=1,max=100,message='valor no valido')])
    nombre = StringField('Nombre',[NoNumeros,NoVacio])

    apaterno = StringField('apaterno',[NoVacio,NoNumeros])
    
    email = EmailField('correo',[validators.Email(message='Dame un correo valido'),NoVacio,NoEspacios])
    
class Profes(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre',[NoNumeros,NoVacio])
    
    apaterno = StringField('apaterno',[NoVacio,NoNumeros])
    
    email = EmailField('email',[validators.Email(message='Dame un correo valido'),NoVacio,NoEspacios])
    
    sueldo = IntegerField('sueldo',
        [
        validators.DataRequired(message='Dato requerido'),
        validators.number_range(min=200,max=100000,message='Valor no valido')])
    telefono = StringField('telefono',
        [
        validators.DataRequired(message='Dato requerido'),
        validators.length(min=10,max=10,message='Ingrese 10 numeros'),Numeros])