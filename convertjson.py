import json

input = open('ACME_Main.json')
inputdata = json.load(input)
input.close()

outputdata = {

    "Name": "ACME_Main",
    "ContactFlowType": "CONTACT_FLOW",
    "Content": json.dumps(inputdata)
}

with open('output.json', 'w+') as outfile:
    json.dump(outputdata, outfile)

