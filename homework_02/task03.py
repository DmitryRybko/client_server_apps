import yaml

data = {
    "list": ['one', 'two', 'three', 'four'],
    "integ": 50,
    "dict": {"key1": "45 руб.", "key2": "60 руб."}
}

with open('file.yaml', 'w', encoding="utf-8") as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False, allow_unicode=True)

with open('file.yaml', encoding="utf-8") as yaml_file:
    print(yaml_file.read())
