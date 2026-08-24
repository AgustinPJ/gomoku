# Proyecto 1: Gomoku (Búsqueda Adversarial) - Entrega 1

Proyecto desarrollado para el ramo de **Fundamentos de Inteligencia Artificial** (Universidad Andrés Bello). 
En esta primera etapa se implementa el juego base funcional para **2 jugadores humanos** en consola, con arquitectura orientada a objetos, código modular y tipado estático (`mypy`).

---

## 📌 Reglas Oficiales del Juego (Variante Freestyle)

* **Tablero:** Tamaño configurable $n \times n$, con $n \ge 5$. Comienza totalmente vacío.
* **Jugadores:** `A` (primer turno) y `B` (segundo turno).
* **Mecánica:** En cada turno se coloca una ficha en una casilla vacía. Las fichas no se mueven, retiran ni capturan. No se puede pasar turno.
* **Condición de Victoria:** Ganador inmediato al conectar **5 o más fichas consecutivas** de forma ininterrumpida (horizontal, vertical o diagonales).
* **Condición de Empate:** Tablero lleno ($n \times n$ fichas jugadas) sin que ningún jugador forme 5 en línea.
* **Coordenadas de Entrada:** Índices del $1$ al $n$ para filas y columnas.

---

## 🧱 Arquitectura del Proyecto

El código está dividido en 4 archivos para separar estrictamente la lógica interna de la interacción con el usuario (PEP-8):

```text
proyecto_gomoku/
│
├── tablero.py       # (HECHO) Modelo de datos y gestión de la grilla nxn.
├── validador.py     # (PENDIENTE) Lógica de detección de 5 en línea y empate.
├── juego.py         # (PENDIENTE) Controlador de turnos y estado de la partida.
└── main.py          # (PENDIENTE) Interfaz de consola, inputs del usuario y visualización.