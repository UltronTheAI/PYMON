import typer, subprocess, colorama, os

colorama.init()
app = typer.Typer()

@app.command()
def run(file):
    try:
        try:
            f = open('check.ch', 'w')
            f.write('running')
            f.close()
        except:
            os.system('cd.> check.ch')
            f = open('check.ch', 'w')
            f.write('running')
            f.close()
        f = open(file, 'r')
        fr = f.read()
        f.close()
        repet = fr
        print(colorama.Fore.GREEN + '############# RUNING ' + file.replace('.py', '') + ' ############# ' + colorama.Fore.YELLOW)
        python_app = subprocess.Popen(['python', file])
        while True:
            f = open('check.ch', 'r')
            fr = f.read()
            f.close()
            # time.sleep(0)
            if 'stop' in fr:
                f = open('check.ch', 'w')
                f.write('stop')
                f.close()
                os.system('del check.ch') 
                print(colorama.Fore.GREEN + '############# STOP ' + file.replace('.py', '') + ' ############# ' + colorama.Fore.YELLOW) 
                break
            else: pass
            # time.sleep(0.1)
            f = open(file, 'r')
            text = f.read()
            f.close()
            if repet != text: 
                print(colorama.Fore.GREEN + '############# RE-RUNING ' + file.replace('.py', '') + ' ############# ' + colorama.Fore.YELLOW)
                python_app.terminate()
                python_app = subprocess.Popen(['python', file])
                repet = text
    except:
        f = open('check.ch', 'w')
        f.write('stop')
        f.close()
        os.system('del check.ch') 
        print(colorama.Fore.GREEN + '############# STOP ' + file.replace('.py', '') + ' ############# ' + colorama.Fore.YELLOW) 
        

@app.command()
def stop():
    f = open('check.ch', 'w')
    f.write('stop')
    f.close()

if __name__ == '__main__':
    app()
    
