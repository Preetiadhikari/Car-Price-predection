import json
import pickle


__fuelsystem = None
__data_columns = None
__model = None


def get_fuelsystem_names():
    return __fuelsystem


def load_saved_artifacts():
    global __fuelsystem
    global __data_columns

    with open(".\artifacts\columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __fuelsystem = __data_columns[37:]

    with open("artifacts/carprice_pred.pickle", "rb") as f:
        __model = pickle.load(f)
    print("loading saved artifact...done")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_fuelsystem_names())
