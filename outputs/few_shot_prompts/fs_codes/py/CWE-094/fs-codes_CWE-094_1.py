first:

    module = request.args.get("module")
    exec("import urllib%s as urllib" % module)
second:
from flask import request

@app.route('/')
def index():
    '''
    get the module version from the request
    importing the urllib module with the version by using exec()
    '''

###
first:
    output = eval(inputStr)
    return output
second:
def evalInput(inputStr):
    '''
    run the inputStr as a python expression and return the result
    '''

###
first:
    usr_input = request.args['input']
    return str(eval(usr_input))
second:
def eval_code(request):
    '''
    get the user input from the request and eval it
    '''

###
first:
    if request.method == 'POST':
        first_name = base64.decodestring(request.POST.get('first_name', ''))
        exec("setname('%s')" % first_name)

second:
import base64