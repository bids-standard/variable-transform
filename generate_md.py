from pathlib import Path
import pandas as pd
import json
from rich import print

def print_this_test(this_test, input_, output_, transform_, f):

    print(f'\n\n## {this_test.name.replace("_", " ")}', file=f)

    print_table("\n### input\n", f, input_)

    print(f"\n### transformation \n", file=f)
    print("```json", file=f)
    with open(transform_, "r") as t:
        print(json.dumps(json.load(t), indent=4), file=f)
    print("```", file=f)

    print_table("\n### output \n", f, output_)    


def print_table(header, f, table_file):
    print(f"{header}", file=f)
    result = pd.read_csv(table_file, sep="\t")
    print(result.to_markdown(index=False), file=f)
    return result    


def to_markdown(dir):

    transformation_list = pd.read_csv(
        Path().joinpath("transformation_list.tsv"), sep="\t"
    ).sort_values('name')

    transformations = transformation_list[transformation_list["type"] == dir].drop(columns=["type"])

    input_dir = Path("spec").joinpath(dir)

    print(f"\n\n[blue]Listing\n{input_dir}[/blue]")

    output_file = Path("spec").joinpath(f"{dir}.md")

    with open(output_file, "w+") as f:

        print(f"# {dir.upper()} transformations\n", file=f)
        print(transformations.to_markdown(index=False), file=f)

        for this_test in input_dir.iterdir():

            print(f"{this_test}")

            if this_test.is_dir():

                input_ = this_test.joinpath("input.tsv")
                if not input_.exists():
                    print(f"[red] input.tsv missing for {this_test}[/red]")
                    continue
                output_ = this_test.joinpath("output.tsv")
                if not output_.exists():
                    print(f"[red]  output.tsv missing for {this_test}[/red]")
                    continue   
                transform_ = this_test.joinpath("transformation.json")
                if not transform_.exists():
                    print(f"[red] tranform.json missing for {this_test}[/red]")
                    continue                               

                print(f'\n\n## {this_test.name.replace("_", " ")}', file=f)

                print(f"\n### input\n", file=f)

                df = pd.read_csv(input_, sep="\t")
                print(df.to_markdown(index=False), file=f)

                print(f"\n### transformation \n", file=f)

                print("```json", file=f)
                with open(transform_, "r") as t:
                    print(json.dumps(json.load(t), indent=4), file=f)
                print("```", file=f)

                print(f"\n### output \n", file=f)

                df = pd.read_csv(output_, sep="\t")
                print(df.to_markdown(index=False), file=f)


def main():

    to_markdown("compute")
    to_markdown("munge")


if __name__ == "__main__":
    main()
