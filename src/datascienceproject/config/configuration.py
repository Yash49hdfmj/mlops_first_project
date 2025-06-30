from src.datascienceproject.constants import *
from src.datascienceproject.util.common import read_yaml,create_directories
from pathlib import Path
from src.datascienceproject.entity.config_entity import (DataIngestconfig,DataValidationConfig)


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schemas_filepath=SCHEMA_FILE_PATH
                 ):
        self.config = read_yaml(Path(config_filepath))
        self.params = read_yaml(Path(params_filepath))
        self.schema = read_yaml(Path(schemas_filepath))

        create_directories([self.config.artifacts_root],verbose = True)

    # data ingestion get config

    def get_data_ingestion_config(self)-> DataIngestconfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir],verbose = True)

        data_ingestion_config = DataIngestconfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    # data validation config

    def get_data_validation_config(self)-> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir],verbose = True)

        data_validation_config = DataValidationConfig(
            root_dir=Path("artifacts/data_validation"),
            unzip_data_dir=Path("artifacts/data_ingestion/winequality-red.csv"),
            STATUS_FILE="artifacts/data_validation/status.txt",
            all_schema=self.schema["COLUMNS"]
        )

        return data_validation_config