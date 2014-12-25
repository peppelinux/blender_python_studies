# appunti python blender

"""
# lockare la camera
a = bpy.data.screens['Default']
a.areas[2].spaces[0].lock_camera = True
# riconoscere l'oggetto dal tipo (capire a quale area stiamo puntando)
a.areas[2].spaces[0].type
"""

def get_area_spaces(screen_name):
    if isinstance(screen_name, str):
        fstring = ' bpy.data.screens["%s"].areas[%d]'
    else:
        fstring = ' bpy.data.screens[%d].areas[%d]'
    cnt = 0
    for i in bpy.data.screens[screen_name].areas:
        area_path = fstring % (screen_name, cnt)
        print(cnt, i.type, area_path)
        cnt_spaces = 0
        spaces = bpy.data.screens[screen_name].areas[ cnt ].spaces
        for e in spaces:
            print('    %s.spaces[%d] %s' % (area_path, cnt_spaces, spaces[cnt_spaces].type ))
            cnt_spaces += 1
        cnt += 1

def get_screen_list():
    screens = []
    cnt = 0
    for i in bpy.data.screens:
        print(cnt, i.name, ' bpy.data.screens["%s"]' % i.name)
        cnt += 1
        screens.append( i.name )
    print('\n\n')
    return screens

for i in get_screen_list():
    print(i)
    get_area_spaces( i )
    print('\n')



