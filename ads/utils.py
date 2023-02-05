import csv
import json


# from ads.models import ADS


def csv_read(file_name, model):
    result = []
    with open(file_name, mode = 'r', encoding="utf-8") as file:
        file_data = csv.DictReader(file)
        for line in file_data:
            record = {"model": model, "pk": line["id"]}
            del line["id"]
            if "price" in line:
                line["price"] = float(line["price"])
            if "is_published" in line:
                if line["is_published"].lower() == "true":
                    line["is_published"] = True
                else:
                    line["is_published"] = False
            record["fields"] = line
            result.append(record)

    return result

def ads_csv_to_json(csv_name, json_name, model):
    csv_dict = csv_read(csv_name, model)
    with open(json_name, 'w', encoding='utf-8', ) as json_f:
        json_f.write(json.dumps(csv_dict, ensure_ascii=False))

    return "Ok"


ads_csv_to_json("../data/categories.csv", "../data/categories.json", 'ads.categories')
ads_csv_to_json("../data/ads.csv", "../data/ads.json", 'ads.ads')


# for line in file_data:
#     print(line)
