import streamlit as st
from docx import Document
from io import BytesIO
import datetime
def rellenar_kyc(datos_cliente, plantilla_path):
    doc = Document(plantilla_path)
    for par in doc.paragraphs:
        for key, value in datos_cliente.items():
            par.text = par.text.replace(f"{{{{{key}}}}}", str(value))
    output = BytesIO()
    doc.save(output)
    return output

# Interfaz Streamlit
st.title("Formulario KYC")

# Selección del tipo de cliente
tipo_cliente = st.radio("Selecciona el tipo de cliente", ["Persona Física", "Persona Jurídica"])

datos_cliente = {}

if tipo_cliente == "Persona Física":
    st.header("Datos Personales")
    datos_cliente["nombre_apellidos"] = st.text_input("Nombre y Apellidos")
    datos_cliente["tipo_documento"] = st.selectbox("Tipo de Documento", ["DNI", "Pasaporte", "NIE"])
    datos_cliente["numero_documento"] = st.text_input("Número de Documento")
    datos_cliente["fecha_nacimiento"] = st.date_input("Fecha de Nacimiento", min_value=datetime.date(1950, 1, 1), max_value=datetime.date(2050, 12, 31))
    datos_cliente["nacionalidad"] = st.text_input("Nacionalidad")
    datos_cliente["pais_residencia"] = st.text_input("País de Residencia")
    datos_cliente["direccion"] = st.text_input("Dirección")
    datos_cliente["telefono"] = st.text_input("Teléfono")
    datos_cliente["email"] = st.text_input("Email")
    datos_cliente["situacion_laboral"] = st.text_input("Situación Laboral")
    datos_cliente["actividad_empresa"] = st.text_input("Actividad Empresarial")
    datos_cliente["patrimonio"] = st.text_input("Patrimonio Aportado")
    
    plantilla_path = "plantilla_kyc_persona_fisica.docx"
    
elif tipo_cliente == "Persona Jurídica":
    st.header("Datos de la Empresa")
    datos_cliente["razon_social"] = st.text_input("Razón Social")
    datos_cliente["tipo_documento"] = st.selectbox("Tipo de Documento", ["CIF", "NIF"])
    datos_cliente["numero_documento"] = st.text_input("Número de Documento")
    datos_cliente["fecha_constitucion"] = st.date_input("Fecha de Constitución")
    datos_cliente["pais_constitucion"] = st.text_input("País de Constitución")
    datos_cliente["objeto_social"] = st.text_input("Objeto Social")
    datos_cliente["actividad_real"] = st.text_input("Actividad Real")
    datos_cliente["direccion"] = st.text_input("Dirección Fiscal")
    datos_cliente["telefono"] = st.text_input("Teléfono")
    datos_cliente["email"] = st.text_input("Email")
    datos_cliente["ingresos_anuales"] = st.text_input("Ingresos Anuales Estimados")
    
    plantilla_path = "plantilla_kyc_persona_juridica.docx"

# Botón para generar el documento
if st.button("Generar Documento KYC"):
    output = rellenar_kyc(datos_cliente, plantilla_path)
    st.download_button(
        label="Descargar Documento KYC",
        data=output.getvalue(),
        file_name="KYC_Completado.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
