import pandas as pd 

with open('data.json', 'r') as file:
    data = pd.read_json(file)


md_table = data.to_markdown(index=False)

with open('table.md', 'w') as output:
    output.write(md_table)

