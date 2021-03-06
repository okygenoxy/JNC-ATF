import os
#this project env
PROJECT_PATH=os.path.dirname(os.path.realpath(__file__)).replace('libs','')
PROJECT_LOG_PATH='logs'+os.sep
PROJECT_DATA_PATH='data'+os.sep
PROJECT_LIBS_PATH='libs'+os.sep
FLASK_APP_PATH='app'+os.sep
FLASK_TEMPLATES_PATH='templates'+os.sep
FLASK_TEMPLATES_CSS_PATH=FLASK_TEMPLATES_PATH+'css'+os.sep
FLASK_TEMPLATES_JS_PATH=FLASK_TEMPLATES_PATH+'js'+os.sep
PROJECT_LOG_REAL_PATH=PROJECT_PATH+PROJECT_LOG_PATH
PROJECT_DATA_REAL_PATH=PROJECT_PATH+PROJECT_DATA_PATH
PROJECT_LIBS_REAL_PATH=PROJECT_PATH+PROJECT_LIBS_PATH
FLASK_APP_REAL_PATH=PROJECT_PATH+FLASK_APP_PATH
FLASK_TEMPLATES_REAL_PATH=FLASK_APP_REAL_PATH+FLASK_TEMPLATES_PATH
FLASK_TEMPLATES_CSS_REAL_PATH=FLASK_TEMPLATES_REAL_PATH+FLASK_TEMPLATES_CSS_PATH
FLASK_TEMPLATES_JS_REAL_PATH=FLASK_TEMPLATES_REAL_PATH+FLASK_TEMPLATES_JS_PATH

#log setting
DEF_LOGGING_FORMATTER = '[%(asctime)s] [%(levelname)s] [%(process)d]: %(message)s'
DEF_DATE_FORMATTER = '%Y-%m-%d %H:%M:%S'