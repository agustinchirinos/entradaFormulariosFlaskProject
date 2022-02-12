from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms.validators import DataRequired, Length, ValidationError


class FormWTF(FlaskForm):
    nombre = StringField(label="Nombre",validators=[
        DataRequired(message="El campo nombre es obligatorio"),
        Length(min=5,max=20,message="El campo nombre debe ser entre 5 y 20 caracteres")
    ])
    edad = IntegerField(label="Edad")

    imagen = FileField(label="Imagen", validators=[
        FileRequired(message="El campo imagen es obligatorio"),
        FileAllowed(['jpg','png'], message="Solo jpg y png")
    ])

    submit = SubmitField(label="Enviar")

    def validate_edad(form,field):
        if field.data<0:
            raise ValidationError("Error la edad no puede ser inferior a cero")

    def validate_imagen(form,field):
        max_length = 1024
        if len(field.data.read()) > max_length:
            raise ValidationError(f"El fichero no puede ser superior a {max_length}")