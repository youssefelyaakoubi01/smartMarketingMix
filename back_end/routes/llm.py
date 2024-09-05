from fastapi import APIRouter,UploadFile,File
from serializers.llm import ask_llm_rag,chat_llm,search_offers,analyseStrategie
import io
from PyPDF2 import PdfReader
from models.user import Conversation,Question,BusinessPlan
llm_root = APIRouter()

@llm_root.post('/search_product_rag')
def pose_question(question: Question):
    return ask_llm_rag(question.question)

@llm_root.post('/ask_llm')
def pose_question(conversation: Conversation):
    print(conversation.messages)
    return chat_llm(conversation)

@llm_root.post('/analyseStrategieProduct')
def analyseStrategieProduct(businessPlan: BusinessPlan):
    return analyseStrategie(businessPlan)




