from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)

# @app.route('/add')
# def add_res():
#     """Add a and b parameters."""
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     c = add(a, b)
#     return f"""<h1>Results</h1>
#             <p>{a} + {b} = {c}</p>
#     """

# @app.route('/sub')
# def sub_res():
#     """Subtract a and b parameters."""
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     c = sub(a,b)
#     return f"""<h1>Results</h1>
#             <p>{a} - {b} = {c}</p>
#     """

# @app.route('/mult')
# def mult_res():
#     """Subtract a and b parameters."""
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     c = mult(a,b)
#     return f"""<h1>Results</h1>
#             <p>{a} x {b} = {c}</p>
#     """

# @app.route('/div')
# def div_res():
#     """Subtract a and b parameters."""
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     c = div(a,b)
#     return f"""<h1>Results</h1>
#             <p>{a} / {b} = {c}</p>
#     """

OPERATIONS = {
    'add' : {'func' : add, 'symbol' : '+'},
    'sub' : {'func' : sub, 'symbol' : '-'},
    'mult' : {'func' : mult, 'symbol' : 'x'},
    'div' : {'func' : div, 'symbol' : '/'}
}

@app.route('/math/<operation>')
def do_math(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    c = OPERATIONS[operation]['func'](a, b)

    return f"""<h1>Results</h1>
               <p>{a} {OPERATIONS[operation]['symbol']} {b} = {c}</p>
            """
