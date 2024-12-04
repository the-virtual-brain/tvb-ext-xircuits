<p>
    <img src="style/icons/TVB_logo.svg" alt="TVB logo" title="TVB" height="100" style="padding: 15px"/>
    <img src="style/icons/VBT_logo.svg" alt="VBT logo" title="VBT" height="100"  />
</p>

# tvb-ext-xircuits

This is a jupyterlab extension built as a prototype for building EBRAINS 
(including TVB simulator, Siibra API) workflows in a visual and interactive manner. It 
extends the already existent [Xircuits](https://xircuits.io/) jupyterlab extension 
by adding new components and new features on top.

Starting with version 2.0.0, tvb-ext-xircuits can be installed in **lightweight** mode or in **full** mode.

**Full** mode means that the extension will be fully working and able to run workflows.

**Lightweight** mode means that only the front-end part of the extension will be available, meaning that the users will 
be able to see all the extension's components, but running workflows will not work.

To install the extension locally and in full mode (recommended):

    pip install tvb-ext-xircuits[full]


To install the extension in lightweight mode (only for specialized users):

    pip install tvb-ext-xircuits


For dev mode setup there are 2 alternatives:
1. Using `jlpm`:

    `jlpm` is a JupyterLab-provided, locked version of `yarn` and has a similar usage:

    ```
    conda activate [my-env]
    pip install --upgrade pip
    pip install -e .[full]
    jupyter labextension develop . --overwrite  # Link your development version of the extension with JupyterLab
    jupyter server extension enable tvbextxircuits  # Enable the server extension
    tvbextxircuits
    ```

2. Using `yarn`:

    You need to have a dedicated `Python env`, `yarn`, `rust` and `cargo` (from https://rustup.rs/) prepared:
   
    ```
    conda activate [my-env]
    pip install --upgrade pip
    pip install -e .[full]
    yarn install
    yarn install:extension
    tvbextxircuits
    ```
    
To rebuild the extension after making changes to it:

      # Rebuild Typescript source after making changes
      jlpm build
      # Rebuild extension after making any changes
      jupyter lab build

To rebuild automatically:

      # Watch the source directory in another terminal tab
      jlpm run watch
      # Run Xircuits in watch mode in one terminal tab
      jupyter lab --watch

##  Notes
To be able to see details info related to TVB components you must first run the command `python generate_description_files.py`

Notebooks generated can be found at `TVB_generated_notebooks/<xircuits_id>`

##  Acknowledgments

Copyright (c) 2022-2024 to Xircuits Team See: https://github.com/XpressAI/xircuits

Copyright (c) 2022-2023 to TVB-Xircuits team (SDL Neuroscience Juelich, INS Marseille, Codemart) for changes in this fork.

Copyright (c) 2024 to Codemart - Brainiacs team for further changes in this fork.

This extension is build on top of the Xircuits https://xircuits.io Jupyter extension, and it adds custom features, tailored for EBRAINS env.

This project has received funding from the European Union’s Horizon 2020 Framework Programme for Research and Innovation under the Specific Grant Agreement No. 945539 (Human Brain Project SGA3).

This project has received funding from the European Union’s Horizon Europe Programme under the Specific Grant Agreement No. 101147319 (EBRAINS 2.0 Project).

This project has received funding from the European Union’s Research and Innovation Program Horizon Europe under Grant Agreement No. 101137289 (Virtual Brain Twin Project).
