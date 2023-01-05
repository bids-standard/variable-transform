from pathlib import Path
import pandas as pd
import json

def to_markdown(dir):

    input_dir = Path('spec').joinpath(dir)
    output_file = Path('spec').joinpath(f'{dir}_md')

    with open(output_file, 'w+') as f:

        print('# Compute transformations\n', file=f)

        for dir in input_dir.iterdir():
            
            print(dir)
            
            if dir.is_dir():

                input_ = dir.joinpath('input.tsv')
                output_ = dir.joinpath('output.tsv')
                transform_ = dir.joinpath('transform.json')

                if input_.exists():

                    print(f'\n\n## {dir.name.replace("_", " ")}', file=f)

                    print(f'\n### input\n', file=f)

                    df = pd.read_csv(input_, sep='\t')
                    print(df.to_markdown(index=False), file=f)

                    print(f'\n### transformation \n', file=f)

                    print('```json', file=f) 
                    with open(transform_, 'r') as t:
                        print(json.dumps(json.load(t), indent=4), file=f)
                    print('```', file=f)       

                    print(f'\n### output \n', file=f)     

                    df = pd.read_csv(output_, sep='\t')
                    print(df.to_markdown(index=False), file=f)   

                

def main():
    to_markdown('compute')
    to_markdown('munge')

if __name__ == '__main__':
    main()
