# BPY (Blender as a python) [pip3 install bpy]
import bpy
# System (Default)
import sys

"""
Description:
    Initialization of constants.
"""
CONST_RESET_ENV = True

def Reset_Environment():
    """
    Description:
        Restore the environment to the default position.
    """
    
    bpy.data.objects['Viewpoint'].location = [0.0, 0.0, 0.0]
    bpy.data.objects['Viewpoint'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
        
    # Move the end-effectors to the default position.
    bpy.data.objects['Smart_Gripper_L_Type_1_001'].location = [0.0, -0.4, 0.0]
    bpy.data.objects['Smart_Gripper_L_Type_1_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    bpy.data.objects['Smart_Gripper_L_Type_2_001'].location = [0.0, 0.4, 0.0]
    bpy.data.objects['Smart_Gripper_L_Type_2_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    bpy.data.objects['Smart_Gripper_R_Type_1_001'].location = [0.0, -0.2, 0.0]
    bpy.data.objects['Smart_Gripper_R_Type_1_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
    bpy.data.objects['Smart_Gripper_R_Type_2_001'].location = [0.0, 0.2, 0.0]
    bpy.data.objects['Smart_Gripper_R_Type_2_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]

def Get_Coordinates(name):
    """
    Description:
        Get the coordinate system of an individual object.
        
    Args:
        (1) name [string]: Object name.
        
    Returns:
        (1) parameter [Vector<float> 1x3, Vector<float>1x4]: Data (position, orientation) of an object.
    """
    
    return {
        'Base': [[0.0, 0.0, 0.0], 
                 [1.0, 0.0, 0.0, 0.0]],
        'Servo': [[0.0, 0.0, 0.1142], 
                  [1.0, 0.0, 0.0, 0.0]],
        'Vacuum_Left': [[0.05, 0.0185, 0.0375], 
                        [0.707107, 0.0, 0.707107, 0.0]],
        'Vacuum_Right': [[-0.05, 0.0185, 0.0375], 
                         [0.0, -0.707107, 0.0, 0.707107]],
        'Camera': [[-0.00727, 0.0297, 0.03506], 
                   [0.707107, 0.0, 0.707107, 0.0]]
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
        # Move the end-effector to the base.
        #   1\ Smart_Gripper_L_Type_1_001
        #   2\ Smart_Gripper_L_Type_2_001
        #   3\ Smart_Gripper_R_Type_1_001
        #   4\ Smart_Gripper_R_Type_2_001
        bpy.data.objects['Smart_Gripper_L_Type_1_001'].location = [0.0, 0.0, 0.0]
        bpy.data.objects['Smart_Gripper_L_Type_1_001'].rotation_quaternion = [1.0, 0.0, 0.0, 0.0]
        
        # Get the coordinates of the object:
        #   location: x, y, z
        #   orientation (Quaternion): w, x, y, z
        location, orientation = Get_Coordinates('Base')
        
        # Set the position and orientation of the object.
        bpy.data.objects['Viewpoint'].location = location
        bpy.data.objects['Viewpoint'].rotation_quaternion = orientation
        
    # Show the homogeneous transformation matrix of the object.
    print(bpy.data.objects['Viewpoint'].matrix_basis)

if __name__ == '__main__':
    main()
