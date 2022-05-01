# 1. Library imports
from pyexpat import model
import uvicorn
from fastapi import FastAPI
from Request import weatherData
import pickle
# 2. Create the app object
app = FastAPI()
pickle_in = open("model.pkl","rb")
model = pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Hi, how are you': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_weather(data:weatherData):
    dataset = data.dict()
    A =dataset['a']
    B =dataset['b']
    C =dataset['c']
    D =dataset['d']
    E =dataset['e']
    F =dataset['f']
    prep = model.predict([[A,B,C,D,E,F]])
    return {
        'prediction': prep
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn Weather:app --reload