# TC1038 · Fundamentos de Programación

Sitio web estático del curso **TC1038 Fundamentos de Programación**, preparado para publicarse directamente con **GitHub Pages**.

## Publicación rápida en GitHub Pages

1. Crea un repositorio nuevo en GitHub, por ejemplo `TC1038-Fundamentos`.
2. Descomprime este ZIP.
3. Sube **todos los archivos y carpetas contenidos dentro del ZIP** a la raíz del repositorio. `index.html` debe quedar en el nivel principal, no dentro de otra carpeta.
4. En GitHub abre **Settings → Pages**.
5. En **Build and deployment**, selecciona:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/ (root)`
6. Presiona **Save**.
7. GitHub mostrará la dirección pública del sitio después de completar el despliegue.

La estructura correcta en GitHub debe verse así:

```text
TC1038-Fundamentos/
├── index.html
├── 404.html
├── .nojekyll
├── README.md
├── LICENSE
├── assets/
├── data/
├── docs/
└── materials/
```

## Características

- Sitio web responsivo para escritorio, tableta y celular.
- Identidad visual azul y gris inspirada en el Tecnológico de Monterrey.
- Navegación por inicio, calendario, módulos, actividades, proyecto, evaluación y recursos.
- Modo claro y oscuro.
- Calendario filtrable.
- Contenido académico separado en archivos JSON.
- Materiales descargables y actividades de cursos anteriores.
- No requiere Node.js, React, bases de datos ni instalación de dependencias.
- Compatible con GitHub Pages y cualquier servidor web estático.

## Ejecución local

No abras únicamente `index.html` con doble clic, ya que el navegador puede bloquear la lectura de los archivos JSON. Inicia un servidor local desde la raíz del proyecto.

Con Python:

```bash
python -m http.server 8000
```

Después abre:

```text
http://localhost:8000
```

## Arquitectura

```text
.
├── index.html                  # Página principal
├── 404.html                    # Respaldo para GitHub Pages
├── .nojekyll                   # Evita procesamiento innecesario de Jekyll
├── assets/
│   ├── css/
│   │   ├── variables.css       # Colores y variables visuales
│   │   └── main.css            # Componentes, layout y responsividad
│   └── js/
│       └── app.js              # Carga y renderizado de contenido
├── data/
│   ├── course.json             # Datos generales del curso
│   ├── calendar.json           # Semanas y sesiones
│   ├── modules.json            # Módulos académicos
│   ├── project.json            # Etapas del proyecto integrador
│   ├── evaluation.json         # Esquema de evaluación
│   ├── resources.json          # Recursos descargables
│   └── announcements.json      # Avisos del curso
├── materials/
│   ├── documents/              # PDF y documentos del curso
│   └── legacy/activities/      # Actividades heredadas
└── docs/                       # Documentación de mantenimiento
```

## Actualización del contenido

### Calendario

Edita `data/calendar.json`. Cada semana utiliza la siguiente estructura:

```json
{
  "week": 1,
  "title": "Introducción a la programación",
  "status": "current",
  "sessions": [
    {
      "date": "2026-08-10",
      "title": "Presentación del curso"
    }
  ]
}
```

Estados admitidos:

- `current`: semana actual.
- `upcoming`: semana próxima.

### Módulos

Edita `data/modules.json` para modificar títulos, descripciones y temas.

```json
{
  "number": 1,
  "title": "Algoritmos",
  "description": "Diseño de soluciones paso a paso.",
  "topics": ["Pseudocódigo", "Diagramas de flujo"]
}
```

### Recursos

1. Copia el archivo dentro de `materials/documents/`.
2. Añádelo a `data/resources.json`.

```json
{
  "title": "Convenciones de estilo en Python",
  "module": "Programación en Python",
  "type": "PDF",
  "url": "materials/documents/Convenciones de Estilo en Python.pdf"
}
```

Evita cambiar nombres de archivos después de publicarlos. Si necesitas hacerlo, actualiza también su ruta dentro del JSON correspondiente.

## Personalización visual

Los colores principales se administran desde `assets/css/variables.css`.

```css
:root {
  --primary: #003b70;
  --secondary: #005eb8;
  --accent: #00a3e0;
  --background: #f5f7f9;
  --surface: #ffffff;
  --text: #263238;
}
```

## Reutilización para otro semestre

1. Cambia el periodo en `index.html` y `data/course.json`.
2. Actualiza fechas y estados en `data/calendar.json`.
3. Revisa `data/evaluation.json`.
4. Sustituye los documentos necesarios.
5. Actualiza enlaces a Canvas, Teams o GitHub.
6. Conserva la misma arquitectura para evitar enlaces rotos.

## Solución de problemas

### La página aparece en blanco

Comprueba que `index.html` esté en la raíz del repositorio y que GitHub Pages publique desde `main / (root)`.

### Se muestra el diseño pero no aparecen módulos o semanas

Revisa la consola del navegador y valida que los archivos de `data/` sean JSON válido. También comprueba mayúsculas y minúsculas en nombres de carpetas y archivos, ya que GitHub Pages las distingue.

### Los PDF no abren

Verifica que la ruta registrada en `data/resources.json` coincida exactamente con el nombre del archivo.

### Los cambios no aparecen

Espera a que finalice la acción de despliegue de GitHub Pages y actualiza la página omitiendo caché con `Ctrl + F5`.

## Tecnologías

- HTML5
- CSS3
- JavaScript moderno
- JSON
- GitHub Pages

## Autor

**Dr. Leonardo Ledesma Domínguez**  
Tecnológico de Monterrey · Campus Querétaro

## Licencia

Consulta el archivo `LICENSE` incluido en el repositorio.

## Calendario AD2026

- **Inicio del curso:** 10 de agosto de 2026.
- **Fin del curso:** 4 de diciembre de 2026.
- **Clases:** lunes y jueves, de 10:00 a 11:30.
- **Asesorías:** miércoles y viernes; el horario está pendiente de definición.
- **Semana TEC 1:** 14–18 de septiembre, sin clases.
- **Semana TEC 2:** 26–30 de octubre, sin clases.
- **Asueto:** lunes 16 de noviembre, sin clase.
- **Duración:** 17 semanas, incluidas 2 Semanas TEC.

Cada clase está registrada como una sesión numerada en `data/calendar.json`. La página determina automáticamente la semana actual a partir de la fecha del dispositivo y la destaca en el resumen del semestre y en el calendario detallado.

## Libros y recursos incorporados

Los libros PDF se encuentran en `materials/books/` y se muestran en la sección **Libros y recursos**. El sitio también enlaza a *El Libro de Python* como recurso web en español. Para añadir o retirar bibliografía, edita `data/resources.json`.

> Nota: *The Python Book, 2nd Edition* se ofrece como material complementario, ya que parte de sus ejemplos utiliza Python 2. Para el curso se debe priorizar Python 3.
