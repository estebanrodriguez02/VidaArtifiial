import turtle

# Función para generar una cadena aplicando reglas de producción
def generate_string(axiom, production_rules, iterations):
    result = axiom

    for _ in range(iterations):
        result = ''.join(production_rules.get(c, c) for c in result)

    return result

# Función para interpretar una cadena y visualizarla con Turtle
def interpret_string(input_string, angle, size):
    turtle.speed(0)
    stack = []

    for char in input_string:
        if char == 'F':
            turtle.forward(size)
        elif char == '-':
            turtle.left(angle)
        elif char == '+':
            turtle.right(angle)

# Configuración inicial de Turtle
if __name__ == "__main__":
    axiom = 'F-F-F-F'
    production_rules = {'F': 'F-F+F+FF-F-F+F'}
    iterations = 10
    result = generate_string(axiom, production_rules, iterations)

    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()

    interpret_string(result, 90, 8)  # Ángulo de 90 grados

    turtle.done()
