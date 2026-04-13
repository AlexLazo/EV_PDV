import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="Dashboard PDV Evaluados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.2rem;
        font-weight: 600;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    h1 {
        color: #1f77b4;
        text-align: center;
        margin-bottom: 30px;
    }
    h2 {
        color: #2c3e50;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Cargar datos
@st.cache_data
def load_data():
    from pathlib import Path

    base_path = Path(__file__).resolve().parent
    file_path = base_path / 'PDV_Evaluados.xlsx'

    if not file_path.exists():
        st.error(
            f"No se encontró el archivo de datos: {file_path} <br>" \
            "Asegúrate de que `PDV_Evaluados.xlsx` esté en la carpeta del proyecto."
        )
        st.stop()

    df = pd.read_excel(file_path)
    
    # Limpieza y normalización de datos
    df['Nombre usuario'] = df['Nombre usuario'].str.strip()
    df['Mes'] = df['Mes'].astype(str)
    df['UEN'] = df['UEN'].str.strip()
    
    # Normalizar nombres geográficos
    df['Departamento/Estado:'] = df['Departamento/Estado:'].str.strip().str.title()
    df['Municipio:'] = df['Municipio:'].str.strip().str.title()
    df['Zona/Barrio del cliente:'] = df['Zona/Barrio del cliente:'].str.strip().str.title()
    df['País:'] = df['País:'].str.strip().str.title()
    df['Nombre del cliente:'] = df['Nombre del cliente:'].str.strip()
    
    return df

df = load_data()

# Header principal
st.markdown("# 📊 Dashboard de PDV Evaluados")
st.markdown("---")

# Información general en columnas
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Evaluaciones", len(df), "registros")
col2.metric("Usuarios Únicos", df['Nombre usuario'].nunique(), "personas")
col3.metric("UENs", df['UEN'].nunique(), "unidades")
col4.metric("PDVs Evaluados", df['Nombre del cliente:'].nunique(), "clientes")

st.markdown("---")

# Tabs principales
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏆 Podio Digital",
    "📈 Dashboard General",
    "⚠️ Análisis de Riesgos",
    "👤 Desempeño por Usuario",
    "🗺️ Análisis Geográfico"
])

# ==================== TAB 1: PODIO DIGITAL ====================
with tab1:
    st.header("🏆 Podio Digital - Top Evaluadores")
    st.markdown("Ranking de usuarios por cantidad de PDVs evaluados")
    
    # Datos del podio
    usuarios_conteo = df['Nombre usuario'].value_counts().reset_index()
    usuarios_conteo.columns = ['Nombre usuario', 'PDVs Evaluados']
    usuarios_conteo['Ranking'] = range(1, len(usuarios_conteo) + 1)
    
    # Obtener top 3
    top3 = usuarios_conteo.head(3)
    
    # Calcular estadísticas por usuario
    def get_user_stats(nombre_usuario):
        user_data = df[df['Nombre usuario'] == nombre_usuario]
        sin_riesgo = (user_data['Calificaci\u00f3n'] == 'Sin Riesgo').sum()
        con_riesgo = len(user_data) - sin_riesgo
        porcentaje_sin_riesgo = (sin_riesgo / len(user_data) * 100) if len(user_data) > 0 else 0
        uens = user_data['UEN'].nunique()
        return sin_riesgo, con_riesgo, porcentaje_sin_riesgo, uens
    
    st.markdown("### 🎯 TOP 3 PODIO - CAMPEONES")
    st.markdown("")
    
    # Crear columnas para el podio
    podio_col1, podio_col2, podio_col3 = st.columns([1, 1.5, 1], gap="large")
    
    # Segundo lugar
    if len(top3) >= 2:
        with podio_col1:
            nombre = top3.iloc[1]['Nombre usuario']
            cantidad = top3.iloc[1]['PDVs Evaluados']
            sin_riesgo, con_riesgo, porcentaje, uens = get_user_stats(nombre)
            
            st.markdown("<div style='background: #C0C0C020; border: 2px solid #C0C0C0; border-radius: 8px; padding: 15px;'>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center;'><h2>🥈</h2></div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 18px; font-weight: bold; color: #C0C0C0;'>SEGUNDO LUGAR</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 16px; margin: 10px 0;'>{nombre}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 48px; font-weight: bold; color: #C0C0C0;'>{cantidad}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 12px; color: #888;'>PDVs Evaluados</div>", unsafe_allow_html=True)
            st.progress(porcentaje / 100)
            st.markdown(f"<div style='text-align: center; font-size: 12px;'>✅ {sin_riesgo} | ⚠️ {con_riesgo}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Primer lugar
    if len(top3) >= 1:
        with podio_col2:
            nombre = top3.iloc[0]['Nombre usuario']
            cantidad = top3.iloc[0]['PDVs Evaluados']
            sin_riesgo, con_riesgo, porcentaje, uens = get_user_stats(nombre)
            
            st.markdown("<div style='background: #FFD70020; border: 3px solid #FFD700; border-radius: 8px; padding: 15px;'>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center;'><h1>🥇</h1></div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 22px; font-weight: bold; color: #FFD700;'>PRIMER LUGAR</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 18px; margin: 10px 0; font-weight: bold;'>{nombre}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 56px; font-weight: bold; color: #FFD700;'>{cantidad}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 12px; color: #888;'>PDVs Evaluados</div>", unsafe_allow_html=True)
            st.progress(porcentaje / 100)
            st.markdown(f"<div style='text-align: center; font-size: 12px;'>✅ {sin_riesgo} | ⚠️ {con_riesgo}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Tercer lugar
    if len(top3) >= 3:
        with podio_col3:
            nombre = top3.iloc[2]['Nombre usuario']
            cantidad = top3.iloc[2]['PDVs Evaluados']
            sin_riesgo, con_riesgo, porcentaje, uens = get_user_stats(nombre)
            
            st.markdown("<div style='background: #CD7F3220; border: 2px solid #CD7F32; border-radius: 8px; padding: 15px;'>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center;'><h2>🥉</h2></div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 18px; font-weight: bold; color: #CD7F32;'>TERCER LUGAR</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 16px; margin: 10px 0;'>{nombre}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 48px; font-weight: bold; color: #CD7F32;'>{cantidad}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 12px; color: #888;'>PDVs Evaluados</div>", unsafe_allow_html=True)
            st.progress(porcentaje / 100)
            st.markdown(f"<div style='text-align: center; font-size: 12px;'>✅ {sin_riesgo} | ⚠️ {con_riesgo}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Análisis detallado de los Top 3
    st.markdown("### 📊 Análisis Detallado de Campeones")
    
    nombres_top = [top3.iloc[i]['Nombre usuario'] for i in range(len(top3))]
    tab_labels = [f"🥇 {top3.iloc[0]['Nombre usuario']}", f"🥈 {top3.iloc[1]['Nombre usuario']}", f"🥉 {top3.iloc[2]['Nombre usuario']}"]
    
    tabs_top3 = st.tabs(tab_labels[:len(top3)])
    
    for idx, (tab, nombre) in enumerate(zip(tabs_top3, nombres_top)):
        with tab:
            user_df = df[df['Nombre usuario'] == nombre]
            sin_riesgo, con_riesgo, porcentaje, uens = get_user_stats(nombre)
            
            # Métricas principales
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("📋 Total Evaluadas", len(user_df))
            col2.metric("✅ Sin Riesgo", sin_riesgo)
            col3.metric("⚠️ Con Riesgo", con_riesgo)
            col4.metric("🏢 UENs", uens)
            
            # Gráficos comparativos
            col1, col2 = st.columns(2)
            
            with col1:
                # Calificaciones
                calif = user_df['Calificaci\u00f3n'].value_counts()
                if len(calif) > 0:
                    fig = px.pie(
                        values=calif.values,
                        names=calif.index,
                        title="Distribución de Calificaciones",
                        color_discrete_sequence=px.colors.qualitative.Set2
                    )
                    st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Tendencia mensual
                mes_data = user_df.groupby('Mes').size().reset_index(name='Cantidad')
                if len(mes_data) > 0:
                    fig = px.bar(
                        mes_data,
                        x='Mes',
                        y='Cantidad',
                        title="Evaluaciones por Mes",
                        color='Cantidad',
                        color_continuous_scale='Blues'
                    )
                    st.plotly_chart(fig, use_container_width=True)
            
            # Tabla de evaluaciones
            st.subheader("Últimas Evaluaciones")
            cols_show = ['Dia del mes', 'Mes', 'Nombre del cliente:', 'UEN', 'Calificaci\u00f3n']
            cols_exist = [c for c in cols_show if c in user_df.columns]
            if cols_exist:
                df_show = user_df[cols_exist].tail(10).copy()
                st.dataframe(df_show, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Ranking completo
    st.markdown("### 📈 Ranking Completo")
    
    col1, col2 = st.columns([3, 1])
    with col2:
        top_n = st.slider("Mostrar top:", min_value=5, max_value=len(usuarios_conteo), value=10)
    
    usuarios_top = usuarios_conteo.head(top_n)
    
    fig_ranking = go.Figure()
    colores = ['#FFD700', '#C0C0C0', '#CD7F32'] + ['#3498db'] * (len(usuarios_top) - 3)
    
    fig_ranking.add_trace(go.Bar(
        y=usuarios_top['Nombre usuario'],
        x=usuarios_top['PDVs Evaluados'],
        orientation='h',
        marker=dict(color=colores[:len(usuarios_top)], line=dict(color='rgba(0,0,0,0.3)', width=2)),
        text=usuarios_top['PDVs Evaluados'],
        textposition='outside',
        hovertemplate='<b>%{y}</b><br>PDVs: %{x}<extra></extra>'
    ))
    
    fig_ranking.update_layout(
        title="Ranking General de Evaluadores",
        xaxis_title="PDVs Evaluados",
        yaxis_title="Usuario",
        height=500,
        template="plotly_white",
        showlegend=False
    )
    
    st.plotly_chart(fig_ranking, use_container_width=True)
    
    # Tabla resumen
    st.subheader("Tabla Resumen")
    tabla_top = usuarios_top.copy()
    medallas = ['🥇', '🥈', '🥉'] + ['  '] * (len(tabla_top) - 3)
    tabla_top['Medalla'] = medallas[:len(tabla_top)]
    tabla_top['Posición'] = tabla_top['Ranking'].astype(str) + 'º'
    tabla_top = tabla_top[['Medalla', 'Posición', 'Nombre usuario', 'PDVs Evaluados']]
    
    st.dataframe(tabla_top, use_container_width=True, hide_index=True)

# ==================== TAB 2: DASHBOARD GENERAL ====================
with tab2:
    st.header("📈 Dashboard General")
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    
    with col1:
        uen_filter = st.multiselect(
            "Filtrar por UEN:",
            options=sorted(df['UEN'].unique()),
            default=sorted(df['UEN'].unique())
        )
    
    with col2:
        mes_filter = st.multiselect(
            "Filtrar por Mes:",
            options=sorted(df['Mes'].unique()),
            default=sorted(df['Mes'].unique())
        )
    
    with col3:
        calificacion_filter = st.multiselect(
            "Filtrar por Calificación:",
            options=sorted(df['Calificaci\u00f3n'].unique()),
            default=sorted(df['Calificaci\u00f3n'].unique())
        )
    
    # Aplicar filtros
    df_filtered = df[
        (df['UEN'].isin(uen_filter)) &
        (df['Mes'].isin(mes_filter)) &
        (df['Calificaci\u00f3n'].isin(calificacion_filter))
    ]
    
    st.markdown(f"**Registros mostrados:** {len(df_filtered)} de {len(df)}")
    st.markdown("---")
    
    # Gráficos en filas
    col1, col2 = st.columns(2)
    
    # Gráfico 1: Calificación distribution
    with col1:
        calif_count = df_filtered['Calificaci\u00f3n'].value_counts().reset_index()
        calif_count.columns = ['Calificación', 'Cantidad']
        
        fig_calif = px.pie(
            calif_count,
            values='Cantidad',
            names='Calificación',
            title="Distribución de Calificaciones",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_calif, use_container_width=True)    
    with col2:
        # Gráfico: Evaluaciones por Mes
        pdv_mes = df_filtered.groupby('Mes').size().reset_index(name='Cantidad')
        
        fig_mes = px.line(
            pdv_mes,
            x='Mes',
            y='Cantidad',
            title="Tendencia de Evaluaciones",
            markers=True,
            line_shape='linear'
        )
        fig_mes.update_traces(line=dict(width=3, color='#1f77b4'))
        st.plotly_chart(fig_mes, use_container_width=True)    
    # Gráfico 3: PDVs por Día de la Semana  
    col1, col2 = st.columns(2)
    
    with col1:
        pdv_dia = df_filtered['Dia de la semana'].value_counts().reset_index()
        pdv_dia.columns = ['Día', 'Cantidad']
        
        orden_dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        pdv_dia['Día'] = pd.Categorical(pdv_dia['Día'], categories=orden_dias, ordered=True)
        pdv_dia = pdv_dia.sort_values('Día')
        
        fig_dia = px.bar(
            pdv_dia,
            x='Día',
            y='Cantidad',
            title="Evaluaciones por Día de la Semana",
            color='Cantidad',
            color_continuous_scale='Blues',
            text='Cantidad'
        )
        fig_dia.update_traces(textposition='outside')
        st.plotly_chart(fig_dia, use_container_width=True)
    
    with col2:
        # Resumen de métricas por UEN
        uen_summary = df_filtered['UEN'].value_counts().reset_index()
        uen_summary.columns = ['UEN', 'Cantidad']
        st.subheader("📊 Resumen por UEN")
        st.dataframe(uen_summary, use_container_width=True, hide_index=True)

# ==================== TAB 3: ANÁLISIS DE RIESGOS ====================
with tab3:
    st.header("⚠️ Análisis de Riesgos")
    
    # Columnas de riesgos
    riesgo_cols = [col for col in df.columns if col.startswith(('Ubicaci\u00f3n:', 'Espacio:', 'Reversa:', 'Descarga:', 'Suelo:', 'Inclinaci\u00f3n:', 'calzada', 'Condiciones', 'Iluminaci\u00f3n', 'Desniveles', '5s:', 'Distancia:', 'Carretillas:', 'Robos:', 'Amenaza', 'Riesgos:', 'Explosiones:', 'Agua:', 'Ventilaci\u00f3n:', 'El\u00e9ctrico:'))]
    
    if riesgo_cols:
        st.subheader("Resumen de Riesgos Identificados")
        
        # Contar riesgos por categoría (Si/Sí = riesgo identificado)
        riesgos_resumen = {}
        for col in riesgo_cols:
            si_count = (df[col].astype(str).str.lower().isin(['sí', 'si', 'yes', 's'])).sum()
            if si_count > 0:
                nombre_corto = col.split(':')[0][:40]  # Acortar nombre
                riesgos_resumen[nombre_corto] = si_count
        
        if riesgos_resumen:
            riesgos_df = pd.DataFrame(
                list(riesgos_resumen.items()),
                columns=['Tipo de Riesgo', 'Cantidad']
            ).sort_values('Cantidad', ascending=False)
            
            # Gráfico de riesgos
            fig_riesgos = px.bar(
                riesgos_df.head(15),
                x='Cantidad',
                y='Tipo de Riesgo',
                orientation='h',
                title="Top 15 Riesgos Identificados",
                color='Cantidad',
                color_continuous_scale='Reds',
                text='Cantidad'
            )
            fig_riesgos.update_traces(textposition='outside')
            st.plotly_chart(fig_riesgos, use_container_width=True)
            
            # Tabla de riesgos
            st.subheader("Tabla Detallada de Riesgos")
            st.dataframe(riesgos_df, use_container_width=True, hide_index=True)
            
            # Estadísticas de riesgos
            col1, col2, col3 = st.columns(3)
            total_riesgos = riesgos_df['Cantidad'].sum()
            evaluaciones_con_riesgo = (df['Calificaci\u00f3n'] != 'Sin Riesgo').sum()
            porcentaje_riesgo = (evaluaciones_con_riesgo / len(df)) * 100
            
            with col1:
                st.metric("Total de Riesgos Identificados", total_riesgos)
            with col2:
                st.metric("Evaluaciones con Riesgo", evaluaciones_con_riesgo)
            with col3:
                st.metric("% Evaluaciones con Riesgo", f"{porcentaje_riesgo:.1f}%")

# ==================== TAB 4: DESEMPEÑO POR USUARIO ====================
with tab4:
    st.header("👤 Desempeño por Usuario")
    
    # Selector de usuario
    usuario_seleccionado = st.selectbox(
        "Seleccionar Usuario:",
        options=sorted(df['Nombre usuario'].unique())
    )
    
    # Filtrar datos del usuario
    df_usuario = df[df['Nombre usuario'] == usuario_seleccionado]
    
    # Estadísticas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total de Evaluaciones", len(df_usuario))
    with col2:
        riesgos_count = (df_usuario['Calificaci\u00f3n'] != 'Sin Riesgo').sum()
        st.metric("Evaluaciones con Riesgo", riesgos_count)
    with col3:
        sin_riesgo = (df_usuario['Calificaci\u00f3n'] == 'Sin Riesgo').sum()
        st.metric("Sin Riesgo", sin_riesgo)
    with col4:
        porcentaje = (sin_riesgo / len(df_usuario) * 100) if len(df_usuario) > 0 else 0
        st.metric("% Sin Riesgo", f"{porcentaje:.1f}%")
    
    st.markdown("---")
    
    # Gráfico del usuario
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Calificaciones del usuario
        calif_usuario = df_usuario['Calificaci\u00f3n'].value_counts().reset_index()
        calif_usuario.columns = ['Calificación', 'Cantidad']
        
        fig_calif_user = px.pie(
            calif_usuario,
            values='Cantidad',
            names='Calificación',
            title=f"Distribución de Calificaciones - {usuario_seleccionado}",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig_calif_user, use_container_width=True)
    
    with col2:
        # Resumen por UEN
        uen_usuario = df_usuario['UEN'].value_counts().reset_index()
        uen_usuario.columns = ['UEN', 'Cantidad']
        
        st.subheader("📊 Resumen")
        st.dataframe(uen_usuario, use_container_width=True, hide_index=True)
    
    # Tabla de detalle de evaluaciones
    st.subheader("📋 Detalle de Evaluaciones")
    
    columnas_mostrar = ['Dia del mes', 'Mes', 'Nombre del cliente:', 'UEN', 'Calificaci\u00f3n', 'ACIs creados']
    columnas_existentes = [col for col in columnas_mostrar if col in df_usuario.columns]
    
    df_usuario_detalle = df_usuario[columnas_existentes].copy()
    df_usuario_detalle.columns = ['Día', 'Mes', 'Cliente', 'UEN', 'Calificación', 'ACIs']
    
    st.dataframe(df_usuario_detalle, use_container_width=True, hide_index=True)

# ==================== TAB 5: ANÁLISIS GEOGRÁFICO ====================
with tab5:
    st.header("🗺️ Análisis Geográfico")
    
    # Gráficos geografía
    col1, col2 = st.columns(2)
    
    with col1:
        # Por Departamento
        dept_count = df['Departamento/Estado:'].value_counts().head(10).reset_index()
        dept_count.columns = ['Departamento', 'Cantidad']
        
        fig_dept = px.bar(
            dept_count,
            x='Cantidad',
            y='Departamento',
            orientation='h',
            title="Top 10 Departamentos/Estados",
            color='Cantidad',
            color_continuous_scale='Sunset',
            text='Cantidad'
        )
        fig_dept.update_traces(textposition='outside')
        st.plotly_chart(fig_dept, use_container_width=True)
    
    with col2:
        # Por País
        pais_count = df['Pa\u00eds:'].value_counts().reset_index()
        pais_count.columns = ['País', 'Cantidad']
        
        fig_pais = px.pie(
            pais_count,
            values='Cantidad',
            names='País',
            title="Distribución por País",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_pais, use_container_width=True)
    
    # Por Municipio (Top 15)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        mun_count = df['Municipio:'].value_counts().head(15).reset_index()
        mun_count.columns = ['Municipio', 'Cantidad']
        
        fig_mun = px.bar(
            mun_count,
            x='Cantidad',
            y='Municipio',
            orientation='h',
            title="Top 15 Municipios",
            color='Cantidad',
            color_continuous_scale='Viridis',
            text='Cantidad'
        )
        fig_mun.update_traces(textposition='outside')
        st.plotly_chart(fig_mun, use_container_width=True)
    
    with col2:
        # Estadísticas geográficas
        st.subheader("📍 Estadísticas Geográficas")
        st.metric("Países", df['Pa\u00eds:'].nunique())
        st.metric("Departamentos/Estados", df['Departamento/Estado:'].nunique())
        st.metric("Municipios", df['Municipio:'].nunique())
        st.metric("Zonas/Barrios Únicos", df['Zona/Barrio del cliente:'].nunique())

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888; font-size: 0.85em;'>
    Dashboard generado automáticamente | Datos actualizados: {0}
    </div>
""".format(datetime.now().strftime("%d/%m/%Y %H:%M")), unsafe_allow_html=True)
