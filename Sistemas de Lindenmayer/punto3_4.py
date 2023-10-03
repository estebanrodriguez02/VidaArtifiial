import turtle

# Definimos las reglas de producción
def apply_rules(s):
    new_s = ""
    for char in s:
        if char == 'F':
            new_s += 'FF'
        elif char == 'G':
            new_s += 'FG[−F[G]−G][G+G][+F[G]+G]'
        else:
            new_s += char
    return new_s

# Configuramos el sistema
initial_string = "G"
iterations = 4
step_length = 10

# Inicializamos la tortuga
t = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(0)

# Implementamos el sistema de interpretación con pila
stack = []

for _ in range(iterations):
    initial_string = apply_rules(initial_string)

for char in initial_string:
    if char == 'F' or char == 'G':
        t.forward(step_length)
    elif char == '+':
        t.left(22.5)  # Ángulo modificado a 22.5 grados
    elif char == '-':
        t.right(22.5)  # Ángulo modificado a 22.5 grados
    elif char == '[':
        stack.append((t.position(), t.heading()))
    elif char == ']':
        position, heading = stack.pop()
        t.penup()
        t.goto(position)
        t.setheading(heading)
        t.pendown()

# Mostramos el resultado
screen.update()
turtle.done()
