import streamlit as st
import requests
import pokebase as pb
import matplotlib.pyplot as plt
import pandas as pd


#Prueba la aplicación en línea aquí
#https://pokeapi-subarudev.streamlit.app



# Funcion que devuelve una lista de los nombres de los Pokemon para el 
def obtener_pokemon():
    return [
        # Primera
        "bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard", "squirtle", "wartortle",
        "blastoise", "caterpie", "metapod", "butterfree", "weedle", "kakuna", "beedrill", "pidgey", "pidgeotto",
        "pidgeot", "rattata", "raticate", "spearow", "fearow", "ekans", "arbok", "pikachu", "raichu", "sandshrew",
        "sandslash", "nidoran-f", "nidorina", "nidoqueen", "nidoran-m", "nidorino", "nidoking", "clefairy", "clefable",
        "vulpix", "ninetales", "jigglypuff", "wigglytuff", "zubat", "golbat", "oddish", "gloom", "vileplume", "paras",
        "parasect", "venonat", "venomoth", "diglett", "dugtrio", "meowth", "persian", "psyduck", "golduck", "machop",
        "machoke", "machamp", "bellsprout", "weepinbell", "victreebel", "tentacool", "tentacruel", "geodude",
        "graveler", "golem", "ponyta", "rapidash", "slowpoke", "slowbro", "magnemite", "magneton", "farfetchd",
        "doduo", "dodrio", "seel", "dewgong", "grimer", "muk", "shellder", "cloyster", "gastly", "haunter", "gengar",
        "onix", "drowzee", "hypno", "krabby", "kingler", "exeggcute", "exeggutor", "cubone", "marowak", "lickitung",
        "kangaskhan", "horsea", "seadra", "goldeen", "seaking", "staryu", "starmie", "mr-mime", "scyther", "jynx",
        "electabuzz", "magmar", "pinsir", "tauros", "magikarp", "gyarados", "lapras", "ditto", "eevee", "vaporeon",
        "jolteon", "flareon", "porygon", "omanyte", "omastar", "kabuto", "kabutops", "aerodactyl", "mewtwo", "mew",
        #Segunda
        "chikorita", "bayleef", "meganium", "cyndaquil", "quilava", "typhlosion", "totodile", "croconaw", "feraligatr",
        "sentret", "furret", "hoothoot", "noctowl", "ledyba", "ledian", "spinarak", "ariados", "chinchou", "lanturn",
        "pichu", "cleffa", "igglybuff", "togepi", "togetic", "natu", "xatu", "mareep", "flaaffy", "ampharos", "hoppip",
        "skiploom", "jumpluff", "aipom", "sunkern", "sunflora", "yanma", "wooper", "quagsire", "espeon", "umbreon",
        "murkrow", "murkrow", "slowking", "wobbuffet", "gligar", "steelix", "sneasel", "teddiursa", "ursaring",
        "slugma", "magcargo", "swinub", "piloswine", "corsola", "remoraid", "octillery", "delibird", "swinub",
        "piloswine", "zubat", "lugia", "ho-oh", "celebi",
        # Tercera
        "treecko", "grovyle", "sceptile", "torchic", "combusken", "blaziken", "mudkip", "marshtomp", "swampert",
        "poochyena", "mightyena", "zigzagoon", "linoone", "wurmple", "silcoon", "beautifly", "cascoon", "dustox",
        "lotad", "lombre", "ludicolo", "seedot", "nuzleaf", "shiftry", "ralts", "kirlia", "gardevoir", "surskit",
        "masqurain", "shroomish", "breloom", "slakoth", "vigoroth", "slaking", "nincada", "ninjask", "shedinja",
        "whismur", "loudred", "exploud", "makuhita", "hariyama", "azurill", "nosepass", "geodude", "graveler", "golem",
        "trapinch", "vibrava", "flygon", "baltoy", "claydol", "aron", "lairon", "aggron", "meditite", "meditite",
        "meditich", "swablu", "altaria", "corphish", "crawdaunt", "finneon", "lumineon", "carvanha", "sharpedo",
        "beldum", "metang", "metagross", "registeel", "regice", "regirock", "kyogre", "groudon", "rayquaza", "jirachi",
        "deoxys",
        # Cuarta
        "turtwig", "grotle", "torterra", "chimchar", "monferno", "infernape", "piplup", "prinplup", "empoleon",
        "starly", "staravia", "staraptor", "bidoof", "bibarel", "kricketot", "kricketune", "shinx", "luxio", "luxray", "budew",
        "roselia", "roserade", "combee", "vespiquen", "pachirisu", "shellos", "gastrodon", "ambipom", "drifloon", "drifblim",
        "buneary", "lopunny", "machop", "machoke", "machamp", "meditite", "meditite", "meditich", "gible", "gabite", "garchomp",
        "riolu", "lucario", "carnivine", "finneon", "lumineon", "cherrim", "cherubi", "munchlax", "snorlax", "buizel", "floatzel", "hippopotas",
        "hippowdon", "bronzor", "bronzong", "chingling", "snover", "abomasnow", "weavile", "mismagius", "honchkrow", "spiritomb", "giratina", "dialga",
        "palkia", "manaphy", "phione", "shaymin", "arceus",
        # Quinta
        "victini", "snivy", "servine", "serperior", "tepig", "tepig", "pignite", "emboar", "oshawott", "dewott",
        "samurott", "patrat", "watchog", "lillipup", "herdier", "stoutland", "purrloin", "liepard", "sewaddle",
        "swadloon", "leavanny", "venipede", "whirlipede", "scolipede", "cottonee", "whimsicott", "petilil", "lilligant",
        "sandile", "krokorok", "krookodile", "darumaka", "darmanitan", "maractus", "dwebble", "crustle", "scraggy",
        "scrafty", "sigilyph", "yamask", "cofagrigus", "tirtouga", "carracosta", "archen", "archeops", "trubbish",
        "garbodor", "zorua", "zoroark", "minccino", "cinccino", "audino", "tympole", "palpitoad", "seismitoad", "throh",
        "sawk", "swanna", "vanillite", "vanillish", "vanilluxe", "deerling", "sawsbuck", "emolga", "karrablast",
        "escavalier", "foongus", "amoonguss", "frillish", "jellicent", "ferroseed", "ferrothorn", "charizard", "zekrom",
        "reshiram", "landorus", "tornadus", "thundurus", "kyurem", "meloetta", "genesect",
        # Sexta
        "chespin", "quilladin", "chestnaught", "fennekin", "braixen", "delphox", "froakie", "frogadier", "greninja",
        "bunnelby", "diggersby", "fletchinder", "talonflame", "scatterbug", "spewpa", "vivillon", "litleo", "pyroar",
        "flabebe", "floette", "florges", "diglett", "honedge", "doublade", "aegislash", "spritzee", "aromatisse",
        "swirlix", "slurpuff", "inkay", "malamar", "binacle", "barbacle", "skrelp", "dragalge", "helioptile",
        "heliolisk", "goomy", "sliggoo", "goodra", "skitty", "delcatty", "zygarde", "xerneas", "yveltal", "hoopa",
        "volcanion",
        # Septima
        "rowlet", "dartrix", "decidueye", "litten", "torracat", "incineroar", "popplio", "brionne", "primarina",
        "pikipek", "trumbeak", "toucannon", "yungoos", "gumshoos", "grubbin", "charjabug", "vikavolt", "crabrawler",
        "crabominable", "oricorio", "cutiefly", "ribombee", "rockruff", "lycanroc", "wishiwashi", "mareanie", "toxapex",
        "mudbray", "mudsdale", "dewpider", "araquanid", "mimikyu", "sandygast", "palossand", "stufful", "bewear",
        "bounsweet", "steenee", "tsareena", "comfey", "solgaleo", "lunala", "necrozma", "magearna", "marshadow",
        "zeraora", "poipole", "nihilego", "blacephalon", "stakataka", "kartana", "type: null", "silicobra", "sandaconda",
        # Octava
        "grookey", "thwackey", "rillaboom", "scorbunny", "raboot", "cinderace", "sobble", "drizzile", "inteleon",
        "skwovet", "greedent", "rookidee", "corvisquire", "corviknight", "blipbug", "dottler", "orbeetle", "nickit",
        "thievul", "gossifleur", "eldegoss", "wooloo", "dubwool", "chewtle", "drednaw", "yamper", "boltund", "impidimp",
        "morgrem", "grimmsnarl", "bunnelby", "diggersby", "toxel", "toxtricity", "sizzlipede", "centiskorch",
        "clobbopus", "grapploct", "sinistea", "polteageist", "hatenna", "hattrem", "hatterene", "applin", "flapple",
        "appletun", "zacian", "zamazenta", "eternatus", "kubfu", "urshifu", "calyrex", "spectrier", "glastrier",
        "regieleki", "regidrago", "zarude", "cufant", "copperajah", "rolycoly", "carkol", "coalossal", "toxtricity",
        "dragapult", "dreepy", "dracovish", "arctovish", "dracozolt", "arctozolt", "galarian ponyta",
        "galarian rapidash", "galarian weezing", "galarian farfetchd", "galarian zigzagoon", "galarian linoone",
        "galarian moltres", "galarian zapdos", "galarian articuno",
        #Novena
        "sprigatito", "floragato", "meowscarada", "fuecoco", "crocalor", "skeledirge", "quaxly", "quaxwell",
        "quaquaval", "lechonk", "oinkologne", "tarountula", "spidops", "nymble", "lokix", "fidough", "doughnot",
        "flaaffy", "mareep", "ampharos", "tinkatink", "tinkatuff", "tinkaton", "smoliv", "dolliv", "arboliva",
        "capsakid", "scovillain", "rellor", "rabsca", "shroodle", "grafaiai", "klawf", "nacli", "naclstack",
        "garganacl", "charcadet", "armarouge", "ceruledge", "wiglett", "wugtrio", "tatsugiri", "dondozo", "baxcalibur",
        "frigibax", "drayton", "iron treads", "iron hands", "iron jugulis", "iron moth", "iron thorns", "iron bundle",
        "iron crown", "gholdengo", "wugtrio", "walking wake", "iron leaves", "koraidon", "miraidon",
    ]


# Función para obtener la información de cada Pokemon
def obtener_info_pokemon(pokemones):
    info_pokemon = []  # Lista para almacenar los datos de los Pokemones

    # Iterar sobre la lista de Pokemones seleccionados
    for nombre in pokemones:
        try:
            # Realizar una solicitud para obtener los datos del Pokemon
            url = f"https://pokeapi.co/api/v2/pokemon/{nombre}/"
            respuesta = requests.get(url)

            # Extraer la respuesta en formato JSON
            data = respuesta.json()

            # Obtener el número de Pokedex (índice único de cada Pokemon)
            numero_pokedex = data['id']

            # Obtener la URL de la especie del Pokemon para poder saber su generación
            identificar_especies = data['species']['url']
            especies_respuesta = requests.get(identificar_especies)
            especies_data = especies_respuesta.json()

            # Extraer la generación del Pokemon desde la información de la especie
            generacion = especies_data['generation']['name']

            # Extraer los tipos del Pokemon (puede tener más de uno)
            tipos = [tipo['type']['name'] for tipo in data['types']]

            # Extraer las estadísticas (HP, ataque, defensa, etc.)
            info_pokemon.append({
                'Número de Pokedex': numero_pokedex,  # Número único del Pokemon
                'Nombre': nombre,  # Nombre del pokemon
                'Generación': generacion,  # Generación a la que pertenece el Pokemon
                'Altura (m)': data['height'] / 10,  # Convertir la altura de decímetros a metros
                'Peso (kg)': data['weight'] / 10,  # Convertir el peso de hectogramos a kilogramos
                'HP': next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'hp'),  # Vida
                'Ataque': next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'attack'),  # Ataque
                'Defensa': next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'defense'),  # Defensa
                'Velocidad': next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'speed'),  # Velocidad
                'Tipos': tipos  # Tipos de Pokemon (agua, fuego, etc.)
            })
        except requests.exceptions.RequestException as e:
            st.warning(f"No se pudo obtener información de {nombre}. Error de red: {e}")
        except KeyError as e:
            st.warning(f"Error al procesar los datos de {nombre}. Información incompleta. Error: {e}")

    return info_pokemon  # Devolver la lista con la información de los Pokemon

# Función principal de la aplicación
def main():
    st.title("Información de Pokémon")  # Título 

    # Cargar la lista predefinida 
    lista_pokemon = obtener_pokemon()

    # Texto de entrada para seleccionar los Pokemon que se desean ver
    input_pokemon = st.multiselect("Selecciona los Pokemon para ver su información:", lista_pokemon)

    # Procesar la entrada de Pokemon seleccionados
    if input_pokemon:
        # Obtener la información de los Pokemon seleccionados
        info = obtener_info_pokemon(input_pokemon)

        if info:
            # Crear un DataFrame de pandas con la información de los Pokemon
            df = pd.DataFrame(info)

            # Establecer el "Número de Pokedex" como índice en el DataFrame
            df.set_index('Número de Pokedex', inplace=True)

            # Mostrar la tabla con la información detallada de los Pokemon
            st.subheader("Datos de los Pokémon")
            st.dataframe(df)

            # Gráfico de barras para mostrar la altura de los Pokemon seleccionados
            plt.figure(figsize=(10, 6))
            plt.bar(df['Nombre'], df['Altura (m)'], color='skyblue', edgecolor='black')
            plt.title("Altura de los Pokémon", fontsize=16, fontweight='bold')
            plt.xlabel("Pokémon", fontsize=12)
            plt.ylabel("Altura (m)", fontsize=12)
            plt.xticks(rotation=45, fontsize=10)  # Rotar los nombres de los Pokemon para mejor visibilidad
            plt.yticks(fontsize=10)
            plt.grid(axis='y', linestyle='--', alpha=0.7)  # Añadir una cuadrícula horizontal
            st.pyplot(plt)

            # Gráfico de barras para mostrar el peso de los Pokemon seleccionados
            plt.figure(figsize=(10, 6))
            plt.bar(df['Nombre'], df['Peso (kg)'], color='salmon', edgecolor='black')
            plt.title("Peso de los Pokémon", fontsize=16, fontweight='bold')
            plt.xlabel("Pokémon", fontsize=12)
            plt.ylabel("Peso (kg)", fontsize=12)
            plt.xticks(rotation=45, fontsize=10)
            plt.yticks(fontsize=10)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            st.pyplot(plt)

            # Gráfico de barras para mostrar la distribución por generaciones
            contador_por_generacion = df['Generación'].value_counts()

            # Crear el gráfico
            plt.figure(figsize=(10, 6))
            plt.bar(contador_por_generacion.index, contador_por_generacion.values, color='lightgreen', edgecolor='black')
            plt.title("Distribución de Pokémon por Generación", fontsize=16, fontweight='bold')
            plt.xlabel("Generación", fontsize=12)
            plt.ylabel("Número de Pokémon", fontsize=12)
            plt.xticks(rotation=45, fontsize=10)
            plt.yticks(fontsize=10)

            # Asegurarse de que el eje Y solo tenga enteros
            plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))

            plt.grid(axis='y', linestyle='--', alpha=0.7)
            st.pyplot(plt)

            # Procesar los tipos de Pokemon para el gráfico de distribución por tipo
            tipos = df['Tipos'].explode().value_counts()

            # Asegurarnos de que los valores sean enteros 
            tipos = tipos.astype(int)

            # Crear el gráfico
            plt.figure(figsize=(10, 6))
            plt.bar(tipos.index, tipos.values, color='orange', edgecolor='black')
            plt.title("Distribución de Pokémon por Tipo", fontsize=16, fontweight='bold')
            plt.xlabel("Tipo", fontsize=12)
            plt.ylabel("Número de Pokémon", fontsize=12)
            plt.xticks(rotation=45, fontsize=10)
            plt.yticks(fontsize=10)

            # Establecer el eje Y como solo enteros
            plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))

            plt.grid(axis='y', linestyle='--', alpha=0.7)
            st.pyplot(plt)


if __name__ == '__main__':
    main()  # Llamar a la función principal para ejecutar la app
