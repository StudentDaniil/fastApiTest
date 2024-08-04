def individual_data(message):
    return {
        "id": str(message["_id"]),
        "text": message["text"]
    }


def all_data(messages):
    return [individual_data(message) for message in messages]
