from pathlib import Path
import yaml

class Vault():
    def __init__(self,path):
        self.path = Path(path)
        self.notes = [str(p) for p in self.path.rglob('*') if p.is_file() and p.suffix == ".md"]

    def get_note_properties(self):
        pass

class Note():
    def __init__(self,path):
        self.path = path
        self.read_properties()

    def read_properties(self) -> None:
        self.properties = {}
        with open(self.path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Check if the file starts with YAML front matter delimiters
        if content.startswith('---'):
            parts = content.split('---', 2) # Split into [empty, yaml_content, markdown_content]
            if len(parts) > 1:
                yaml_string = parts[1]
                self.properties = yaml.safe_load(yaml_string)
        return None # No YAML front matter found
