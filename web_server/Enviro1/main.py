import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app= FastAPI()

def get_list():
    return[1,2,3]

@app.get('/')
def get_list():
    return {'name' : 'Lana'}

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return"""""
        <h1>Lana es una gorda. Viejita pero no chuchumeca</h1>
        <p>Mientras que ponky es ultragordo y joven y bello (Y nuevamente gordo. Es demasiado gordo jeje)</p>
    """

def run():
    store.get_categories()

if __name__== '__main__':
    run()
