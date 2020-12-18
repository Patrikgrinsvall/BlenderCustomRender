#############
##
## This script is ment to be placed inside a blender project. 
## Then default values, listed below, will be replaced with 
## values in specified json file
##
###############
import bpy
import sys
import json
import os 

argv = sys.argv
print(os.path.dirname(os.path.realpath(__file__)))
print(str(sys.argv))

default_project_settings = {
    'PrimaryText'      :   {
        'type'      : 'Text',
        'object'    : 'Text',
        'property'  : 'body',
        'value'     : 'PlaceholderText'
    },
    'BackgroundColor'      :   {
        'type'      : 'Color',
        'object'    : 'Plane',
        'property'  : 'body',
        'value'     : 'PlaceholderText'
    },    
#    'Text1'     :   'PlaceHolderText',
#    'Color1'    :   (.1, .7, 1, 1),
#    'Color2'    :   '#ff0000',
#    'Background':   (0, 0, 0, 1),
#    'Image1'    :   'placeholder.jpg',
#    'Image2'    :   'placeholder.jpg'
}

## Load Default values if json file is specified
if len(sys.argv) > 1 :
    for i, arg in enumerate(sys.argv):
        if arg in ['--defaultjson']:
            print("YEA, we now should load json", sys.argv[i + 1])
            default_project_settings = json.load(open(sys.argv[i + 1]))

## Now check and replace all values from json 
for object in default_project_settings:
    if bpy.context.scene.objects.get(default_project_settings[object]['object']):
        print("Yes, we found object: ", object, 'of with id:', default_project_settings[object]['object'])
        if default_project_settings[object]['type'] == 'Text':
            txt             = bpy.context.scene.objects.get(default_project_settings[object]['object'])
            txt.data.body   = default_project_settings[object]['value']
            pass
        if default_project_settings[object]['type'] == 'Color':
            pass
        if default_project_settings[object]['type'] == 'Image':
            pass
        
#    print(object,"->", default_project_settings[object]['object'], default_project_settings[object]['value'])
#        if(bpy.context.scene.objects.get(object)
#       txt = bpy.context.scene.objects.get("Text")
#if txt:
 #   print("Yes, the object existed")
  #  print(txt.data.body);
#txt = bpy.data.objects['Text']
#txt.data.body = default_properties['Text']
