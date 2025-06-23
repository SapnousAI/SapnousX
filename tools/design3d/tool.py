try:
    import bpy
    design3d_available = True
except ImportError:
    design3d_available = False

def create_cube_blender():
    if not design3d_available:
        return 'Blender bpy not available.'
    bpy.ops.mesh.primitive_cube_add()
    return 'Cube created in Blender.'
