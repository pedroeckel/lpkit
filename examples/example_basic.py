from lpkit import solve_with_simplex, solve_with_graphics

model_text = """
Max Z = 5*x1 + 2*x2
x1 <= 3
x2 <= 4
x1 + 2*x2 <= 9
x1 - 2*x2 <= 2
x1 >= 0
x2 >= 0
"""

solve_with_graphics(model_text, verbose={
    "show_gradient": True,
    "show_level_curves": True,
    "show_objective_value": True,
    "show_vertex_points": True,
    "show_optimal_point": True
})

solve_with_simplex(model_text)