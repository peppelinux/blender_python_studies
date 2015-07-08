def print_pydata(active_ob):
    """
      active_ob = bpy.context.scene.objects.active
      
      dopo puoi usarlo tipo così :)
      profile_mesh = bpy.data.meshes.new("Base_Profile_Data")
      profile_mesh.from_pydata(Verts, [], [])      
    """
    data = active_ob.data     
    verts = [(round(v.co[0],5),round(v.co[1],5),round(v.co[2],5)) for v in data.vertices]
    edges = [(e.vertices[0],e.vertices[1]) for e in data.edges]
    #faces = [(f.vertices[0],f.vertices[1],f.vertices[2],f.vertices[3]) for f in data.faces]
    print('')
    print(len(verts),'vertices in total')
    print(len(edges),'edges in total')
    #print(len(faces),'faces in total\n')
    #print('from_pydata(',verts,',',edges,',',faces,')', sep='')
    print('from_pydata(',verts,',',edges,',)', sep='')
    return (verts, edges)
