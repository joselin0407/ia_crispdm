# run_aidav3.py
import os
from dotenv import load_dotenv
load_dotenv()  # Carga tu API Key del archivo .env

import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from my_agent_v3.agent import root_agent

async def main():
    # 🌟 UX MOMENTO 0: Imprimimos el saludo proactivo de inmediato
    os.system('cls' if os.name == 'nt' else 'clear')
    print("═"*75)
    print("  🤖  ¡BIENVENIDO A AIDA V3!  🤖  ")
    print("  Agente de Documentación de Repositorios (CRISP-DM - Estándar IBM)")
    print("═"*75)
    print(" Estoy lista para escanear y documentar carpetas enteras de proyectos.")
    print(" Identificaré tus códigos de proyecto y auditaré cada fase sistemáticamente.")
    print("\n ¿Cómo empezar? Solo dime:")
    print(" 👉 'AIDA, analiza la carpeta repositorio_prueba_ml y genera el reporte Word'")
    print("═"*75 + "\n")

    # Configuración del entorno de ejecución de ADK
    session_service = InMemorySessionService()
    APP_NAME = "aida_app"
    USER_ID = "desarrollador_vanti"
    SESSION_ID = "sesion_actual_1"

    # Creamos la sesión del chat (Con el await solucionado)
    await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    
    # Inicializamos el Runner
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

    # Bucle interactivo con reporte de TOKENS
    while True:
        try:
            user_input = input("[user]: ")
            if user_input.lower() in ["exit", "quit", "salir"]:
                print("\n¡Hasta luego! Cerrando sesión en AIDA V3...")
                break
                
            if not user_input.strip():
                continue
                
            content = types.Content(role="user", parts=[types.Part(text=user_input)])
            
            # Emojis reales corregidos para consolas de Windows/Linux
            print("\n[AIDA]: ⚙️ 🤔 Pensando...", end="\r")
            
            tokens_input = 0
            tokens_output = 0
            tokens_total = 0
            
            # Ejecución del agente
            for event in runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
                
                # Extracción de metadatos de tokens
                if hasattr(event, 'usage_metadata') and event.usage_metadata:
                    tokens_input = getattr(event.usage_metadata, 'prompt_token_count', 0)
                    tokens_output = getattr(event.usage_metadata, 'candidates_token_count', 0)
                    tokens_total = getattr(event.usage_metadata, 'total_token_count', 0)
                
                if event.is_final_response():
                    print(" " * 30, end="\r") 
                    print(f"[AIDA]: {event.content.parts[0].text}\n")
                    
                    # 📊 IMPRIMIMOS EL CONSUMO DE TOKENS EN PANTALLA
                    if tokens_total > 0:
                        print("─"*50)
                        print(" 📊 METADATOS DE CONSUMO DE ESTE TURNO:")
                        print(f"  • Tokens de Entrada (Input):   {tokens_input:,}")
                        print(f"  • Tokens de Salida (Output):  {tokens_output:,}")
                        print(f"  • Tokens Totales Consumidos:   {tokens_total:,}")
                        print("─"*50 + "\n")
                    
        except KeyboardInterrupt:
            print("\n\nSesión finalizada abruptamente. ¡Adiós!")
            break
        except Exception as e:
            print(f"\n[Error de ejecución]: {e}\n")

if __name__ == "__main__":
    asyncio.run(main())

