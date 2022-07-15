from datetime import datetime

def logger_without_params(func):
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        func_date_time = datetime.now().strftime('%d-%b-%y %H:%M:%S')
        func_name = func.__name__
        func_args = args, kwargs
        logger_slice = [f'{func_date_time}; function: {func_name};\nargs: {str(func_args)};\n'
                        f'function result: {str(func_result)}\n\n']
        with open('logger.txt', 'a', encoding='utf-8') as f:
            f.write(logger_slice[0])
        return func_result
    return wrapper

def logger(filepath):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            func_date_time = datetime.now().strftime('%d-%b-%y %H:%M:%S')
            func_name = func.__name__
            func_args = args, kwargs
            logger_slice = [f'{func_date_time}; function: {func_name};\nargs: {str(func_args)};\n'
                            f'function result: {str(func_result)}\n\n']
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(logger_slice[0])
            return func_result
        return wrapper
    return decorator
