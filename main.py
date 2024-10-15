import dotenv
import os
from logmod.custom_logger import CustomLogger

dotenv.load_dotenv()


class CustomModule:
    def __init__(self, logger):
        self.logger = logger

    def output_log(self):
        self.logger.debug("This is debug.")
        self.logger.info("This is info.")
        self.logger.warning("This is warning.")
        self.logger.error("This is error.")
        self.logger.critical("This is critical.")


if __name__ == "__main__":
    logger = CustomLogger.get_logger("main", os.environ.get("LOG_CONFIG_PATH", "config/logging.yaml"))
    main = CustomModule(logger)
    main.output_log()