import argparse

def main():
    parser = argparse.ArgumentParser(description="Lexgen CLI")
    parser.add_argument("--template", help="YAML template to run")
    args = parser.parse_args()
    print("Running agent with template:", args.template)
