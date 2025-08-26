from fastapi import FastAPI, Request, Form, UploadFile,File
from .services.verify_ai import classify_and_respond
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .services.extract_file_text import extract_text_from_file



app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=templates.TemplateResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/classify")
async def classify_email(request: Request, email_text:str = Form(None), file_upload: UploadFile = File(None)):
    log_messages = []
    email_content = ""
    error_message = None 
    
    if file_upload and file_upload.filename:
        log_messages.append(f"Arquivo recebido: {file_upload.filename}")
        email_content, error_message = await extract_text_from_file(file_upload)
    
        if not error_message and  email_content:
            log_messages.append("AVISO: Texto lido mas não pode ser extraído, verifique se não é uma imagem.")
        elif not error_message and not email_content:
            log_messages.appedend("AVISO: Nenhum texto extraído do arquivo.")
            error_message = "Não foi possível extrair o texto do PDF, verifique se não é uma imagem."
        elif error_message:
            log_messages.append(f"Erro ao extrair texto do arquivo: {error_message}")
    elif email_text:
        log_messages.append("Texto do email recebido via formulário.")
        email_content = email_text
    
    else:
        error_message = "Por favor, cole o texto ou envie um arquivo para análise."
    
    context = {
        "request": request,
        "email_text": email_text,
        
    }   
    
    if error_message:
        log_messages.append(f"Processo Interrompido, Motivo: {error_message}")
        context["error"] = error_message
    
    elif email_content:
        result = classify_and_respond(email_content)
        context.update({
            "classification": result.get("classification"),
            "suggested_reply": result.get("suggested_reply"),
            "error": result.get("error")
        })    
    context["log_messages"] = log_messages
    print(log_messages)
    return templates.TemplateResponse("index.html", context)