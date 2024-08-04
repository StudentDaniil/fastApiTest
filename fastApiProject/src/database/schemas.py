def individual_data(message):
    return {
        "id": str(message["_id"]),
        "text": message["text"],
        "from_f": message["from_f"]
    }


def all_data(messages):
    return [individual_data(message) for message in messages]
