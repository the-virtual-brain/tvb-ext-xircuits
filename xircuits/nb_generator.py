import os
import nbformat


class NotebookGenerator(object):

    def __init__(self, notebooks_dir=None):
        if notebooks_dir is None:
            notebooks_dir = 'generated_notebooks'

        if not os.path.exists(notebooks_dir):
            os.mkdir(notebooks_dir)

        self.notebooks_dir = notebooks_dir
        self.notebook = nbformat.v4.new_notebook()

    def add_code_cell(self, code):
        self._add_cell(nbformat.v4.new_code_cell(code))

    def add_markdown_cell(self, text):
        self._add_cell(nbformat.v4.new_markdown_cell(text))

    def _add_cell(self, cell):
        self.notebook['cells'].append(cell)

    def store(self, file_name):
        path = os.path.join(self.notebooks_dir, file_name)

        with open(path, 'w') as f:
            nbformat.write(self.notebook, f)

        return path
