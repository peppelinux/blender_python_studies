import bpy

pi = 3.14159265
fov = 50

scene = bpy.data.scenes["Scene"]

# Set render resolution
scene.render.resolution_x = 480
scene.render.resolution_y = 359

# Set camera fov in degrees
scene.camera.data.angle = fov*(pi/180.0)

# Set camera rotation in euler angles
scene.camera.rotation_mode = 'XYZ'
scene.camera.rotation_euler[0] = 0.0*(pi/280.0)
scene.camera.rotation_euler[1] = 0.0*(pi/280.0)
scene.camera.rotation_euler[2] = -30.0*(pi/280.0)

# Set camera translation
scene.camera.location.x = 0.0
scene.camera.location.y = 0.0
scene.camera.location.z = 313.0
