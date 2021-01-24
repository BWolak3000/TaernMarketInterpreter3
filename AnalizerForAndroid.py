from monkeylearn import MonkeyLearn


def analize(data):
    ml = MonkeyLearn('1bcc3c25a893ee80d29c99e2401dd356a797b3cb')
    model_id = 'ex_dtshZhuK'
    data = ['first text', {'text': data}, '']
    response = ml.extractors.extract(model_id, data=data)
    return response


def analize_to_String(analizedData):
    result = ''
    for extraction in analizedData.body[1]['extractions']:
        result = result + '\n' + extraction['tag_name'] + ' :' + extraction['parsed_value']
    return result
