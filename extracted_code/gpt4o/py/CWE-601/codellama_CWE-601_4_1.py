from flask import Flask, request, redirect

app = Flask('flask_redirect_with_code')

@app.route('/')
def redirect_with_code():
    '''
        Redirect with code 302
    '''
    # Redirect to another URL (e.g., '/new-location') with status code 302
    return redirect('/new-location', code=302)

@app.route('/new-location')
def new_location():
    '''
        New location endpoint
    '''
    return "You have been redirected to the new location!"

if __name__ == '__main__':
    app.run(debug=True)
