from pyknow import KnowledgeEngine, Fact, Rule

# Definir un hecho para representar las preferencias del usuario
class PreferenciasFact(Fact):
    pass

# Definir un hecho para representar las recomendaciones
class RecomendacionFact(Fact):
    pass

# Definir un motor de reglas
class SistemaExpertoDeportes(KnowledgeEngine):
    # Regla 1: Si al usuario le gusta el aire libre, entonces recomendar senderismo
    @Rule(PreferenciasFact(gusta_aire_libre=True))
    def regla_senderismo(self):
        self.declare(RecomendacionFact(deporte_recomendado="Senderismo"))

    # Regla 2: Si al usuario le gusta el agua, entonces recomendar natación
    @Rule(PreferenciasFact(gusta_agua=True))
    def regla_natacion(self):
        self.declare(RecomendacionFact(deporte_recomendado="Natación"))

# Crear una instancia del sistema experto
sistema_experto_deportes = SistemaExpertoDeportes()

# Definir las preferencias del usuario
preferencias_usuario = {
    "gusta_aire_libre": True,
    "gusta_agua": False
}

# Cargar las preferencias del usuario en el sistema experto
sistema_experto_deportes.reset()
sistema_experto_deportes.declare(PreferenciasFact(**preferencias_usuario))

# Ejecutar el sistema experto
sistema_experto_deportes.run()

# Obtener la recomendación del sistema experto
recomendacion = sistema_experto_deportes.facts[RecomendacionFact]

# Imprimir la recomendación
print("Deporte Recomendado:", recomendacion["deporte_recomendado"] if recomendacion else "No hay recomendación")
