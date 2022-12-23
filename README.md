# tvb-ext-xircuits

This is a jupyterlab extension built as a prototype for building EBRAINS 
(including TVB simulator, Siibra API) workflows in a visual and interactive manner. It 
extends the already existent [Xircuits](https://xircuits.io/) jupyterlab extension 
by adding new components and new features on top.

For installing in a Jupyter Lab environment:

    pip install tvb-ext-xircuits


For dev mode setup there are 2 alternatives:
1. Using `jlpm`:

    `jlpm` is a JupyterLab-provided, locked version of `yarn` and has a similar usage:

    ```
    conda activate [my-env]
    pip install --upgrade pip
    pip install -e .
    jupyter labextension develop . --overwrite  # Link your development version of the extension with JupyterLab
    jupyter server extension enable tvbextxircuits  # Enable the server extension
    xircuits
    ```

2. Using `yarn`:

    You need to have a dedicated `Python env`, `yarn`, `rust` and `cargo` (from https://rustup.rs/) prepared:
   
    ```
    conda activate [my-env]
    pip install --upgrade pip
    pip install -e .
    yarn install
    yarn install:extension
    xircuits
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

##  Acknowledgments

Copyright (c) 2022 to Xircuits Team See: https://github.com/XpressAI/xircuits

Copyright (c) 2022 to TVB-Xircuits team (SDL Neuroscience Juelich, INS Marseille, Codemart) for changes in this fork.

This extension is build on top of the Xircuits https://xircuits.io Jupyter extension, and it ads custom features, tailored for EBRAINS env.

This project has received funding from the European Union’s Horizon 2020 Framework Programme for Research and Innovation under the Specific Grant Agreement No. 945539 (Human Brain Project SGA3).
