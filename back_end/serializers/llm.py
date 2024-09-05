
from langchain_groq import ChatGroq
from rag.chercher_similartite import fun_chercher_similarite
from rag.chercher_similartite_offres import fun_chercher_similarite_offers
import os
from fastapi import UploadFile,File
from typing import List
from models.user import Message,BusinessPlan


client = ChatGroq(
        model="llama-3.1-70b-versatile",
        api_key="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",
        temperature=0.5 )


def ask_llm_rag(question):
    question_tr = client.invoke(f"Traduire cette question {question} en anglais")
    print(question_tr)
    full_prompt = fun_chercher_similarite(question_tr)
    reponse = client.invoke(full_prompt).content
    print(reponse)
    return reponse

def chat_llm(conversation):
        print(conversation.messages)
        reponse = client.invoke(f"'system:','Répondre à la dérnière question après avoir lu toute la conversation!,répondre directement retourner juste la réponse dirècte' {conversation.messages} " ).content
        print(reponse)
        return reponse

def search_offers(extracted_text):
        
        test_client = ChatGroq(
                model="llama-3.1-70b-versatile",
                api_key="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",
                temperature=0.5 )
        reponse = test_client.invoke("'system:','traduire le cv  en anglais et Essayer de résumer ce cv en extraire les champs neccessaires pour chercher les offres pertinentes pour ce profil, voici le cv'" + extracted_text)
        print(reponse.content)
        offres=fun_chercher_similarite_offers(reponse)
        print(offres)
        return offres
        

def analyseStrategie(businessPlan: BusinessPlan):
        reponse = client.invoke(f"'system:vous êtes un smart analyste expert au domaine de marketing mix, capable d'analyser toutes les stratégies marketing mix, et de citer les points forts et faibles, et des suggestions pour amélioer cette stratégie,en se basant sur les produits/Services réussis dans les années récentes ' ,voici la stratégie: {businessPlan.json()}").content
        print(reponse)
        return reponse