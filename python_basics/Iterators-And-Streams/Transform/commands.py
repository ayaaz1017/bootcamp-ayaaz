import typer
import yaml
from processing_functions import *
from stream_functions import *
from stream_adapter_functions import *

app = typer.Typer()

@app.command()
def basic(input_filename: str, output_filename: str = None):
    """Process file by converting lines to uppercase"""
    upper_case(input_filename, output_filename)

@app.command()
def dynamic(input_filename: str, pipeline_file: str):
    """Process file dynamically using the pipeline defined in YAML"""
    with open(pipeline_file, 'r') as f:
        pipeline = yaml.safe_load(f)["pipeline"]
    
    with open(input_filename, 'r') as f:
        records = f.readlines()

    for record in records:
        for func_name in pipeline:
            func = globals().get(func_name)
            if func:
                record = func(record)
        print(record.strip())

@app.command()
def process_stream(input_filename: str, pipeline_file: str):
    """Process file using stream-based pipeline"""
    with open(pipeline_file, 'r') as f:
        pipeline = yaml.safe_load(f)["pipeline"]
    
    with open(input_filename, 'r') as f:
        lines = iter(f.readlines())

    for func_name in pipeline:
        func = globals().get(f"stream_{func_name}")
        if func:
            lines = func(lines)

    for line in lines:
        print(line.strip())

if __name__ == "__main__":
    app()
