class DBPropertyUtil:
    @staticmethod
    def get_connection_string(config_file):
        connection_str = ""
        with open(config_file, 'r') as file:
            for line in file:
                if line.strip() and not line.startswith('#'):
                    key, value = line.split('=')
                    connection_str += f"{key.strip()}={value.strip()};"
        return connection_str
