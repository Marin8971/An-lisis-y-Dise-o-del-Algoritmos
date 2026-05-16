# Guía básica de GitHub + VS Code para trabajo en equipo

## 1. Crear una cuenta de GitHub

Si no tienes cuenta:

https://github.com

---

# 2. Instalar herramientas necesarias

## Instalar Git

Descargar:

https://git-scm.com/downloads

Verificar instalación:

```bash
git --version
```

---

## Instalar Visual Studio Code

https://code.visualstudio.com

---

# 3. Configurar Git por primera vez

Abrir terminal en VS Code y ejecutar:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tucorreo@gmail.com"
```

Verificar:

```bash
git config --list
```

---

# 4. Clonar un repositorio de GitHub

## Paso 1 — Copiar el enlace del repositorio

En GitHub:

```text
Code → HTTPS → copiar enlace
```

Ejemplo:

```bash
https://github.com/Marin8971/An-lisis-y-Dise-o-del-Algoritmos.git
```

---

## Paso 2 — Clonar en VS Code

Abrir terminal (en la carpeta en la que se quiera guardar el repositorio): 

```text
Terminal → New Terminal
```

Ejecutar:

```bash
git clone "https://github.com/Marin8971/An-lisis-y-Dise-o-del-Algoritmos.git"
```

---

## Paso 3 — Entrar a la carpeta

```bash
cd "An-lisis-y-Dise-o-del-Algoritmos"
```

---

## Paso 4 — Abrir el proyecto

```bash
code .
```

---

# 5. Flujo básico de trabajo en equipo

## MUY IMPORTANTE

Siempre seguir este orden:

```text
1. Descargar cambios
2. Trabajar
3. Guardar cambios
4. Hacer commit
5. Subir cambios
```

---

# 6. Descargar cambios del repositorio

Antes de empezar a trabajar:

```bash
git pull
```

Esto descarga:
- cambios del compañero,
- archivos nuevos,
- commits recientes.

---

# 7. Ver archivos modificados

```bash
git status
```

---

# 8. Guardar cambios en Git

## Agregar archivos

```bash
git add .
```

---

## Crear commit

```bash
git commit -m "descripcion del avance"
```

Ejemplos:

```bash
git commit -m "algoritmo backtracking terminado"
```

```bash
git commit -m "fix: algoritmo iterador modificado"
```

---

# 9. Subir cambios a GitHub

```bash
git push
```

---

# 10. Flujo recomendado para trabajar correctamente

## Cada vez que empieces:

```bash
git pull
```

---

## Después de trabajar:

```bash
git add .
git commit -m "mensaje"
git push
```

---

# 11. Qué es una rama (branch)

Una rama permite trabajar sin dañar la rama principal.

La principal normalmente se llama:

```text
main
```

---

# 12. Crear una rama nueva

Ejemplo:

```bash
git checkout -b desarrollo-backtracking
```

---

# 13. Ver ramas

```bash
git branch
```

---

# 14. Cambiar de rama

```bash
git checkout main
```

o:

```bash
git checkout desarrollo-backtracking
```

---

# 15. Subir una rama a GitHub

```bash
git push -u origin desarrollo-backtracking
```

---

# 16. Cómo hacer merge correctamente

## Paso 1 — Volver a main

```bash
git checkout main
```

---

## Paso 2 — Descargar cambios recientes

```bash
git pull
```

---

## Paso 3 — Hacer merge

```bash
git merge desarrollo-backtracking
```

---

## Paso 4 — Probar el proyecto

Verificar:
- que compile,
- que no existan errores,
- que todo funcione correctamente.

---

## Paso 5 — Subir cambios finales

```bash
git push
```

---

# 17. Qué es un conflicto

Un conflicto ocurre cuando:
- dos personas modifican la misma línea,
- Git no sabe cuál versión conservar.

---

# 18. Cómo resolver conflictos

Git mostrará algo así:

```text
<<<<<<< HEAD
codigo mio
=======
codigo compañero
>>>>>>> rama
```

Debes:
1. elegir qué código dejar,
2. borrar esas marcas,
3. guardar el archivo.

---

## Después:

```bash
git add .
git commit -m "conflicto resuelto"
git push
```

---

# 19. Recomendaciones IMPORTANTES

## NO trabajar directamente sobre main

Usar ramas para:
- nuevas funciones,
- algoritmos,
- cambios grandes.

---

## Hacer commits pequeños

MAL:

```text
"muchos cambios"
```

BIEN:

```text
"algoritmo greedy terminado"
```

---

## Hacer pull frecuentemente

Evita conflictos enormes.

---

## No editar exactamente lo mismo al mismo tiempo

Especialmente:
- informes,
- mismas funciones,
- mismos archivos.

---

# 20. Comandos más importantes

## Descargar cambios

```bash
git pull
```

---

## Ver estado

```bash
git status
```

---

## Agregar cambios

```bash
git add .
```

---

## Crear commit

```bash
git commit -m "mensaje"
```

---

## Subir cambios

```bash
git push
```

---

## Crear rama

```bash
git checkout -b nombre-rama
```

---

## Cambiar rama

```bash
git checkout main
```

---

## Hacer merge

```bash
git merge nombre-rama
```

---

# 21. Flujo profesional recomendado

```text
main
│
├── rama-algoritmo1
├── rama-algoritmo2
├── rama-informe
└── rama-tests
```

Cuando algo ya funciona:
- se hace merge a `main`.

---

# 22. Recomendación para proyectos universitarios

## Código

```text
VS Code + GitHub
```

## Informes colaborativos

```text
Overleaf
```

porque evita muchísimos conflictos en archivos `.tex`.
