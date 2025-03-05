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

# Estado de selección de cliente
if "tipo_cliente" not in st.session_state:
    st.session_state.tipo_cliente = None

# Pantalla principal con dos cards
if st.session_state.tipo_cliente is None:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Persona Física")
        if st.button("Seleccionar Persona Física"):
            st.session_state.tipo_cliente = "Persona Física"
    with col2:
        st.subheader("Persona Jurídica")
        if st.button("Seleccionar Persona Jurídica"):
            st.session_state.tipo_cliente = "Persona Jurídica"

# Mostrar el formulario solo después de seleccionar una opción
if st.session_state.tipo_cliente:
    st.header(f"Formulario KYC - {st.session_state.tipo_cliente}")
    
    datos_cliente = {}
    
    if st.session_state.tipo_cliente == "Persona Física":
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
    
    elif st.session_state.tipo_cliente == "Persona Jurídica":
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
