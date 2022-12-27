from inspect import stack


class SharedData:
    module_shared_data: dict = {}
    global_shared_data: dict = {}

    @staticmethod
    def share(key: str, value: any, scope: str = 'module') -> None:
        """
        add data to shared data which can be used by other test suites
        :param key: name of the shared data
        :param value: value of the shared data
        :param scope: scope of the shared data (can be module and global)
        """
        module = stack()[1][1]
        if scope == 'module':
            SharedData.module_shared_data[key] = {'module': module, 'value': value}
        elif scope == 'global':
            SharedData.global_shared_data[key] = {'value': value}
        else:
            raise ValueError(f'scope can only be module or global, get: {scope}')

    @staticmethod
    def get(key: str) -> any:
        """
        get share data from other test classes
        :param key: name of the shared data
        :return shared_data
        """
        module = stack()[1][1]

        data = SharedData.module_shared_data.get(key)
        if data and data.get('module') == module and data.get('value'):
            return data.get('value')

        data = SharedData.global_shared_data.get(key)
        if data.get('value'):
            return data.get('value')
        else:
            return None
