import os
import asyncio
import logging
from datetime import datetime, timedelta
from pathlib import Path
from pydantic import SecretStr
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from browser_use import Agent, Browser, BrowserConfig
from browser_use.browser.context import BrowserContextConfig, BrowserContext

# Load environment variables
load_dotenv()

browser_context_config = BrowserContextConfig(
    cookies_file="cookies.json",
    wait_for_network_idle_page_load_time=10.0,
    browser_window_size={'width': 1920, 'height': 540},  # Full width, half height
    locale='pt-BR',
    user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    highlight_elements=True,
    viewport_expansion=500,
    allowed_domains=[],
    save_recording_path='./recordings',
    save_downloads_path='./downloads',
    trace_path='./traces',
    disable_security=False    
)

browser_config = BrowserConfig(
                    headless=False,
                    disable_security=False,
                    chrome_instance_path='/usr/bin/google-chrome'
)


# Initialize the model
# gpt-4o is the largest model available
#llm = ChatOpenAI(model="gpt-4o",temperature=0.0)
#llm = ChatOllama(model="deepseek-r1", num_ctx=32000)
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv("GEMINI_API_KEY")))

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
    return logging

logger = setup_logger()

async def run_task(tasks, file):

    initial_actions_form_agent = [	
        {'open_tab': {'url': 'http://www.google.com'}},
    ]

    try:

        # Configure the browser to connect to your Chrome instance
        browser = Browser(
            config=browser_config
        )
        context = BrowserContext(browser=browser, config=browser_context_config)
        
        agent = Agent(
            initial_actions=initial_actions_form_agent,
            browser_context=context,
            task=tasks,
            llm=llm,
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
    
    logger.info("Starting test execution")
    
    try:
        
        logger.info("Buscando o preco mais barato do Xifaxan 550mg 28 comprimidos") 
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
        logger.error(f"Test execution failed: {str(e)}")
        raise
    finally:
        logger.info("Test execution completed")
    
if __name__ == '__main__':
    setup_logger()
    asyncio.run(execute_tests())    