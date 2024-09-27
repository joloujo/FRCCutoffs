import json

dataJSONpath = "./src/data.json"

def updateTable(headers: list[str], rows: list[list[str]]) -> None:
    with open(dataJSONpath, 'w') as f:

        jsonContent = {
            "table": {
                "headers": headers,
                "rows": rows,
            },
        }

        json.dump(jsonContent, f)