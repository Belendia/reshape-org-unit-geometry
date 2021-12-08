import json

orgUnits = {"system":{"id":"4fc19f7c-8933-4e73-89cf-a6ce4e659b40","rev":"2adf10b","version":"2.36.4","date":"2021-12-08T10:33:12.295"},"organisationUnits":[]}

with open('orgunit.json') as f:
    data = json.load(f)
    for ou in data['organisationUnits']:
        if 'featureType' in ou and ou['featureType'] != "NONE":
            ou['geometry'] = {
                'type': ou['featureType'].capitalize(),
                'coordinates': ou['coordinates']
            }
            # print(ou['coordinates'][-4:])
            if ou['coordinates'][-4:] != "]]]]":
                print(ou['id'])
            del ou['coordinates']
            del ou['featureType']
            orgUnits['organisationUnits'].append(ou)

with open('output.json', 'w+') as f:
    json.dump(orgUnits, f)

print('Done')