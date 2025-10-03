# Classificador Inteligente de Emails

## Projeto com IA Generativa Google Gemini

Este é um aplicativo web desenvolvido como solução para um desafio técnico, projetado para otimizar a triagem de emails em um ambiente corporativo financeiro. A aplicação utiliza Inteligência Artificial Generativa (Google Gemini) para classificar o conteúdo de emails como "Produtivo" ou "Improdutivo" e sugerir uma resposta apropriada, tudo através de uma interface web interativa e responsiva.



---

### ✨ Funções Principais

* **Classificação via Texto:** Cole o conteúdo de um email diretamente na interface para análise.
* **Upload de Arquivos:** Suporte para envio de emails nos formatos `.txt` e `.pdf` para extração e análise do texto.
* **Integração com IA Generativa:** Utiliza a API do Google Gemini para uma classificação semântica precisa e geração de respostas contextuais.
* **Experiência Dinâmica:** A interface é amigavel e direta.
* **Log de Processamento:** O usuário pode acompanhar em tempo real as etapas do processo de análise no frontend.
* **Arquitetura Limpa:** O código é desacoplado, separando as responsabilidades do backend, dos serviços de extração de texto e da lógica de IA.

---

### 🚀 Tecnologias Utilizadas

* **Backend:** Python 3.11, FastAPI, Uvicorn
* **Frontend:** HTML5, Tailwind CSS (via CDN), JavaScript 
* **Inteligência Artificial:** Google Generative AI (Gemini Pro)
* **Manipulação de PDF:** PyPDF2
* **Gerenciamento de Dependências:** Pip, requirements.txt
* **Deploy:** Railway

---

### ⚙️ Instalação e Execução Local

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

**1. Clone o Repositório:**

git clone [https://github.com/RenanAlvesSilva/teste-treinee.git](https://github.com/RenanAlvesSilva/teste-treinee.git)
cd teste-treinee

**2. Crie e Ative um Ambiente Virtual:**
 Cria o ambiente
python -m venv venv

 Ativa o ambiente (Windows)
.\venv\Scripts\activate

 Ativa o ambiente (macOS/Linux)
source venv/bin/activate

3. Instale as Dependências:
   pip install -r requirements.txt

4. Configure as Variáveis de Ambiente:
A aplicação precisa de uma chave de API para se comunicar com o serviço do Google.

Crie uma cópia do arquivo de exemplo .env.example:

No Windows: copy .env.example .env

No macOS/Linux: cp .env.example .env

Abra o arquivo .env recém-criado e substitua o placeholder pela sua chave de API do Google AI Studio.
GOOGLE_API_KEY="SUA_CHAVE_DE_API_VAI_AQUI"

5. Execute a Aplicação:
uvicorn app.main:app --reload

🔬 Como Testar a Funcionalidade:

1: Teste com Entrada de Texto:
Na caixa de texto, cole um email com teor financeiro (ex: "Gostaria de saber o status do pagamento da fatura de agosto.").
Clique em "Enviar".
Observe o resultado e o log de processamento aparecerem na tela.

2: Teste com Upload de Arquivo:
Deixe a caixa de texto em branco.
clique em "Clique Para Enviar Arquivo"
Use o campo de upload para selecionar um arquivo .txt ou .pdf que contenha um texto de email.
Clique em "Enviar".
O resultado e o log devem ser exibidos da mesma forma.

3:Teste de Conteúdo Improdutivo:
Tente analisar textos como "Feliz Natal para toda a equipe!" ou um poema aleatório. A IA deve classificar corretamente como "Improdutivo".

☁️ Deploy

Esta aplicação foi implantada na plataforma Railway e está disponível publicamente para testes.

🔗 Link da Aplicação: https://verifysmartemail.up.railway.app/

A configuração de deploy inclui um Procfile para instruir a Railway a iniciar o servidor Uvicorn corretamente em um ambiente de produção.
