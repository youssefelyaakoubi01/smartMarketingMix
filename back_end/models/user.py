from pydantic import BaseModel,EmailStr
from typing import List,Any

class UserSignup(BaseModel):
    firstName: str 
    lastName: str
    username: EmailStr  
    password: str  
    
class UserLogin(BaseModel):
    username: str 
    password: str

class Offre(BaseModel):
    categorie:str
    description: str

class Message(BaseModel):
    question: str
    answer: Any

class Conversation(BaseModel):
    messages: List[Message]

class Question(BaseModel):
    question: str

class AnalyseProduit(BaseModel):
    type: str
    idee: str
    differentiation: str
    besoins: str

class AnalyseMarche(BaseModel):
    clients_cibles: str
    taille_marche: str
    tendances: str

class StrategiePrix(BaseModel):
    positionnement: str
    strategies: str
    justification: str

class Distribution(BaseModel):
    canaux: str
    logistique: str
    partenariats: str

class Promotion(BaseModel):
    canaux_communication: str
    campagnes: str
    mesure_efficacite: str

class AnalyseSWOT(BaseModel):
    forces: str
    faiblesses: str
    opportunites: str
    menaces: str

class BusinessPlan(BaseModel):
    analyse_produit: AnalyseProduit
    analyse_marche: AnalyseMarche
    strategie_prix: StrategiePrix
    distribution: Distribution
    promotion: Promotion
    analyse_swot: AnalyseSWOT