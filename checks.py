from options import *

try:
    from screeninfo import get_monitors
except:
    print('install screeninfo: pip install screeninfo')
    exit(0)

try:   
    import ultralytics
except:
    print('install ultralytics: pip install ultralytics')
    exit(0)

if '.engine' in AI_model_path:
    import tensorrt

try:
    import numpy
except:
    print('install numpy: pip install numpy')
    exit(0)

if Dxcam_capture == True:
    try:
        import dxcam
    except:
        print('Install dxcam: pip install dxcam[cv2]')
        exit(0)

import importlib.metadata
import os

try:
    from cv2 import __version__
except:
    print('install cv2: pip install opencv-python')
    exit(0)

def run_checks():
    ultralytics.utils.checks.collect_system_info()

    cuda_support = ultralytics.utils.checks.cuda_is_available()
    if cuda_support == True:
        print('\nCuda support True')
    else:
        print('Cuda is not supported. Please reinstall pytorch with GPU support. https://pytorch.org/get-started/locally/\nIf you have reinstalled but there is no GPU support, Google how to solve this problem.')

    print('OpenCV version: {0}'.format(__version__))

    if '.engine' in AI_model_path:
        print('TensorRT version: {0}'.format(tensorrt.__version__))
    else:
        print(ultralytics.YOLO(AI_model_path, task='detect').info())

    print('numpy version: {0}'.format(numpy.version.version))

    if Dxcam_capture:
        print('DXcam devices info:\n{0}'.format(dxcam.output_info()))
    # TODO: ADD OBS_CAPTURE CHECKS
    try:
        print('asyncio version: {0}'.format(importlib.metadata.version('asyncio')))
    except:
        print('Please install asyncio: pip install asyncio')

    print('Options file checks:\n')

    print('original_screen_width', original_screen_width)
    print('original_screen_height', original_screen_height, '\n')

    desktop_size = get_monitors()
    for m in desktop_size:
        if m.is_primary:
            if original_screen_width != m.width:
                print('Please open options.py and edit original_screen_width to', m.width)
                exit(0)
            if original_screen_height != m.height:
                print('Please open options.py and edit original_screen_height to', m.height)
                exit(0)

    print('screen_width', screen_width)
    print('screen_height', screen_height, '\n')

    if screen_width >= original_screen_width:
        print('Please decrease the screen_width value to increase the performance of the application.')
        exit(0)
    if screen_height >= original_screen_height:
        print('Please decrease the screen_height value to increase the performance of the application.')
        exit(0)

    print('Dxcam_capture', Dxcam_capture)
    print('dxcam_capture_fps', dxcam_capture_fps)
    print('dxcam_monitor_id', dxcam_monitor_id)
    print('dxcam_gpu_id', dxcam_gpu_id)
    print('dxcam_max_buffer_len', dxcam_max_buffer_len, '\n')

    print('Obs_capture', Obs_capture)
    print('Obs_camera_id', Obs_camera_id)
    print('Obs_capture_fps', Obs_capture_fps, '\n')

    print('native_Windows_capture', native_Windows_capture, '\n')

    print('body_y_offset', body_y_offset)
    print('hideout_targets', hideout_targets, '\n')

    print('mouse_smoothing', mouse_smoothing)
    print('mouse_auto_shoot', mouse_auto_shoot)
    print('mouse_auto_aim', mouse_auto_aim)
    print('mouse_native', mouse_native, '\n')

    print('AI_model_path', AI_model_path)
    print('AI_image_size', AI_image_size)
    print('AI_conf', AI_conf)
    print('AI_iou', AI_iou)
    print('AI_device', AI_device)
    print('AI_half', AI_half)
    print('AI_max_det', AI_max_det)

    print('show_window', show_window)
    print('show_speed', show_speed)
    print('show_fps', show_fps)
    print('debug_window_scale_percent', debug_window_scale_percent)
    print('debug_window_name', debug_window_name, '\n')

    print('Environment variables:\n')
    for key, value in os.environ.items():
        print(f'{key}: {value}')

if __name__ == "__main__":
    run_checks()