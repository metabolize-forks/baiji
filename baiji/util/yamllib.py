def load(path):
    import yaml
    with open(path, 'r') as f:
        return yaml.load(f)
