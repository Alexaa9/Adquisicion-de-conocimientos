"""
Transcripción de hechos y reglas de la actividad de adquisición de conocimiento.
Basado en Actividad.pdf: clasificación de animales y entrevista sobre el perro doméstico.

Ejecución:
    python hechos_animales.py
"""

# Hechos
hechos = {
    "perro": {
        "animal",
        "tiene_pelo",
        "da_leche",  # característica de la especie: las hembras producen leche
        "perro_domestico",
        "aprende_ordenes",
        "olfato_desarrollado",
        "convive_con_humanos",
        "similar_a_perro_o_lobo",
    },
    # Ejemplos ilustrativos para representar los animales descritos en las reglas.
    
    "guepardo_ejemplo": {
        "animal", "tiene_pelo", "come_carne", "color_leonado", "manchas_oscuras"
    },
    "tigre_ejemplo": {
        "animal", "tiene_pelo", "come_carne", "rayas_negras"
    },
    "jirafa_ejemplo": {
        "animal", "tiene_pelo", "tiene_pezuñas", "cuello_largo", "manchas_oscuras"
    },
    "cebra_ejemplo": {
        "animal", "tiene_pelo", "tiene_pezuñas", "rayas_negras"
    },
    "pinguino_ejemplo": {
        "animal", "tiene_plumas", "nada", "blanco_negro"
    },
    "albatros_ejemplo": {
        "animal", "tiene_plumas", "vuela", "pone_huevos", "vuela_muy_bien"
    },
}

# Vínculos entre categorías y propiedades.

reglas = [
    (("animal", "tiene_pelo"), "mamifero"),
    (("animal", "da_leche"), "mamifero"),
    (("animal", "tiene_plumas"), "ave"),
    (("animal", "vuela", "pone_huevos"), "ave"),
    (("mamifero", "come_carne"), "carnivoro"),
    (("mamifero", "tiene_pezuñas"), "ungulado"),
    (("carnivoro", "color_leonado", "manchas_oscuras"), "guepardo"),
    (("carnivoro", "rayas_negras"), "tigre"),
    (("ungulado", "cuello_largo", "manchas_oscuras"), "jirafa"),
    (("ungulado", "rayas_negras"), "cebra"),
    (("ave", "nada", "blanco_negro"), "pinguino"),
    (("ave", "vuela_muy_bien"), "albatros"),
    # Reglas nuevas de la entrevista:
    (("animal", "tiene_pelo", "da_leche"), "mamifero"),
    (("perro_domestico",), "mamifero"),
    # La regla de observación es una orientación, no una clasificación automática.
]

def inferir(hechos_iniciales):
    """Aplica repetidamente las reglas hasta que ya no se agreguen predicados."""
    resultado = {animal: set(predicados) for animal, predicados in hechos_iniciales.items()}
    cambio = True

    while cambio:
        cambio = False
        for animal, predicados in resultado.items():
            for condiciones, conclusion in reglas:
                if all(condicion in predicados for condicion in condiciones):
                    if conclusion not in predicados:
                        predicados.add(conclusion)
                        cambio = True

            # La regla 15 requiere observación humana y no concluye una especie.
            if "similar_a_perro_o_lobo" in predicados:
                if "requiere_observar_comportamiento" not in predicados:
                    predicados.add("requiere_observar_comportamiento")
                    cambio = True

    return resultado

def mostrar_resultados(base_conocimiento):
    for animal, predicados in base_conocimiento.items():
        print(f"\\n{animal.replace('_', ' ').title()}:")
        for predicado in sorted(predicados):
            print(f"  - {predicado}")

if __name__ == "__main__":
    print("=== Hechos iniciales ===")
    mostrar_resultados(hechos)
    resultado = inferir(hechos)
    print("\\n=== Hechos y conclusiones inferidas ===")
    mostrar_resultados(resultado)
