import bpy
import bpy_extras
from mathutils import Matrix
from mathutils import Vector
import random


HEMI_SPHERE = [[0.0000, 0.2731, 1.1076],[0.0000, 0.5358, 1.0279],[0.0000, 0.7778, 0.8985],[0.0000, 0.9899, 0.7244],[0.0000, 1.1641, 0.5123],[0.0000, 1.2934, 0.2702],[0.0000, 1.3731, 0.0076],[0.0533, 0.2679, 1.1076],[0.1045, 0.5255, 1.0279],[0.1517, 0.7629, 0.8985],[0.1931, 0.9709, 0.7244],[0.2271, 1.1417, 0.5123],[0.2523, 1.2686, 0.2702],[0.2679, 1.3467, 0.0076],[0.1045, 0.2523, 1.1076],[0.2050, 0.4950, 1.0279],[0.2977, 0.7186, 0.8985],[0.3788, 0.9146, 0.7244],[0.4455, 1.0754, 0.5123],[0.4950, 1.1950, 0.2702],[0.5255, 1.2686, 0.0076],[0.1517, 0.2271, 1.1076],[0.2977, 0.4455, 1.0279],[0.4321, 0.6467, 0.8985],[0.5500, 0.8231, 0.7244],[0.6467, 0.9679, 0.5123],[0.7186, 1.0754, 0.2702],[0.7629, 1.1417, 0.0076],[0.1931, 0.1931, 1.1076],[0.3788, 0.3788, 1.0279],[0.5500, 0.5500, 0.8985],[0.1517, 0.2271, 1.1076],[0.2977, 0.4455, 1.0279],[0.4321, 0.6467, 0.8985],[0.5500, 0.8231, 0.7244],[0.6467, 0.9679, 0.5123],[0.7186, 1.0754, 0.2702],[0.7629, 1.1417, 0.0076],[0.1931, 0.1931, 1.1076],[0.3788, 0.3788, 1.0279],[0.5500, 0.5500, 0.8985],[0.4950, 0.2050, 1.0279],[0.7186, 0.2977, 0.8985],[0.9146, 0.3788, 0.7244],[1.0754, 0.4455, 0.5123],[1.1950, 0.4950, 0.2702],[1.2686, 0.5255, 0.0076],[0.2679, 0.0533, 1.1076],[0.5255, 0.1045, 1.0279],[0.7629, 0.1517, 0.8985],[0.9709, 0.1931, 0.7244],[1.1417, 0.2271, 0.5123],[1.2686, 0.2523, 0.2702],[1.3467, 0.2679, 0.0076],[0.2731, -0.0000, 1.1076],[0.5358, -0.0000, 1.0279],[0.7778, -0.0000, 0.8985],[0.9899, -0.0000, 0.7244],[1.1641, -0.0000, 0.5123],[1.2934, -0.0000, 0.2702],[1.3731, -0.0000, 0.0076],[0.2679, -0.0533, 1.1076],[0.5255, -0.1045, 1.0279],[0.7629, -0.1517, 0.8985],[0.9709, -0.1931, 0.7244],[1.1417, -0.2271, 0.5123],[1.2686, -0.2523, 0.2702],[1.3467, -0.2679, 0.0076],[0.2523, -0.1045, 1.1076],[0.4950, -0.2050, 1.0279],[0.7186, -0.2977, 0.8985],[0.9146, -0.3788, 0.7244],[1.0754, -0.4455, 0.5123],[1.1950, -0.4950, 0.2702],[1.2686, -0.5255, 0.0076],[0.2271, -0.1517, 1.1076],[0.4455, -0.2977, 1.0279],[0.6467, -0.4321, 0.8985],[0.8231, -0.5500, 0.7244],[0.9679, -0.6467, 0.5123],[1.0754, -0.7186, 0.2702],[1.1417, -0.7629, 0.0076],[0.1931, -0.1931, 1.1076],[0.3788, -0.3788, 1.0279],[0.5500, -0.5500, 0.8985],[0.7000, -0.7000, 0.7244],[0.8231, -0.8231, 0.5123],[0.9146, -0.9146, 0.2702],[0.9709, -0.9709, 0.0076],[0.1517, -0.2271, 1.1076],[0.2977, -0.4455, 1.0279],[0.4321, -0.6467, 0.8985],[0.5500, -0.8231, 0.7244],[0.6467, -0.9679, 0.5123],[0.7186, -1.0754, 0.2702],[0.7629, -1.1417, 0.0076],[0.8231, -0.8231, 0.5123],[0.9146, -0.9146, 0.2702],[0.9709, -0.9709, 0.0076],[0.1517, -0.2271, 1.1076],[0.2977, -0.4455, 1.0279],[0.4321, -0.6467, 0.8985],[0.5500, -0.8231, 0.7244],[0.6467, -0.9679, 0.5123],[0.7186, -1.0754, 0.2702],[0.7629, -1.1417, 0.0076],[0.8231, -0.8231, 0.5123],[0.9146, -0.9146, 0.2702],[0.9709, -0.9709, 0.0076],[0.1517, -0.2271, 1.1076],[0.2977, -0.4455, 1.0279],[0.4321, -0.6467, 0.8985],[0.5500, -0.8231, 0.7244],[0.6467, -0.9679, 0.5123],[0.7186, -1.0754, 0.2702],[0.7629, -1.1417, 0.0076],[-0.1517, -0.7629, 0.8985],[-0.1931, -0.9709, 0.7244],[-0.2271, -1.1417, 0.5123],[-0.2523, -1.2686, 0.2702],[-0.2679, -1.3467, 0.0076],[-0.1045, -0.2523, 1.1076],[-0.2050, -0.4950, 1.0279],[-0.2977, -0.7186, 0.8985],[-0.3788, -0.9146, 0.7244],[-0.4455, -1.0754, 0.5123],[-0.4950, -1.1950, 0.2702],[-0.5255, -1.2686, 0.0076],[-0.1517, -0.2271, 1.1076],[-0.2977, -0.4455, 1.0279],[-0.4321, -0.6467, 0.8985],[-0.5500, -0.8231, 0.7244],[-0.6467, -0.9679, 0.5123],[-0.7186, -1.0754, 0.2702],[-0.7629, -1.1417, 0.0076],[-0.0000, -0.0000, 1.1345],[-0.1931, -0.1931, 1.1076],[-0.3788, -0.3788, 1.0279],[-0.4950, -1.1950, 0.2702],[-0.5255, -1.2686, 0.0076],[-0.1517, -0.2271, 1.1076],[-0.2977, -0.4455, 1.0279],[-0.4321, -0.6467, 0.8985],[-0.5500, -0.8231, 0.7244],[-0.6467, -0.9679, 0.5123],[-0.7186, -1.0754, 0.2702],[-0.7629, -1.1417, 0.0076],[-0.0000, -0.0000, 1.1345],[-0.1931, -0.1931, 1.1076],[-0.3788, -0.3788, 1.0279],[-0.4950, -0.2050, 1.0279],[-0.7186, -0.2977, 0.8985],[-0.9146, -0.3788, 0.7244],[-1.0754, -0.4455, 0.5123],[-1.1950, -0.4950, 0.2702],[-1.2686, -0.5255, 0.0076],[-0.2679, -0.0533, 1.1076],[-0.5255, -0.1045, 1.0279],[-0.7629, -0.1517, 0.8985],[-0.9709, -0.1931, 0.7244],[-1.1417, -0.2271, 0.5123],[-1.2686, -0.2523, 0.2702],[-1.3467, -0.2679, 0.0076],[-0.2731, -0.0000, 1.1076],[-0.5358, -0.0000, 1.0279],[-0.7778, -0.0000, 0.8985],[-0.9899, -0.0000, 0.7244],[-1.1641, -0.0000, 0.5123],[-1.2934, -0.0000, 0.2702],[-1.3731, -0.0000, 0.0076],[-0.2679, 0.0533, 1.1076],[-0.5255, 0.1045, 1.0279],[-0.7629, 0.1517, 0.8985],[-0.9709, 0.1931, 0.7244],[-1.1417, 0.2271, 0.5123],[-1.2686, 0.2523, 0.2702],[-1.3467, 0.2679, 0.0076],[-0.2523, 0.1045, 1.1076],[-0.4950, 0.2050, 1.0279],[-0.7186, 0.2977, 0.8985],[-0.9146, 0.3788, 0.7244],[-1.0754, 0.4455, 0.5123],[-1.1950, 0.4950, 0.2702],[-1.2686, 0.5255, 0.0076],[-0.2271, 0.1517, 1.1076],[-0.4455, 0.2977, 1.0279],[-0.6467, 0.4321, 0.8985],[-0.8231, 0.5500, 0.7244],[-0.9679, 0.6467, 0.5123],[-1.0754, 0.7186, 0.2702],[-1.1417, 0.7629, 0.0076],[-0.1931, 0.1931, 1.1076],[-0.3788, 0.3788, 1.0279],[-0.5500, 0.5500, 0.8985],[-0.7000, 0.7000, 0.7244],[-0.8231, 0.8231, 0.5123],[-0.9146, 0.9146, 0.2702],[-0.9709, 0.9709, 0.0076],[-0.1517, 0.2271, 1.1076],[-0.2977, 0.4455, 1.0279],[-0.4321, 0.6467, 0.8985],[-0.5500, 0.8231, 0.7244],[-0.6467, 0.9679, 0.5123],[-0.7186, 1.0754, 0.2702],[-0.7629, 1.1417, 0.0076],[-0.1045, 0.2523, 1.1076],[-0.2050, 0.4950, 1.0279],[-0.2977, 0.7186, 0.8985],[-0.3788, 0.9146, 0.7244],[-0.4455, 1.0754, 0.5123],[-0.4950, 1.1950, 0.2702],[-0.5255, 1.2686, 0.0076],[-0.0533, 0.2679, 1.1076],[-0.1045, 0.5255, 1.0279],[-0.1517, 0.7629, 0.8985],[-0.1931, 0.9709, 0.7244],[-0.2271, 1.1417, 0.5123],[-0.2523, 1.2686, 0.2702],[-0.2679, 1.3467, 0.0076]]

#---------------------------------------------------------------
# 3x4 P matrix from Blender camera
#---------------------------------------------------------------

# Build intrinsic camera parameters from Blender camera data
#
# See notes on this in 
# blender.stackexchange.com/questions/15102/what-is-blenders-camera-projection-matrix-model

def get_calibration_matrix_K_from_blender(camd):
    f_in_mm = camd.lens
    scene = bpy.context.scene
    resolution_x_in_px = scene.render.resolution_x
    resolution_y_in_px = scene.render.resolution_y
    scale = scene.render.resolution_percentage / 100
    sensor_width_in_mm = camd.sensor_width
    sensor_height_in_mm = camd.sensor_height
    pixel_aspect_ratio = scene.render.pixel_aspect_x / scene.render.pixel_aspect_y
    if (camd.sensor_fit == 'VERTICAL'):
        # the sensor height is fixed (sensor fit is horizontal), 
        # the sensor width is effectively changed with the pixel aspect ratio
        s_u = resolution_x_in_px * scale / sensor_width_in_mm / pixel_aspect_ratio 
        s_v = resolution_y_in_px * scale / sensor_height_in_mm
    else: # 'HORIZONTAL' and 'AUTO'
        # the sensor width is fixed (sensor fit is horizontal), 
        # the sensor height is effectively changed with the pixel aspect ratio
        pixel_aspect_ratio = scene.render.pixel_aspect_x / scene.render.pixel_aspect_y
        s_u = resolution_x_in_px * scale / sensor_width_in_mm
        s_v = resolution_y_in_px * scale * pixel_aspect_ratio / sensor_height_in_mm
    # Parameters of intrinsic calibration matrix K
    alpha_u = f_in_mm * s_u
    alpha_v = f_in_mm * s_v
    u_0 = resolution_x_in_px * scale / 2
    v_0 = resolution_y_in_px * scale / 2
    skew = 0 # only use rectangular pixels
    K = Matrix(
        ((alpha_u, skew,    u_0),
        (   0  , alpha_v, v_0),
        (   0  , 0,     1 )))
    return K


def get_3x4_RT_matrix_from_blender(cam):
    # bcam stands for blender camera
    R_bcam2cv = Matrix(
        ((1, 0,  0),
         (0, -1, 0),
         (0, 0, -1)))
    # Transpose since the rotation is object rotation, 
    # and we want coordinate rotation
    # R_world2bcam = cam.rotation_euler.to_matrix().transposed()
    # T_world2bcam = -1*R_world2bcam * location
    #
    # Use matrix_world instead to account for all constraints
    location, rotation = cam.matrix_world.decompose()[0:2]
    R_world2bcam = rotation.to_matrix().transposed()
    # Convert camera location to translation vector used in coordinate changes
    # T_world2bcam = -1*R_world2bcam*cam.location
    # Use location from matrix_world to account for constraints:     
    T_world2bcam = -1*R_world2bcam @ location
    # Build the coordinate transform matrix from world to computer vision camera
    # NOTE: Use * instead of @ here for older versions of Blender
    # TODO: detect Blender version
    R_world2cv = R_bcam2cv@R_world2bcam
    T_world2cv = R_bcam2cv@T_world2bcam
    # put into 3x4 matrix
    RT = Matrix((
        R_world2cv[0][:] + (T_world2cv[0],),
        R_world2cv[1][:] + (T_world2cv[1],),
        R_world2cv[2][:] + (T_world2cv[2],)
         ))
    return RT

def get_3x4_P_matrix_from_blender(cam):
    K = get_calibration_matrix_K_from_blender(cam.data)
    RT = get_3x4_RT_matrix_from_blender(cam)
    return K, K, RT

# ----------------------------------------------------------
# Alternate 3D coordinates to 2D pixel coordinate projection code
# adapted from https://blender.stackexchange.com/questions/882/how-to-find-image-coordinates-of-the-rendered-vertex?lq=1
# to have the y axes pointing up and origin at the top-left corner
def project_by_object_utils(cam, point):
    scene = bpy.context.scene
    co_2d = bpy_extras.object_utils.world_to_camera_view(scene, cam, point)
    render_scale = scene.render.resolution_percentage / 100
    render_size = (
            int(scene.render.resolution_x * render_scale),
            int(scene.render.resolution_y * render_scale),
            )
    return Vector((co_2d.x * render_size[0], render_size[1] - co_2d.y * render_size[1]))

def sample_hemisphere():
    # hemi_sphere = bpy.data.objects['Sphere']
    # indx = random.randint(0, len(hemi_sphere.data.vertices))
    # v = hemi_sphere.data.vertices[indx]
    # co_final = hemi_sphere.matrix_world @ v.co
    # return co_final
    indx = random.randint(0, len(hemi_sphere.data.vertices))


# ----------------------------------------------------------

cam = bpy.data.objects['Camera']

sample_loc = sample_hemisphere()
cam.location = sample_loc

K = get_calibration_matrix_K_from_blender(cam.data)
RT = get_3x4_RT_matrix_from_blender(cam)
print(K)
print(RT)
