from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from rag.get_embedding_function_m import get_embedding_function
import time


CHROMA_PATH = "./chroma_consultation"

# Configurer Template Prompt
prompt_template= ChatPromptTemplate.from_messages(
    [
        ("system", "Répondez à cette question  {question}"),
        ("human", "En se basant sur le contexte suivant : {context}")

    ]
)


def fun_chercher_similarite(question: str):
    # Prepare the DB.
    print("\n **************** Début  de péreparation de base de données !'  ******************\n ")
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    print("\n **************** Fin  de péreparation de base de données !'  ******************\n\n ")

    # Search the DB.
    print(" **************** Début  D'opération 'Chercher dans la base de données (ChromaDB) !'  ******************\n ")
    results = db.similarity_search_with_score(question, k=15)
    if len(results) == 0:
        print("Désolé,La réponse de votre question n'existe pas dans la base de donées :( , essayer de poser une autre question!")
    print("**************** Fin  D'opération 'Chercher dans la base de données (ChromaDB) !'  ******************\n ")

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt = prompt_template.format(context=context_text, question=question)
    print(prompt)
    return prompt