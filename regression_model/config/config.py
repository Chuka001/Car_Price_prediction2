from os.path import dirname, abspath
PACKAGE_ROOT = dirname(dirname(abspath(__file__)))

# PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent

TRAINED_MODEL_DIR = PACKAGE_ROOT + "/trained_models"
DATASET_DIR = PACKAGE_ROOT + "/data"

TESTING_DATA_FILE = "test.csv"
TRAINING_DATA_FILE = "vehicles.csv"
TARGET = "price"
FEATURES = ['id', 'url', 'region', 'region_url', 'year', 'manufacturer', 'model',
       'condition', 'cylinders', 'fuel', 'odometer', 'title_status',
       'transmission', 'vin', 'drive', 'size', 'type', 'paint_color',
       'image_url', 'description', 'county', 'state', 'lat', 'long',
       'ori_cost_prc']

# variables
vars_to_retain = ['manufacturer', 'year','odometer', 
              'transmission', 'type', 'ori_cost_prc']


PIPELINE_NAME = "price_model_pipe.pkl"

rem_cols = ['id', 'url', 'region', 'region_url', 'model',
       'condition', 'cylinders', 'fuel', 'title_status', 
       'vin', 'drive', 'size', 'paint_color',
       'image_url', 'description', 'county', 'state', 'lat', 'long']