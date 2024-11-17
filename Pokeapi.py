import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd
import random
import asyncio
import aiohttp

# ---------------------------------
# Cargar lista completa de Pokémon
# ---------------------------------
@st.cache_data(ttl=86400)  # Caché de 24 horas
def obtener_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1020"
    respuesta = requests.get(url)
    data = respuesta.json()
    return [pokemon['name'] for pokemon in data['results']]

# ---------------------------------
# Obtener información de Pokémon (con asyncio para mayor velocidad)
# ---------------------------------
@st.cache_data(ttl=3600)  # Caché de 1 hora
async def obtener_info_pokemon_async(pokemones):
    info_pokemon = []

    async def fetch_data(session, nombre):
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{nombre}/"
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()

                    # Extraer información de especie para obtener generación
                    especies_url = data['species']['url']
                    async with session.get(especies_url) as especies_resp:
                        if especies_resp.status == 200:
                            especies_data = await especies_resp.json()
                            generacion = especies_data['generation']['name']

                    return {
                        'Número de Pokedex': data['id'],
                        'Nombre': nombre,
                        'Generación': generacion,
                        'Altura (m)': data['height'] / 10,
                        'Peso (kg)': data['weight'] / 10,
                        'HP': next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'hp'),
                        'Ataque': next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'attack'),
                        'Defensa': next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'defense'),
                        'Velocidad': next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'speed'),
                        'Tipos': [tipo['type']['name'] for tipo in data['types']]
                    }
        except Exception as e:
            st.warning(f"Error al procesar {nombre}: {e}")
            return None

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, nombre) for nombre in pokemones]
        resultados = await asyncio.gather(*tasks)
        info_pokemon = [res for res in resultados if res is not None]

    return info_pokemon

def obtener_info_pokemon(pokemones):
    return asyncio.run(obtener_info_pokemon_async(pokemones))

# ---------------------------------
# Función principal de la app
# ---------------------------------
def main():
    st.title("Información de Pokémon")

    # Cargar lista de Pokémon
    lista_pokemon = obtener_pokemon()

    # Selección de Pokémon
    input_pokemon = st.multiselect("Selecciona los Pokémon para ver su información:", lista_pokemon)

    # Botón para seleccionar 10 Pokémon aleatorios
    if st.button("Seleccionar 10 Pokémon al azar"):
        seleccion_aleatoria = random.sample(lista_pokemon, min(10, len(lista_pokemon)))
        input_pokemon.extend(seleccion_aleatoria)
        input_pokemon = list(set(input_pokemon))
        st.experimental_set_query_params(pokemon=",".join(input_pokemon))

    # Procesar la información seleccionada
    if input_pokemon:
        with st.spinner("Cargando información de los Pokémon..."):
            info = obtener_info_pokemon(input_pokemon)

        if info:
            # Crear DataFrame con la información de Pokémon
            df = pd.DataFrame(info)

            # Mapear generaciones a un formato amigable
            generacion_map = {
                'generation-i': '1° Generación',
                'generation-ii': '2° Generación',
                'generation-iii': '3° Generación',
                'generation-iv': '4° Generación',
                'generation-v': '5° Generación',
                'generation-vi': '6° Generación',
                'generation-vii': '7° Generación',
                'generation-viii': '8° Generación',
                'generation-ix': '9° Generación'
            }
            df['Generación'] = df['Generación'].map(generacion_map)
            df.set_index('Número de Pokedex', inplace=True)

            # Mostrar tabla de datos
            st.subheader("Datos de los Pokémon")
            st.dataframe(df)

            # Gráficos (altura, peso, generaciones, tipos)
            # Altura
            st.subheader("Altura de los Pokémon")
            plt.figure(figsize=(10, 6))
            plt.bar(df['Nombre'], df['Altura (m)'], color='skyblue', edgecolor='black')
            plt.xticks(rotation=45)
            st.pyplot(plt)

            # Peso
            st.subheader("Peso de los Pokémon")
            plt.figure(figsize=(10, 6))
            plt.bar(df['Nombre'], df['Peso (kg)'], color='salmon', edgecolor='black')
            plt.xticks(rotation=45)
            st.pyplot(plt)

            # Generaciones
            st.subheader("Distribución por Generación")
            contador_por_generacion = df['Generación'].value_counts()
            plt.figure(figsize=(8, 8))
            plt.pie(contador_por_generacion, labels=contador_por_generacion.index, autopct='%1.1f%%', startangle=140)
            st.pyplot(plt)

            # Tipos
            st.subheader("Distribución por Tipo")
            tipos = df['Tipos'].explode().value_counts()
            plt.figure(figsize=(10, 6))
            plt.bar(tipos.index, tipos.values, color='green', edgecolor='black')
            plt.xticks(rotation=45)
            st.pyplot(plt)

if __name__ == '__main__':
    main()
