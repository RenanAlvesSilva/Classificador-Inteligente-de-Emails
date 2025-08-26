from PyPDF2 import PdfReader
from fastapi import UploadFile 
import io


async def extract_text_from_file(file: UploadFile) -> tuple[str, str | None]:
    
    content = ""
    error = None
    
    try:
        if not file or not file.filename:
            return "Nenhum arquivo enviado."
        
        file_bytes = await file.read()
        
        if file.filename.endswith('.txt'):
            content = file_bytes.decode('utf-8')
        elif file.filename.endswith('.pdf'):
            reader = PdfReader(io.BytesIO(file_bytes))
            full_text = ""
            for page in reader.pages:
                full_text += page.extract_text() or ""
            content = full_text
        else:
            return "", "Tipo de arquivo não suportado. Por favor, envie um arquivo .txt ou .pdf."
    except Exception as e:
        error = f"Erro ao processar o arquivo: {e}"
    
    return content, error
   