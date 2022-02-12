Pasos para ejecutar el proyecto:
1. Clonar el repositorio
2. Configurar el proyecto con un virtualenv
3. Instalar los requirements.txt
4. Crear con PgAdmin una base de datos con el nombre de tutorialFlask
   1. Restaurar tutorialFlaskDump.tar en la base de datos tutorialFlask
5. Crear con PgAdmin una base de datos con el nombre tutorialFlaskORM
   1. Volcar la migración en la base de datos tutorialFlaskORM
      1. Desde una terminal ejecutar "flask db upgrade" 