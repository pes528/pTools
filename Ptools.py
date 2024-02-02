import subprocess, time, json, re, asyncio
from src.toolphish import banner, ToolPhi

#colors
rojito, roj, fin = "\033[1;33m","\033[1;41m",  "\033[0m"


async def main():
    subprocess.run(["clear"])

    print(
f"""
{banner()}
    {roj} created By 
  telegram: @pes528 {fin}

Herramientas de phishing para Termux

""")
    #search_tool = input("Escribe rep0: ")
    tools = ToolPhi()
    await tools.add_data()
    #tools.get_data()
    page = 2
    while True:
        tools.get_data()
        if tools.get_data() == None:print("Ups llegaste al final");break
        print(rojito+"\nPara clonar un repositorio escribe el numero que tiene asignado cada uno\nPreciona 0 para salir, Enter para continuar viendo."+fin)
        op = input(": ")
        try:
            clone = tools.sites.get(int(op), False)
        except ValueError:
            clone = False
        
        if op != "0":
            if clone != False:
                tool = re.search(r'\/(\w+)$', clone).group(1)
                print(tool)
                mover = lambda: subprocess.run(f"mv {tool} $HOME", shell=True)
                print("CLONANDO REPOSITORIO...")
                time.sleep(2)
                #HOME = "sudo $HOME" if subprocess.run(["uname", "-o"], capture_output=True, text=True).stdout == "GNU/Linux" else "$HOME" 
                #print(HOME)
                subprocess.run(["git", "clone", f"https://github.com/{clone}"])
                time.sleep(2)
                print("\033[1;32mREPOSITORIO CLONADO CON EXITO EN LA CARPETA PRINCIPAL \033[1;0m")
                mover()
                time.sleep(3)
            print("Pagina: ", page)
            await tools.add_data(f"&p={page}")
            tools.get_data()
            
            page += 1
            if tools.get_data() == None:
                print("UPS!! llegaste al final")
                break
            
        
        else:
            break 
    
    #print(tools.sites)
if __name__ == "__main__":
    import subprocess
    
    run = lambda : asyncio.run(main()) if subprocess.run(["ping", "-c", "1", "www.google.com"], capture_output=True) != "ping: unknown host www.google.com" else print("NO TIENES ACCESO A INTERNET")
    run()


