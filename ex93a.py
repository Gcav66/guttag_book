
def get_models(fname):
    models = []
    try:
        with open(fname, 'r') as models_file:
            for line in models_file:
                models.append(float(line))
    except IOError as e:
        raise ValueError(f'Whoops: get_models could not open {fname} Are you referencing the full path?')
        #raise e
    return models


try:
    models = get_models('models_metrics.txt')
except Exception as e:
    print (e)
