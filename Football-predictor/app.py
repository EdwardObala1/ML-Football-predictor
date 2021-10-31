import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("model.pkl","rb")
mlp_model=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Hi"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Age,Special,LS,ST,RS,LW,LF,CF,RF,RW,LAM,CAM,RAM,LM,LCM,CM,RCM,RM,LWB,LDM,CDM,RDM,RWB,LB,RB,
        Crossing,Finishing,HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,FKAccuracy,LongPassing,BallControl,Reactions,ShotPower,Strength,Aggression,Interceptions,
        Positioning,Vision,Penalties,Composure):
   
    prediction=mlp_model.predict([[Age,Special,LS,ST,RS,LW,LF,CF,RF,RW,LAM,CAM,RAM,LM,LCM,CM,RCM,RM,LWB,LDM,CDM,RDM,RWB,LB,RB,
        Crossing,Finishing,HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,FKAccuracy,LongPassing,BallControl,Reactions,ShotPower,Strength,Aggression,Interceptions,
        Positioning,Vision,Penalties,Composure]])
    print(prediction)
    return prediction

'Age','Special','LS','ST','RS','LW','LF','CF','RF','RW','LAM','CAM','RAM','LM','LCM','CM','RCM','RM','LWB','LDM','CDM','RDM','RWB','LB','RB','Crossing','Finishing','HeadingAccuracy','ShortPassing',
'Volleys','Dribbling','Curve','FKAccuracy','LongPassing','BallControl','Reactions','ShotPower','Strength','Aggression','Interceptions','Positioning','Vision','Penalties','Composure','Release Clause'


def main():
    st.title("Fifa Predictor")
    html_temp = """
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;">ML Project</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.slider("Age", 0, 50)
    Special = st.slider('Special', 0, 100)
    InternationalReputation = st.slider('InternationalReputation', 0, 10)
    SkillMoves = st.slider("SkillMoves", 0, 100)
    WorkRate = st.slider("WorkRate", 0, 100)
    LS = st.slider("LS", 0, 100)
    ST = st.slider('ST', 0, 100)
    RS = st.slider('RS', 0, 100)
    LW = st.slider('LW', 0, 100)
    LF = st.slider('LF', 0, 100)
    CF = st.slider('CF', 0, 100)
    RF = st.slider("RF", 0, 100)
    RW = st.slider('RW', 0, 100)
    LAM = st.slider('LAM', 0, 100)
    LCM = st.slider('LCM', 0, 100)
    CM = st.slider('CM', 0, 100)
    RCM = st.slider('RCM', 0, 100)
    RM = st.slider("RM", 0, 100)
    LWB = st.slider('LWB', 0, 100)
    LDM = st.slider('LDM', 0, 100)
    CDM = st.slider('CDM', 0, 100)
    RDM = st.slider('RDM', 0, 100)
    RWB = st.slider('RWB', 0, 100)
    LB = st.slider("LB", 0, 100)
    CAM = st.slider('CAM', 0, 100)
    RAM = st.slider('RAM', 0, 100)
    LM = st.slider("LM", 0, 100)
    LCB = st.slider('LCB', 0, 100)
    CB = st.slider('CB', 0, 100)
    RCB = st.slider('RCB', 0, 100)
    RB = st.slider('RB', 0, 100)
    Crossing = st.slider('Crossing', 0, 100)
    Finishing = st.slider('Finishing', 0, 100)
    HeadingAccuracy = st.slider('HeadingAccuracy', 0, 100)
    ShortPassing = st.slider('ShortPassing', 0, 100)
    Volleys = st.slider('Volleys', 0, 100)
    Dribbling = st.slider("Dribbling", 0, 100)
    Curve = st.slider('Curve', 0, 100)
    FKAccuracy = st.slider('FKAccuracy', 0, 100)
    LongPassing = st.slider('LongPassing', 0, 100)
    BallControl = st.slider('BallControl', 0, 100)
    Reactions = st.slider('Reactions', 0, 100)
    ShotPower = st.slider('ShotPower', 0, 100)
    Strength = st.slider('Strength', 0, 100)
    Aggression = st.slider('Aggression', 0, 100)
    Interceptions = st.slider('Interceptions', 0, 100)
    Positioning = st.slider("Positioning", 0, 100)
    Vision = st.slider('Vision', 0, 100)
    Penalties = st.slider('Penalties', 0, 100)
    Composure = st.slider('Composure', 0, 100)
   
 

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Age,Special,LS,ST,RS,LW,LF,CF,RF,RW,LAM,CAM,RAM,LM,LCM,CM,RCM,RM,LWB,LDM,CDM,RDM,RWB,LB,RB,
        Crossing,Finishing,HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,FKAccuracy,LongPassing,BallControl,Reactions,ShotPower,Strength,Aggression,Interceptions,
        Positioning,Vision,Penalties,Composure)

    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()

# small change
