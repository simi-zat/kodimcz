import csv, json

def order_kids(deti:list[str]) -> dict:
    ret = {}
    for d in deti:
        dob = d[2].split(". ")
        if dob[1] not in ret:
            ret[dob[1]] = []

        ret[dob[1]].append(d[0])
    return ret

seznam_trid = {}

with open("kids.csv", 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        if row[1] not in seznam_trid:
            seznam_trid[row[1]] = []

        seznam_trid[row[1]].append(row)

for k, v in seznam_trid.items():

    rr = order_kids(v)
    sorted_rr = dict(sorted(rr.items()))

    with open(f"{k}.json", 'w') as f:
        json.dump(sorted_rr, f, ensure_ascii=False)





