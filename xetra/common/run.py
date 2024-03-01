"""Running the Xetra ETL application"""
import logging as log
import logging.config as logcfg
import yaml as yml


def main():
    """
    Entry point to run Xetra ETL: job
    """
    # Parsing the YAML file
    config_path = 'E:/Projects/ETL Pipelines with Python+Pandas/Udemy_PythonEtlPiplines2/XetraETL/configs/xetra_report1_config.yml'
    config = yml.safe_load(open(config_path))
    # configure logging
    log_config = config['logging']
    log.config.dictConfig(log_config)
    logger = log.getLogger(__name__)
    



if __name__ == '__main__':
    main()