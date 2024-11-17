import streamlit as st
import requests
import pokebase as pb
import matplotlib.pyplot as plt
import pandas as pd
import random 



#Prueba la aplicación en línea aquí
#https://pokeapi-subarudev.streamlit.app



# Funcion que devuelve una lista de los nombres de los Pokemon para el 
def obtener_pokemon():
    return [ 
             #Primera generacion 
            "bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard", "squirtle", "wartortle",
            "blastoise", "caterpie", "metapod", "butterfree", "weedle", "kakuna", "beedrill", "pidgey", "pidgeotto",
            "pidgeot", "rattata", "raticate", "spearow", "fearow", "ekans", "arbok", "pikachu", "raichu", "sandshrew",
            "sandslash", "nidoran-f", "nidorina", "nidoqueen", "nidoran-m", "nidorino", "nidoking", "clefairy",
            "clefable", "vulpix", "ninetales", "jigglypuff", "wigglytuff", "zubat", "golbat", "oddish", "gloom",
            "vileplume", "paras", "parasect", "venonat", "venomoth", "diglett", "dugtrio", "meowth", "persian",
            "psyduck", "golduck", "mankey", "primeape", "growlithe", "arcanine", "poliwag", "poliwhirl", "poliwrath",
            "abra", "kadabra", "alakazam", "machop", "machoke", "machamp", "bellsprout", "weepinbell", "victreebel",
            "tentacool", "tentacruel", "geodude", "graveler", "golem", "ponyta", "rapidash", "slowpoke", "slowbro",
            "magnemite", "magneton", "farfetchd", "doduo", "dodrio", "seel", "dewgong", "grimer", "muk", "shellder",
            "cloyster", "gastly", "haunter", "gengar", "onix", "drowzee", "hypno", "krabby", "kingler", "voltorb",
            "electrode", "exeggcute", "exeggutor", "cubone", "marowak", "hitmonlee", "hitmonchan", "lickitung",
            "koffing", "weezing", "rhyhorn", "rhydon", "chansey", "tangela", "kangaskhan", "horsea", "seadra",
            "goldeen", "seaking", "staryu", "starmie", "mr-mime", "scyther", "jynx", "electabuzz", "magmar", "pinsir",
            "tauros", "magikarp", "gyarados", "lapras", "ditto", "eevee", "vaporeon", "jolteon", "flareon", "porygon",
            "omanyte", "omastar", "kabuto", "kabutops", "aerodactyl", "snorlax", "articuno", "zapdos", "moltres",
            "dratini", "dragonair", "dragonite", "mewtwo", "mew",
            #Segunda generacion
            "chikorita", "bayleef", "meganium", "cyndaquil", "quilava", "typhlosion", "totodile", "croconaw",
            "feraligatr", "sentret", "furret", "hoothoot", "noctowl", "ledyba", "ledian", "spinarak", "ariados",
            "crobat", "chinchou", "lanturn", "pichu", "cleffa", "igglybuff", "togepi", "togetic", "natu", "xatu",
            "mareep", "flaaffy", "ampharos", "bellossom", "marill", "azumarill", "sudowoodo", "politoed", "hoppip",
            "skiploom", "jumpluff", "aipom", "sunkern", "sunflora", "yanma", "wooper", "quagsire", "espeon",
            "umbreon", "murkrow", "slowking", "misdreavus", "unown", "wobbuffet", "girafarig", "pineco", "forretress",
            "dunsparce", "gligar", "steelix", "snubbull", "granbull", "qwilfish", "scizor", "shuckle", "heracross",
            "sneasel", "teddiursa", "ursaring", "slugma", "magcargo", "swinub", "piloswine", "corsola", "remoraid",
            "octillery", "delibird", "mantine", "skarmory", "houndour", "houndoom", "kingdra", "phanpy", "donphan",
            "porygon2", "stantler", "smeargle", "tyrogue", "hitmontop", "smoochum", "elekid", "magby", "miltank",
            "blissey", "raikou", "entei", "suicune", "larvitar", "pupitar", "tyranitar", "lugia", "ho-oh", "celebi",
            #Tercera generacion
            "treecko", "grovyle", "sceptile", "torchic", "combusken", "blaziken", "mudkip", "marshtomp", "swampert",
            "poochyena", "mightyena", "zigzagoon", "linoone", "wurmple", "silcoon", "beautifly", "cascoon", "dustox",
            "lotad", "lombre", "ludicolo", "seedot", "nuzleaf", "shiftry", "taillow", "swellow", "wingull", "pelipper",
            "ralts", "kirlia", "gardevoir", "surskit", "masquerain", "shroomish", "breloom", "slakoth", "vigoroth",
            "slaking", "nincada", "ninjask", "shedinja", "whismur", "loudred", "exploud", "makuhita", "hariyama",
            "azurill", "nosepass", "skitty", "delcatty", "sableye", "mawile", "aron", "lairon", "aggron", "meditite",
            "medicham", "electrike", "manectric", "plusle", "minun", "volbeat", "illumise", "roselia", "gulpin",
            "swalot", "carvanha", "sharpedo", "wailmer", "wailord", "numel", "camerupt", "torkoal", "spoink", "grumpig",
            "spinda", "trapinch", "vibrava", "flygon", "cacnea", "cacturne", "swablu", "altaria", "zangoose",
            "seviper", "lunatone", "solrock", "barboach", "whiscash", "corphish", "crawdaunt", "baltoy", "claydol",
            "lileep", "cradily", "anorith", "armaldo", "feebas", "milotic", "castform", "kecleon", "shuppet",
            "banette", "duskull", "dusclops", "tropius", "chimecho", "absol", "wynaut", "snorunt", "glalie",
            "spheal", "sealeo", "walrein", "clamperl", "huntail", "gorebyss", "relicanth", "luvdisc", "bagon",
            "shelgon", "salamence", "beldum", "metang", "metagross", "regirock", "regice", "registeel", "latias",
            "latios", "kyogre", "groudon", "rayquaza", "jirachi", #"deoxys",
            #Cuarta generacion
            "turtwig", "grotle", "torterra", "chimchar", "monferno", "infernape", "piplup", "prinplup", "empoleon",
            "starly", "staravia", "staraptor", "bidoof", "bibarel", "kricketot", "kricketune", "shinx", "luxio",
            "luxray", "budew", "roserade", "cranidos", "rampardos", "shieldon", "bastiodon", "burmy",
            "mothim", "combee", "vespiquen", "pachirisu", "buizel", "floatzel", "cherubi", "cherrim", "shellos",
            "gastrodon", "ambipom", "drifloon", "drifblim", "buneary", "lopunny", "mismagius", "honchkrow", "glameow",
            "purugly", "chingling", "stunky", "skuntank", "bronzor", "bronzong", "bonsly", "mime-jr", "happiny",
            "chatot", "spiritomb", "gible", "gabite", "garchomp", "munchlax", "riolu", "lucario", "hippopotas",
            "hippowdon", "skorupi", "drapion", "croagunk", "toxicroak", "carnivine", "finneon", "lumineon", "mantyke",
            "snover", "abomasnow", "weavile", "magnezone", "lickilicky", "rhyperior", "tangrowth", "electivire",
            "magmortar", "togekiss", "yanmega", "leafeon", "glaceon", "gliscor", "mamoswine", "porygon-z", "gallade",
            "probopass", "dusknoir", "froslass", "rotom", "uxie", "mesprit", "azelf", "dialga", "palkia", "heatran",
            "regigigas", "giratina", "cresselia", "phione", "manaphy", "darkrai", "arceus",
            #Quinta generacion
            "victini", "snivy", "servine", "serperior", "tepig", "pignite", "emboar", "oshawott", "dewott", "samurott",
            "patrat", "watchog", "lillipup", "herdier", "stoutland", "purrloin", "liepard", "pansage", "simisage", "pansear",
            "simisear", "panpour", "simipour", "munna", "musharna", "pidove", "tranquill", "unfezant", "blitzle",
            "zebstrika", "roggenrola", "boldore", "gigalith", "woobat", "swoobat", "drilbur", "excadrill", "audino",
            "timburr", "gurdurr", "conkeldurr", "tympole", "palpitoad", "seismitoad", "throh", "sawk", "sewaddle",
            "swadloon", "leavanny", "venipede", "whirlipede", "scolipede", "cottonee", "whimsicott", "petilil",
            "lilligant", "sandile", "krokorok", "krookodile", "darumaka", "maractus",
            "dwebble", "crustle", "scraggy", "scrafty", "sigilyph", "yamask", "cofagrigus", "tirtouga", "carracosta",
            "archen", "archeops", "trubbish", "garbodor", "zorua", "zoroark", "minccino", "cinccino", "gothita",
            "gothorita", "gothitelle", "solosis", "duosion", "reuniclus", "ducklett", "swanna", "vanillite", "vanillish",
            "vanilluxe", "deerling", "sawsbuck", "emolga", "karrablast", "escavalier", "foongus", "amoonguss", "frillish",
            "jellicent", "alomomola", "joltik", "galvantula", "ferroseed", "ferrothorn", "klink", "klang", "klinklang",
            "tynamo", "eelektrik", "eelektross", "elgyem", "beheeyem", "litwick", "lampent", "chandelure", "axew",
            "fraxure", "haxorus", "cubchoo", "beartic", "cryogonal", "shelmet", "accelgor", "stunfisk", "mienfoo",
            "mienshao", "druddigon", "golett", "golurk", "pawniard", "bisharp", "bouffalant", "rufflet", "braviary",
            "vullaby", "mandibuzz", "heatmor", "durant", "deino", "zweilous", "hydreigon", "larvesta", "volcarona",
            "cobalion", "terrakion", "virizion", "reshiram", "zekrom", "kyurem",
            "genesect", #meloetta
            #Sexta generacion
            "chespin", "quilladin", "chesnaught", "fennekin", "braixen", "delphox", "froakie", "frogadier", "greninja",
            "bunnelby", "diggersby", "fletchling", "fletchinder", "talonflame", "scatterbug", "spewpa", "vivillon", "litleo",
            "pyroar", "flabebe", "floette", "florges", "skiddo", "gogoat", "pancham", "pangoro", "furfrou", "espurr",
            "honedge", "doublade", "spritzee", "aromatisse", "swirlix", "slurpuff", "inkay",
            "malamar", "binacle", "barbaracle", "skrelp", "dragalge", "clauncher", "clawitzer", "helioptile", "heliolisk",
            "tyrunt", "tyrantrum", "amaura", "aurorus", "sylveon", "hawlucha", "dedenne", "carbink", "goomy", "sliggoo",
            "goodra", "klefki", "phantump", "trevenant", "pumpkaboo", "bergmite", "avalugg", "noibat", "noivern",
            "xerneas", "yveltal", "diancie", "hoopa", "volcanion",
            #Septima generacion
            "rowlet", "dartrix", "decidueye", "litten", "torracat", "incineroar", "popplio", "brionne", "primarina", "pikipek",
            "trumbeak", "toucannon", "yungoos", "gumshoos", "grubbin", "charjabug", "vikavolt", "crabrawler", "crabominable",
            "cutiefly", "ribombee", "rockruff", "mareanie", "toxapex", "mudbray",
            "mudsdale", "dewpider", "araquanid", "fomantis", "lurantis", "morelull", "shiinotic", "salandit", "salazzle",
            "stufful", "bewear", "bounsweet", "steenee", "tsareena", "comfey", "oranguru", "passimian", "wimpod", "golisopod",
            "sandygast", "palossand", "pyukumuku", "type-null", "silvally", "komala", "turtonator", "togedemaru",
            "bruxish", "drampa", "dhelmise", "jangmo-o", "hakamo-o", "kommo-o", "tapu-koko", "tapu-lele",
            "tapu-bulu", "tapu-fini", "cosmog", "cosmoem", "solgaleo", "lunala", "nihilego", "buzzwole", "pheromosa",
            "xurkitree", "celesteela", "kartana", "guzzlord", "necrozma", "magearna", "marshadow", "poipole", "naganadel",
            "stakataka", "blacephalon", "zeraora", "meltan", "melmetal",
            #Octava generacion
            "grookey", "thwackey", "rillaboom", "scorbunny", "raboot", "cinderace", "sobble", "drizzile", "inteleon", "skwovet",
            "greedent", "rookidee", "corvisquire", "corviknight", "blipbug", "dottler", "orbeetle", "nickit", "thievul",
            "gossifleur", "eldegoss", "wooloo", "dubwool", "chewtle", "drednaw", "yamper", "boltund", "rolycoly", "carkol",
            "coalossal", "applin", "flapple", "appletun", "silicobra", "sandaconda", "cramorant", "arrokuda", "barraskewda",
            "toxel", "toxtricity", "sizzlipede", "centiskorch", "clobbopus", "grapploct", "sinistea", "polteageist", "hatenna",
            "hattrem", "hatterene", "impidimp", "morgrem", "grimmsnarl", "obstagoon", "perrserker", "cursola", "sirfetchd",
            "mr-rime", "runerigus", "milcery", "alcremie", "falinks", "pincurchin", "snom", "frosmoth", "stonjourner",
            "eiscue", "indeedee", "morpeko", "cufant", "copperajah", "dracozolt", "arctozolt", "dracovish", "arctovish",
            "duraludon", "dreepy", "drakloak", "dragapult", "zacian", "zamazenta", "eternatus", "kubfu",
            "zarude", "regieleki", "regidrago", "glastrier", "spectrier", "calyrex",
            #Novena generacion
            "sprigatito", "floragato", "meowscarada", "fuecoco", "crocalor", "skeledirge", "quaxly", "quaxwell", "quaquaval",
            "lechonk", "tarountula", "spidops", "nymble", "lokix", "rellor", "rabsca", "greavard", "houndstone",
            "flittle", "espathra", "farigiraf", "kingambit",
            "nacli", "naclstack", "garganacl", "gimmighoul", "gholdengo", "great-tusk", "scream-tail",
            "brute-bonnet", "flutter-mane", "slither-wing", "sandy-shocks", "iron-treads", "iron-bundle", "iron-hands",
            "iron-jugulis", "iron-moth", "iron-thorns", "frigibax", "arctibax", "baxcalibur", "tandemaus",
            "fidough", "dachsbun", "smoliv", "dolliv", "arboliva", "pawmi", "pawmo", "pawmot", "mabosstiff",
            "shroodle", "grafaiai", "capsakid", "scovillain", "tadbulb", "bellibolt", "wattrel", "kilowattrel", "bramblin",
            "brambleghast", "toedscool", "toedscruel", "klawf", "cetoddle", "cetitan", "veluza", "dondozo",
            "annihilape", "clodsire", "tinkatink", "tinkatuff", "tinkaton", "wiglett", "wugtrio", "bombirdier", "finizen",
            "varoom", "revavroom", "cyclizar", "orthworm", "glimmet", "glimmora",
] 


# Función para obtener información de los Pokémon
def obtener_info_pokemon(nombres_pokemon):
    info_pokemon = []

    for nombre in nombres_pokemon:
        try:
            # Obtener datos del Pokémon desde pokebase
            pokemon = pb.pokemon(nombre)
            especie = pb.pokemon_species(nombre)

            # Extraer información necesaria
            numero_pokedex = pokemon.id
            generacion = especie.generation.name
            tipos = [tipo.type.name for tipo in pokemon.types]
            stats = {stat.stat.name: stat.base_stat for stat in pokemon.stats}

            # Agregar información al listado
            info_pokemon.append({
                'Número de Pokedex': numero_pokedex,  # Número único del Pokémon
                'Nombre': nombre.capitalize(),  # Capitalizamos el nombre
                'Generación': generacion,  # Generación a la que pertenece el Pokémon
                'Altura (m)': pokemon.height / 10,  # Convertir altura de decímetros a metros
                'Peso (kg)': pokemon.weight / 10,  # Convertir peso de hectogramos a kilogramos
                'HP': stats.get('hp', 0),  # Vida base
                'Ataque': stats.get('attack', 0),  # Ataque base
                'Defensa': stats.get('defense', 0),  # Defensa base
                'Velocidad': stats.get('speed', 0),  # Velocidad base
                'Tipos': tipos  # Tipos del Pokémon
            })

        except Exception as e:
            st.warning(f"Error al obtener información de {nombre}: {e}")

    return info_pokemon

# Función para obtener la lista de Pokémon predefinida
def obtener_pokemon():
    try:
        # Usar Pokebase para obtener una lista de nombres de Pokémon
        return [pb.pokemon(i).name for i in range(1, 1021)]  # Ajustar rango según generación máxima
    except Exception as e:
        st.error(f"Error al obtener la lista de Pokémon: {e}")
        return []

# Función principal de la aplicación
def main():
    st.title("Información de Pokémon")  # Título

    # Cargar la lista predefinida 
    lista_pokemon = obtener_pokemon()

    # Variable para almacenar Pokémon seleccionados
    input_pokemon = st.multiselect("Selecciona los Pokémon para ver su información:", lista_pokemon)

    # Botón para generar 10 Pokémon aleatorios
    if st.button("Seleccionar 10 Pokémon al azar"):
        seleccion_aleatoria = random.sample(lista_pokemon, min(10, len(lista_pokemon)))  # Selecciona máximo 10 Pokémon
        input_pokemon.extend(seleccion_aleatoria)  # Agregar la selección aleatoria
        input_pokemon = list(set(input_pokemon))  # Eliminar duplicados
        st.experimental_set_query_params(pokemon=",".join(input_pokemon))  # Mantener persistencia

    # Procesar la entrada de Pokémon seleccionados
    if input_pokemon:
        # Obtener la información de los Pokémon seleccionados
        info = obtener_info_pokemon(input_pokemon)

        if info:
            # Crear un DataFrame de pandas con la información de los Pokémon
            df = pd.DataFrame(info)

            # Mapeo de generaciones para mostrarlo con formato amigable
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

            # Reemplazar las generaciones en el DataFrame
            df['Generación'] = df['Generación'].map(generacion_map)

            # Establecer el "Número de Pokedex" como índice en el DataFrame
            df.set_index('Número de Pokedex', inplace=True)

            # Mostrar la tabla con la información detallada de los Pokémon
            st.subheader("Datos de los Pokémon")
            st.dataframe(df)

            # Gráficos de alturas y pesos
            st.subheader("Altura de los Pokémon")
            plt.figure(figsize=(10, 6))
            plt.bar(df['Nombre'], df['Altura (m)'], color='skyblue', edgecolor='black')
            plt.xlabel("Pokémon", fontsize=12)
            plt.ylabel("Altura (m)", fontsize=12)
            plt.xticks(rotation=45, fontsize=10)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            st.pyplot(plt)

            st.subheader("Peso de los Pokémon")
            plt.figure(figsize=(10, 6))
            plt.bar(df['Nombre'], df['Peso (kg)'], color='salmon', edgecolor='black')
            plt.xlabel("Pokémon", fontsize=12)
            plt.ylabel("Peso (kg)", fontsize=12)
            plt.xticks(rotation=45, fontsize=10)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            st.pyplot(plt)

            # Distribución por generación
            contador_por_generacion = df['Generación'].value_counts()
            colores_generaciones = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#ffccff']
            st.subheader("Distribución de Pokémon por Generación")
            plt.figure(figsize=(8, 8))
            plt.pie(contador_por_generacion.values, labels=contador_por_generacion.index, colors=colores_generaciones,
                    autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black', 'linewidth': 1})
            plt.axis('equal')
            st.pyplot(plt)

            # Distribución por tipo
            tipos = df['Tipos'].explode().value_counts()
            tipo_colores = {
                'normal': '#A8A878', 'fire': '#C03028', 'water': '#6890F0', 'electric': '#F8D030',
                'grass': '#78C850', 'ice': '#98D8D8', 'fighting': '#F08030', 'poison': '#A040A0',
                'ground': '#E0C068', 'flying': '#A890F0', 'psychic': '#F85888', 'bug': '#A8B820',
                'rock': '#B8A038', 'ghost': '#705898', 'dragon': '#7038F8', 'dark': '#705848',
                'steel': '#B8B8D0', 'fairy': '#EE99AC'
            }
            colores = [tipo_colores.get(tipo, '#808080') for tipo in tipos.index]
            st.subheader("Distribución de Pokémon por Tipo")
            plt.figure(figsize=(10, 6))
            plt.bar(tipos.index, tipos.values, color=colores, edgecolor='black')
            plt.xlabel("Tipo", fontsize=12)
            plt.ylabel("Número de Pokémon", fontsize=12)
            plt.xticks(rotation=45, fontsize=10)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            st.pyplot(plt)

if __name__ == '__main__':
    main()