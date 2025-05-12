# Laboratorio de Ingeniería de Operaciones - UCR

Este repositorio contiene los materiales del laboratorio de Ingeniería de Operaciones de la carrera de Ingeniería Industrial de la Universidad de Costa Rica (UCR).

## Estructura del repositorio

Cada carpeta corresponde a un tema particular del curso, y dentro de cada una encontrará:
- 📚 Contenidos teóricos relevantes
- 💻 Ejemplos prácticos para ejecutar
- 📊 Datos de ejemplo cuando sean requeridos
- 🧩 Ejercicios propuestos

## Cómo utilizar este repositorio

### Opción 1: Clonar el repositorio (recomendado)

1. Instala Git en tu computadora: [Descargar Git](https://git-scm.com/downloads)
2. Abre tu terminal o línea de comandos
3. Ejecuta:
   ```bash
   git clone https://github.com/mauricio-zamora-ucr/ingenieria_operaciones.git
   ```
4. Accede a la carpeta creada:
   ```bash
   cd ingenieria_operaciones
   ```

### Opción 2: Hacer Fork (para contribuir)

1. Haz clic en el botón "Fork" en la parte superior derecha de esta página
2. Selecciona tu cuenta personal donde quieres copiar el repositorio
3. Ahora tendrás tu propia copia donde puedes hacer cambios

### Opción 3: Usar GitHub Codespaces (sin instalar nada)

GitHub Codespaces es un entorno de desarrollo en la nube que te permite trabajar directamente desde tu navegador:

1. Haz clic en el botón verde "<> Code" arriba en este repositorio
2. Selecciona la pestaña "Codespaces"
3. Haz clic en "Create codespace on main"
4. Espera a que se cargue el entorno (puede tomar unos minutos la primera vez)
5. ¡Listo! Tienes un VS Code en la nube con todo configurado

Ventajas de Codespaces:
- No necesitas instalar software
- Funciona en cualquier computadora con navegador
- Tiene todo preconfigurado
- Puedes guardar tu progreso

## Sincronizar cambios (para quienes hicieron Fork)

Si el repositorio original se actualiza y quieres obtener los últimos cambios:

1. Ve a tu repositorio forkado
2. Haz clic en "Sync fork"
3. Luego en "Update branch"

O por línea de comandos:
```bash
git pull origin main
```

## Contribuciones

Si encuentras errores o quieres mejorar los materiales, puedes:
1. Crear un "Issue" reportando el problema
2. Hacer un "Pull Request" con tus mejoras

# Cómo Sincronizar tu Codespace con el Repositorio Principal

Si estás trabajando en GitHub Codespaces y necesitas obtener las actualizaciones del repositorio original (upstream), sigue estos pasos:

## 1. Configurar el repositorio upstream (solo primera vez)

1. Abre la terminal en tu Codespace
2. Ejecuta:
   ```bash
   git remote add upstream https://github.com/mauricio-zamora-ucr/ingenieria_operaciones.git
   ```
3. Verifica que se añadió correctamente:
   ```bash
   git remote -v
   ```
   Deberías ver tanto `origin` (tu fork) como `upstream` (el repo original).

## 2. Sincronizar cambios desde el repositorio principal

Cada vez que quieras actualizar tu Codespace con los últimos cambios del repo original:

1. Asegúrate de tener todos tus cambios locales guardados y commitados
2. En la terminal del Codespace ejecuta:
   ```bash
   git fetch upstream
   ```
3. Fusiona los cambios con tu rama main:
   ```bash
   git merge upstream/main
   ```
4. Sube los cambios a tu fork (opcional):
   ```bash
   git push origin main
   ```

## 3. Resolver conflictos (si los hay)

Si hay conflictos entre tus cambios y los del repositorio original:
1. GitHub Codespaces te mostrará los archivos en conflicto
2. Abre cada archivo y busca las secciones marcadas con `<<<<<<<`, `=======` y `>>>>>>>`
3. Edita los archivos para resolver los conflictos
4. Guarda los cambios
5. Haz commit de los cambios resueltos:
   ```bash
   git add .
   git commit -m "Resuelto merge conflict con upstream"
   ```

## 4. Sincronización visual con VS Code en Codespaces

1. Haz clic en el ícono de Control de Código Fuente en la barra lateral izquierda
2. En el menú de tres puntos (`...`) selecciona "Pull from"
3. Elige "upstream/main"
4. Si hay cambios, se fusionarán automáticamente

## Consejos importantes

- Antes de sincronizar, siempre haz commit de tus cambios locales
- Usa `git status` frecuentemente para ver el estado de tu repositorio
- Si algo sale mal, puedes deshacer el merge con:
  ```bash
  git merge --abort
  ```

Esta configuración te permite mantener tu Codespace actualizado con los últimos materiales del curso mientras preservas cualquier trabajo personal que hayas realizado.


---

📌 **Nota:** Este repositorio es parte del curso II-0703 Ingeniería de Operaciones de la Escuela de Ingeniería Industrial, UCR.

⌨️ Desarrollado por [Mauricio Zamora](https://github.com/mauricio-zamora-ucr)
