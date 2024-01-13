import subprocess

def run_command():
    model_path = 'Wizard-Vicuna-13B-Uncensored.gguf' 
    custom_prompt = '"Hikari: Jay is very goodfriend."'

    command = [
        'main',
        '-cml',
        '-r', '"Hikari:"',
        '-r', '"User:","Jay:"',
        '-m', model_path,
        '--temp', '0.6',
        '-c', '2048',
        '-n', '256',
        '--top_p', '0.9',
        '--top_k', '40',
        '--repeat_penalty', '1.0',
        '--ignore-eos',
        '--color',
        '-i',
        '-p', custom_prompt
    ]


    while True:
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error {e.returncode}")
        input("Press Enter to continue...")

if __name__ == "__main__":
    run_command()
