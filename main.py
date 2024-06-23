from fastapi import FastAPI, Query, Response
import google.generativeai as genai
from starlette.responses import JSONResponse

app = FastAPI()


def gemini(question: str):
    genai.configure(api_key='AIzaSyAFAmVIP6l33PQUj5G0Yk05RyH9u42g1gg')
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text


@app.get("/chat")
def chat(question: str):
    return JSONResponse(content={"text": gemini(question)})
