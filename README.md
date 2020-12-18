# About

This project is for rendering blender projects automaticly, with customization options. Thesse customizations are loaded from json file. 

# Author 
Patrik Grinsvall<patrik.grinsvall[]gmail.com>

# Todo
The values and properties that is customized is for now hardcoded, they should be able to locate through a path. This will come.

# Usage
Using external python script:
- blender --background textintro1/textintro1.blend -P customize.py --render-output //render_  -a -- --defaultoptions default_customize.json
  
Using script provided by project, where the script is called "init":
- blender --background textintro1/textintro1.blend --python-text init customize.py --render-output //render_  -a -- --defaultoptions default_customize.json