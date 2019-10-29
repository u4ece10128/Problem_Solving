files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}


result = {}

for k, v in files.items():
    result.setdefault(v, []).append(k)

print result