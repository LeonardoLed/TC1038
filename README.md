# TC1038 · Fundamentos de Programación

Sitio oficial del curso **TC1038 Fundamentos de Programación**, preparado como proyecto estático para **GitHub Pages**.

## Datos del curso

- **Profesor:** Dr. Leonardo Ledesma Domínguez
- **Sitio:** https://leonardoled.github.io/
- **Periodo:** 10 de agosto al 4 de diciembre de 2026
- **Clases:** lunes y jueves, 10:00–11:30
- **Asesorías:** miércoles y viernes · horario de asesores (previa cita)
- **Laboratorios:** martes de 14:05 a 14:55 **ó** viernes de 15:05 a 15:55
- **Semanas:** 17, de las cuales 2 son Semanas TEC sin clases
- **Semana TEC 1:** 14–18 de septiembre
- **Semana TEC 2:** 26–30 de octubre
- **Asueto:** lunes 16 de noviembre

## Evaluación

| Evidencia | Peso |
|---|---:|
| Exámenes Modulares (de avance) | 15% |
| Examen Final Integrador | 30% |
| Tareas y Actividades | 10% |
| Proyecto | 35% |
| Laboratorio | 10% |

### Exámenes de avance

- **Avance 1:** Temas 1, 2 y 3; se marca en la última sesión del Tema 3.
- **Avance 2:** Temas 4 y 5; se marca en la última sesión del Tema 5.
- **Avance 3:** Temas 6 y 7; se marca en la última sesión del Tema 7.
- **Avance 4:** Temas 8, 9 y 10; se marca en la última sesión del Tema 10.
- **Examen Final Integrador:** Sesión 28, lunes 30 de noviembre.

## Estructura académica

El curso está organizado en **13 temas**. Se agregó el Tema 12, **Terminal, rutas y organización de archivos**, porque el curso base contiene una actividad específica de rutas que no quedaba claramente representada en la estructura anterior. El Proyecto integrador pasó a Tema 13.

La actividad de autoestudio de ciclos (`actividad7-2.html`) se comparte entre los temas 5 (`while`) y 6 (`for`), ya que el curso base no contiene una práctica HTML independiente dedicada exclusivamente a `for`.

## Navegación

- Cada tarjeta del calendario es clicable y abre una subpágina en `sessions/`.
- Cada sesión indica su Tema/Módulo y muestra las actividades del curso base asociadas.
- Cada tarjeta de Tema abre una subpágina en `modules/`.
- Las actividades originales se conservan en `activities/base/`, junto con sus imágenes, documentos, CSS, JS y ejemplos para no romper enlaces relativos.
- `activities/index.html` funciona como catálogo moderno de actividades.
- Los avances del proyecto están en `project/`.
- Todos los enlaces a archivos PDF se abren en una pestaña nueva.

## Semana actual

La semana actual se detecta automáticamente usando la fecha del navegador. Cuando el semestre está en curso:

- su tarjeta recibe un **fondo azul claro**;
- el borde cambia a **azul Tec**;
- aparece la etiqueta **Semana actual**;
- el número de semana en el calendario de 17 semanas se colorea en azul;
- la tarjeta de inicio también se actualiza con el contenido de la semana.

## Carpetas principales

```text
.
├── index.html
├── assets/
│   ├── css/
│   ├── js/
│   └── icons/
├── data/
│   ├── calendar.json
│   ├── modules.json
│   ├── activities.json
│   ├── evaluation.json
│   └── ...
├── sessions/          # una subpágina por sesión
├── modules/           # una subpágina por tema
├── activities/
│   ├── index.html
│   └── base/          # copia funcional del curso base
├── project/           # avances del proyecto
├── materials/
│   ├── books/
│   ├── documents/
│   └── base-documents/
└── docs/
```

## Publicación en GitHub Pages

1. Sube el contenido del proyecto a la rama `main`.
2. En GitHub abre **Settings → Pages**.
3. Selecciona **Deploy from a branch**.
4. Rama: `main`.
5. Carpeta: `/ (root)`.
6. Guarda.

No requiere Node.js, npm ni un proceso de compilación.

## Desarrollo local

Como el sitio carga datos JSON mediante `fetch`, conviene usar un servidor local:

```bash
python -m http.server 8000
```

Luego abre `http://localhost:8000`.

## Flujo Git

```bash
git add .
git commit -m "Actualiza contenido de TC1038"
git push
```

## Cómo editar el calendario

El archivo principal es `data/calendar.json`. Cada sesión puede tener:

- `number`
- `date`
- `day`
- `time`
- `topic`
- `module`
- `page`
- `activities`
- `exam`, cuando corresponde

Al agregar una sesión nueva también debe crearse su subpágina en `sessions/`.

## Bibliografía

Los PDF de bibliografía se encuentran en `materials/books/`. También se incluye el recurso externo **El Libro de Python**: https://ellibrodepython.com/

---

Tecnológico de Monterrey · Campus Querétaro

## Ruta pedagógica por sesión

Cada subpágina de sesión está organizada en tres momentos: **Previo a la sesión**, **Durante la sesión** e **Implementa en tu proyecto**. Las actividades base se etiquetan explícitamente con el módulo al que pertenecen. El calendario enlaza cada sesión y muestra, cuando aplica, el avance del proyecto relacionado. Los avances del proyecto enlazan de regreso a los módulos que los alimentan.


## Diseño de páginas de sesión

Cada sesión tiene una página desagregada con: preparación previa, trabajo durante la clase, vínculo con el proyecto, pseudocódigo con estilo propio, ejemplo o punto de partida en Python, casos de prueba y checklist de aprendizaje. Los retos nuevos complementan las actividades base en una distribución aproximada 50/50.

La Sesión 1 es exclusivamente **Presentación y encuadre del curso**. El Tema 1 comienza formalmente en la Sesión 2.

Los bloques de código permiten copiar su contenido desde la interfaz y los retos se encuentran en `activities/challenges/`.
