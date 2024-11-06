import configparser
from pathlib import Path


class ConfigFileParser:
    cfgFile = 'qa.ini'  # Значение по умолчанию, если не передано другое имя файла
    cfgFileDirectory = 'config'
    config = configparser.ConfigParser()

    def __init__(self, cfg=cfgFile):
        self.cfgFile = cfg
        self.BASE_DIR = Path(__file__).parent.parent
        self.CONFIG_FILE = self.BASE_DIR.joinpath(self.cfgFileDirectory).joinpath(self.cfgFile)

        # Проверка, существует ли файл конфигурации
        if not self.CONFIG_FILE.exists():
            raise FileNotFoundError(f"Файл конфигурации '{self.cfgFile}' не найден.")

        # Чтение файла конфигурации
        self.config.read(self.CONFIG_FILE)

    def getSectionParam(self, section, param):
        """Получить параметр из указанной секции конфигурационного файла."""
        try:
            # Попытка доступа к параметру в указанной секции
            return self.config[section][param]
        except KeyError as e:
            # Обработка ошибки, если секция или параметр не найдены
            missing_key = e.args[0]
            if missing_key == section:
                raise KeyError(f"Секция '{section}' не найдена в файле конфигурации '{self.cfgFile}'.")
            elif missing_key == param:
                raise KeyError(
                    f"Параметр '{param}' не найден в секции '{section}' в файле конфигурации '{self.cfgFile}'.")
        except configparser.NoSectionError:
            raise KeyError(f"Секция '{section}' отсутствует в файле конфигурации '{self.cfgFile}'.")
