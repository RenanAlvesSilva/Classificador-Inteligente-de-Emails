import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def classify_and_respond(email_text:str) -> dict:
    
    try:
        prompt = f""""
            Você é um assistente de IA especialista, trabalhando para uma grande empresa do setor financeiro. Sua única função é analisar emails e classificá-los com precisão para otimizar o fluxo de trabalho da equipe.

            **Contexto do Negócio:**
            - **Emails Produtivos:** São estritamente relacionados a operações financeiras. Eles exigem uma ação da nossa equipe. Exemplos incluem: perguntas sobre o status de um pagamento, solicitação de segunda via de boleto, dúvidas sobre um processo de financiamento, envio de documentos para análise de crédito, questionamentos sobre faturas.
            - **Emails Improdutivos:** São todos os outros. Eles não exigem ação da equipe financeira. Exemplos incluem: mensagens de "Feliz Natal", agradecimentos genéricos, spam, propagandas, perguntas sobre vagas de emprego, ou qualquer assunto não relacionado a finanças.

            **Sua Tarefa:**
            Analise o texto do email abaixo e retorne um JSON com duas chaves:
            1. "classification": Classifique o email como "Produtivo" ou "Improdutivo" com base estrita no contexto de negócio acima.
            2. "suggested_reply": Sugira uma resposta profissional e adequada.

            **Exemplos:**
            - **Email para analisar:** "Prezados, poderiam verificar se o pagamento da fatura do mês passado já foi processado? Obrigado."
            - **Sua resposta JSON:** "classification": "Produtivo", "suggested_reply": "Prezado cliente, obrigado pelo contato. Estamos verificando o status de seu pagamento e retornaremos em breve com a confirmação."
            - **Email para analisar:** "Obrigado pela ajuda de sempre! Vocês são 10!"
            - **Sua resposta JSON:** "classification": "Improdutivo", "suggested_reply": "Agradecemos o seu feedback positivo! Estamos sempre à disposição."

            **REGRAS IMPORTANTES:**
            - Seja rigoroso na classificação. Um email de agradecimento é improdutivo, mesmo que seja educado.
            - Sua resposta deve ser APENAS o objeto JSON, sem nenhum texto ou formatação adicional.
            - Não use ```json``` ou outros delimitadores.
            
            **Email para analisar:** "{email_text}"
        """
        
        response = model.generate_content(prompt)
        print(response)
        generated_text = response.text 
        result = json.loads(generated_text)
        return result
    
    except Exception as e:
        print(f"Erro ao classificar e responder o email: {e}")
        return {
            "classification": "Erro",
            "suggested_reply": "Desculpe, houve um erro ao processar sua solicitação. Por favor, tente novamente mais tarde."
        }
        
