# BPY (Blender as a python) [pip3 install bpy]
import bpy
# System (Default)
import sys

"""
Description:
    Initialization of constants.
"""
CONST_RESET_ENV = True
# End-Effectors:
#   ABB:
#       [ABB_Smart_Gripper_L_Type_1_001, ABB_Smart_Gripper_L_Type_2_001,
#        ABB_Smart_Gripper_R_Type_1_001, ABB_Smart_Gripper_R_Type_2_001]
#   SMC (MHM)
#       [EE_SMC_MHM_ABB_IRB_120_001, EE_SMC_MHM_Universal_Robots_UR3_001]
#   SMC (XT661_2A)
#       [EE_SMC_XT661_2A_ABB_IRB_120_001, EE_SMC_XT661_2A_Universal_Robots_UR3_001]
#   SMC (XT661_4C)
#       [EE_SMC_XT661_4C_ABB_IRB_120_001, EE_SMC_XT661_4C_Universal_Robots_UR3_001]
#   SMC (ZP2)
#       [EE_SMC_ZP2_ABB_IRB_120_001, EE_SMC_ZP2_Universal_Robots_UR3_001]
#   Intel Realsense (D434i)
#       [EE_Intel_Camera_HT_Circular_001, EE_Intel_Camera_HT_Square_001]
CONST_EE_NAME = 'ABB_Smart_Gripper_R_Type_1_001'

def Reset_Environment():
    """
    Description:
        Restore the environment to the default position.
    """
                
    bpy.data.objects['Viewpoint'].location = [0.0, 0.0, 0.0]
    bpy.data.objects['Viewpoint'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
        
    # Move the end-effectors to the default position.
    #   ABB:
    bpy.data.objects['ABB_Smart_Gripper_L_Type_1_001'].location = [0.2, -0.4, 0.0]
    bpy.data.objects['ABB_Smart_Gripper_L_Type_1_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    bpy.data.objects['ABB_Smart_Gripper_L_Type_2_001'].location = [0.2, 0.4, 0.0]
    bpy.data.objects['ABB_Smart_Gripper_L_Type_2_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    bpy.data.objects['ABB_Smart_Gripper_R_Type_1_001'].location = [0.2, -0.2, 0.0]
    bpy.data.objects['ABB_Smart_Gripper_R_Type_1_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    bpy.data.objects['ABB_Smart_Gripper_R_Type_2_001'].location = [0.2, 0.2, 0.0]
    bpy.data.objects['ABB_Smart_Gripper_R_Type_2_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    #   SMC (MHM)
    bpy.data.objects['EE_SMC_MHM_ABB_IRB_120_001'].location = [-0.2, 0.2, 0.0]
    bpy.data.objects['EE_SMC_MHM_ABB_IRB_120_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    bpy.data.objects['EE_SMC_MHM_Universal_Robots_UR3_001'].location = [-0.2, 0.4, 0.0]
    bpy.data.objects['EE_SMC_MHM_Universal_Robots_UR3_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    #   SMC (XT661_2A)
    bpy.data.objects['EE_SMC_XT661_2A_ABB_IRB_120_001'].location = [0.0, -0.2, 0.0]
    bpy.data.objects['EE_SMC_XT661_2A_ABB_IRB_120_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    bpy.data.objects['EE_SMC_XT661_2A_Universal_Robots_UR3_001'].location = [0.0, -0.4, 0.0]
    bpy.data.objects['EE_SMC_XT661_2A_Universal_Robots_UR3_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    #   SMC (XT661_4C)
    bpy.data.objects['EE_SMC_XT661_4C_ABB_IRB_120_001'].location = [-0.2, -0.2, 0.0]
    bpy.data.objects['EE_SMC_XT661_4C_ABB_IRB_120_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    bpy.data.objects['EE_SMC_XT661_4C_Universal_Robots_UR3_001'].location = [-0.2, -0.4, 0.0]
    bpy.data.objects['EE_SMC_XT661_4C_Universal_Robots_UR3_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    #   SMC (ZP2)
    bpy.data.objects['EE_SMC_ZP2_ABB_IRB_120_001'].location = [0.0, 0.2, 0.0]
    bpy.data.objects['EE_SMC_ZP2_ABB_IRB_120_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    bpy.data.objects['EE_SMC_ZP2_Universal_Robots_UR3_001'].location = [0.0, 0.4, 0.0]
    bpy.data.objects['EE_SMC_ZP2_Universal_Robots_UR3_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    #   Intel Realsense (D434i)
    bpy.data.objects['EE_Intel_Camera_HT_Circular_001'].location = [-0.2, 0.0, 0.0]
    bpy.data.objects['EE_Intel_Camera_HT_Circular_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    bpy.data.objects['EE_Intel_Camera_HT_Square_001'].location = [0.2, 0.0, 0.0]
    bpy.data.objects['EE_Intel_Camera_HT_Square_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]

def Duplicate_Object(name: str, identification: str):
    """
    Description:
        Duplication of objects and/or object hierarchy (if exists).
        
    Args:
        (1) name [string]: Name of the main object.
        (2) identification [string]: Identification of the name of the new object.
                                     (name + '_' + identification)
    """
    
    # Select the main object and/or object hierarchy.
    bpy.data.objects[name].select_set(True)
    if bpy.data.objects[name].children:
        # If the object has children(s).
        for obj in bpy.data.objects[name].children:        
            bpy.data.objects[obj.name].select_set(True)
    # Duplicate the selected object(s).
    bpy.ops.object.duplicate()
    
    # Deselect the current object / object hierarchy.
    for obj in bpy.context.selected_objects:
        if name in obj.name:
            # Rename the main object.
            obj.name = name + '_' + identification
        bpy.data.objects[obj.name].select_set(False)
    
    bpy.context.view_layer.update()
    
def Add_Viewpoints(viewpoint_name: str, v) -> None:
    """
    Decription:
        Add viewpoints with the correct transformation.
        
    Args:
        (1) viewpoint_name [string]: Name of the main object.
        (2) v [Vector<float> (1x7) x n]: Position and orientation (Quaternion) of the object. 
                                         Note:
                                            n is the number of viewpoints.
    """

    for i, v_i in enumerate(v):
        # Duplication of objects and/or object hierarchy (if exists).
        Duplicate_Object(viewpoint_name, f'{i}')

        # Set the name of the new waipoint.
        #   (name + '_' + identification)
        viewpoint_name_new = viewpoint_name + f'_{i}'
        
        # Set the target (desired) viewpoint position and orientation.
        bpy.data.objects[viewpoint_name_new].location            = v_i[:3]
        bpy.data.objects[viewpoint_name_new].rotation_quaternion = v_i[3:]
        
def Get_Coordinates(name):
    """
    Description:
        Get the coordinate system of an individual object.
        
    Args:
        (1) name [string]: Object name.
        
    Returns:
        (1) parameter [Vector<float> (1x7) x n]: Data (position, orientation) of an object.
                                                 Note:
                                                    n is the number of potential coordinates.
    """
    
    return {
        'ABB_Smart_Gripper_L_Type_1_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], 
                                           [0.0, 0.0, 0.1142, 1.0, 0.0, 0.0, 0.0],
                                           [0.05, 0.0185, 0.0375, 0.707107, 0.0, 0.707107, 0.0],
                                           [-0.00727, 0.0297, 0.03506, 0.5, -0.5, 0.5, 0.5]],
        'ABB_Smart_Gripper_L_Type_2_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], 
                                           [0.0, 0.0, 0.1142, 1.0, 0.0, 0.0, 0.0],
                                           [0.05, 0.0185, 0.0375, 0.707107, 0.0, 0.707107, 0.0],
                                           [-0.00727, 0.0297, 0.03506, 0.5, -0.5, 0.5, 0.5]],
        'ABB_Smart_Gripper_R_Type_1_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], 
                                           [0.0, 0.0, 0.1142, 1.0, 0.0, 0.0, 0.0],
                                           [0.05, 0.0185, 0.0375, 0.707107, 0.0, 0.707107, 0.0],
                                           [-0.05, 0.0185, 0.0375, 0.0, -0.707107, 0.0, 0.707107]],
        'ABB_Smart_Gripper_R_Type_2_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], 
                                           [0.0, 0.0, 0.1142, 1.0, 0.0, 0.0, 0.0],
                                           [0.05, 0.0185, 0.0375, 0.707107, 0.0, 0.707107, 0.0],
                                           [-0.05, 0.0185, 0.0375, 0.0, -0.707107, 0.0, 0.707107]],
        'EE_SMC_MHM_ABB_IRB_120_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                                       [0.0, 0.0, 0.2177, 1.0, 0.0, 0.0, 0.0]],
        'EE_SMC_MHM_Universal_Robots_UR3_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                                                [0.0, 0.2177, 0.0, 1.0, 0.0, 0.0, 0.0]],
        'EE_SMC_XT661_2A_ABB_IRB_120_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                                            [0.0, 0.0, 0.1765, 1.0, 0.0, 0.0, 0.0]],
        'EE_SMC_XT661_2A_Universal_Robots_UR3_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                                                     [0.0, 0.0, 0.1765, 1.0, 0.0, 0.0, 0.0]],
        'EE_SMC_XT661_4C_ABB_IRB_120_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                                            [0.0, 0.0, 0.1877, 1.0, 0.0, 0.0, 0.0]],
        'EE_SMC_XT661_4C_Universal_Robots_UR3_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                                                     [0.0, 0.0, 0.1877, 1.0, 0.0, 0.0, 0.0]],
        'EE_SMC_ZP2_ABB_IRB_120_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                                       [0.0, 0.0, 0.186, 1.0, 0.0, 0.0, 0.0]],
        'EE_SMC_ZP2_Universal_Robots_UR3_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                                                [0.0, 0.0, 0.186, 1.0, 0.0, 0.0, 0.0]],
        'EE_Intel_Camera_HT_Circular_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                                            [0.0, 0.0, 0.005, 1.0, 0.0, 0.0, 0.0],
                                            [-0.1, 0.0, 0.03, 1.0, 0.0, 0.0, 0.0]],
        'EE_Intel_Camera_HT_Square_001': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                                          [0.0, 0.0, 0.005, 1.0, 0.0, 0.0, 0.0],
                                          [-0.1, 0.0, 0.03, 1.0, 0.0, 0.0, 0.0]]

    }[name]

def main():
    """
    Description:
        A simple script for generating data (position, orientation) of an object to determine the coordinate 
        system of the individual parts of the end-effector.
        
        The object in our case is the 'Viewpoint'.
    """    
    
    # Set rotation axis sequence configuration.
    bpy.data.objects['Viewpoint'].rotation_mode = 'QUATERNION'
        
    if CONST_RESET_ENV == True:
        Reset_Environment()
    else:
        # Move the end-effector to the base position.
        bpy.data.objects[CONST_EE_NAME].location = [0.0, 0.0, 0.0]
        bpy.data.objects[CONST_EE_NAME].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
        
        # Get the coordinates of the object:
        #   v_coord (location, orientation):
        #       location: x, y, z
        #       orientation (Quaternion): w, x, y, z
        v_coord = Get_Coordinates(CONST_EE_NAME)

        # Add viewpoints with the correct transformation.
        Add_Viewpoints('Viewpoint', v_coord)
        
    # Show the homogeneous transformation matrix of the object.
    i = 0
    while True:
        viewpoint_name = 'Viewpoint_' + str(i)
        # Check if the object exists within the scene
        if bpy.context.scene.objects.get(viewpoint_name):
            print(bpy.data.objects[viewpoint_name].matrix_basis)
        else:
            break
        i += 1

if __name__ == '__main__':
    main()
