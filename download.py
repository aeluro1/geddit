def download(entry):
    match entry.domain:
        case "i.redd.it":
            pass
        case "v.redd.it":
            pass
        case _:
            print(f"Unkown domain for post '{entry.id}': {entry.domain}")
