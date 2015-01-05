import bpy

bpy.context.user_preferences.system.compute_device_type = 'CUDA'
bpy.ops.wm.addon_disable(module="Zero_Brush")
