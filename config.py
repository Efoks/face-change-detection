import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_DIR, 'Task-CV-FitSpace.Fashion', 'parameter set')
ANNOTATIONS_DIR = os.path.join(PROJECT_DIR, 'Task-CV-FitSpace.Fashion', 'Annotations')

TRAIN_DIR = os.path.join(PROJECT_DIR, 'Task-CV-FitSpace.Fashion', 'train set')
TRAIN_BATCH_DIR = os.path.join(TRAIN_DIR, 'batch01')
TRAIN_BATCH_RENDER_DIR = os.path.join(TRAIN_BATCH_DIR, 'Rendering')

BATCH_1_DIR = os.path.join(DATA_DIR, 'batch01')
BATCH_2_DIR = os.path.join(DATA_DIR, 'batch02')
BATCH_DIR = [BATCH_1_DIR, BATCH_2_DIR]
BATCH_RENDER_DIR = [os.path.join(BATCH_DIR[0], 'Rendering'), os.path.join(BATCH_DIR[0], 'Rendering')]

RENDER_TYPES = ['Front', 'Angle', 'Side']