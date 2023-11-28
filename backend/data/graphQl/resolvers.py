import json


def get_data_resolver(obj, info):
    print("Resolver running!")

    try:
        with open('../json/data.combinedData.json') as all_data_file:
            all_data_dict = json.loads(all_data_file.read())
        print(all_data_dict)
        payload = {
            "success": True,
            "getData": all_data_dict
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
