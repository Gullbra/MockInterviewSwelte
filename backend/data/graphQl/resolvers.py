import json
import os


def get_data_resolver(obj, info):
    print("Resolver running!")

    print("what about this?")
    try:
        print("Before file opening")
        with open('../data/json/data.combinedData.json') as all_data_file:
            all_data_dict = json.loads(all_data_file.read())
        print("All data", all_data_dict)

        payload = {
            "success": True,
            "data": all_data_dict
        }
        # payload = all_data_file
        return payload
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
        print("error!{}".format(str(error)))
        print(os.getcwd())
        # payload = {}
        return payload

    # return payload
