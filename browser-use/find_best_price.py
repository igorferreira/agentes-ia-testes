import asyncio
import logging
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from browser_use import Agent
from dotenv import load_dotenv
from browser_use import Agent, Browser, BrowserConfig
from datetime import datetime, timedelta
from pathlib import Path

# Load environment variables
load_dotenv()

# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        #chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: 
        #chrome_instance_path= '/usr/bin/google-chrome'
        #save_recording_path="./recordings/"            
    )
)

# Initialize the model
# gpt-4o is the largest model available
llmOpenAI = ChatOpenAI(model="gpt-4o",temperature=0.0)
llmOllama=ChatOllama(model="deepseek-r1", num_ctx=32000)

llmChoice = llmOpenAI

def setup_logger(log_file='logs/find_best_price.log'):
    log_dir = Path(log_file).parent
    log_dir.mkdir(parents=True, exist_ok=True)
    
    str_format = '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
    log_formatter = logging.Formatter(str_format)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)

    logging.basicConfig(level=logging.INFO, 
                        format=str_format, 
                        handlers=[
                            logging.FileHandler(log_file),
                            console_handler
    ])

async def run_task(tasks, file):
        
    try:
        agent = Agent(
            task=tasks, 
            llm=llmChoice, 
            save_conversation_path= "./conversations/"+file, 
            generate_gif="./execucoes/" + file + ".gif" 
        ) 
        history = await agent.run()    
        result = history.final_result()
        print(result)

        if result:        
            with open("results/"+file + ".txt", "w") as file:
                file.write(result)
        else:
            print('No result')
    finally:
        # Certifique-se de que todos os recursos sejam liberados
        print("Recursos liberados.")


async def execute_tests():
    
    """Execute all tests in sequence."""
    
    orientacao_padrao = """ 
        Gere um Relatório das buscas listando os precos em cada farmacia e qual o preco mais barato.
        Tudo sempre em português.
    """
    
    logging.info("Starting test execution")
    
    try:
        
        logging.info("Buscando o preco mais barato do Xifaxan 550mg 28 comprimidos") 
        await run_task("""
                Acessar os sites das farmácias e buscar o preço do Xifaxan 550mg 28 comprimidos.
                Lista de farmácias: Drogasil, Drogaria São Paulo, Pague Menos, Ultrafarma, Onofre, Droga Raia, Panvel, Drogaria Araujo, Drogaria Venancio, Drogaria Pacheco.
                Encontre outras farmarcias se necessário.
                Busque também em farmácias de João Pessoa que entregam em domicílio se possivel proximo de bairro Jardim Oceania.
                Sempre confirme aceitar cookies e informe se não encontrar o preço.
                Se nao encontrar o preço, informar que nao foi encontrado.
                Se nao encontrar farmacias proximas a Joao Pessoa, informar que nao foi encontrado.
                Listar os preços encontrados, o link de compra e identificar qual é o mais barato.
        """ + orientacao_padrao,
        "tasks_preenchimento_todos_campos_validos")
        await asyncio.sleep(5)  # Wait 2 seconds between tests        
    

    except Exception as e:
        logging.error(f"Test execution failed: {str(e)}")
        raise
    finally:
        logging.info("Test execution completed")
    
if __name__ == '__main__':
    setup_logger()
    asyncio.run(execute_tests())    