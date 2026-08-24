# Guía de Desarrollo y Especificaciones: Proyecto 1 (Gomoku)

Documento de coordinación interna para la **Entrega 1** del curso Fundamentos de Inteligencia Artificial (UNAB). Contiene la arquitectura modular, contratos de interfaz, lógica paso a paso y responsabilidades asignadas para cada archivo.

---

## 📌 Reglas Oficiales de Gomoku (Variante Freestyle)

* **Tablero:** Tamaño configurable de `n x n`, con `n >= 5`. Comienza totalmente vacío.
* **Jugadores:** El jugador `A` siempre realiza el primer movimiento; el jugador `B` realiza el segundo movimiento.
* **Mecánica:** En cada turno se coloca una única ficha en una casilla vacía. Las fichas no se mueven, no se retiran y no se capturan. No se permite pasar turno.
* **Condición de Victoria:** Gana inmediatamente quien forme una línea ininterrumpida de **5 o más fichas consecutivas** de su color (horizontal, vertical o diagonales). Las líneas de 6 o más también otorgan la victoria.
* **Condición de Empate:** Ocurre cuando el tablero queda completamente lleno (se alcanzan `n * n` jugadas) sin que ningún jugador haya formado 5 en línea.
* **Coordenadas de Entrada:** Índices del `1` al `n` para filas y columnas en la consola del usuario.

---

## 🧱 Arquitectura y Estándares de Código

Para cumplir con la separación de responsabilidades exigida en el enunciado:
* **No usar librerías externas** para la lógica del juego[cite: 1].
* **Prohibido usar `print()` o `input()`** dentro de `tablero.py`, `validador.py` o `juego.py`[cite: 1]. La interacción con la consola pertenece exclusivamente a `main.py`[cite: 1].
* **PEP-8:** Variables y funciones en `snake_case`, clases en `PascalCase`, sangría de 4 espacios[cite: 1].
* **Tipado Estático (`mypy`):** Todas las funciones deben incluir anotaciones de tipo (`fila: int, columna: int) -> bool:`).

```text
proyecto_gomoku/
│
├── tablero.py       # (HECHO - Integrante 1) Modelo de datos y manipulación de la matriz n x n
├── validador.py     # (PENDIENTE - Integrante 2) Algoritmos de conteo en 4 ejes y empate
├── juego.py         # (PENDIENTE - Integrante 3) Controlador de estados y flujo de turnos
└── main.py          # (PENDIENTE - Integrante 3) Consola, renderizado e interacción de usuario