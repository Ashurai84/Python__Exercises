 import nbformat

# Load the Jupyter notebook
with open('your_notebook.ipynb') as f:
    notebook = nbformat.read(f, as_version=4)

# Extract code cells and save each to a .py file
for i, cell in enumerate(notebook.cells):
    if cell.cell_type == 'code':
        code = cell.source
        with open(f'code_{i + 1}.py', 'w') as code_file:
            code_file.write(code)