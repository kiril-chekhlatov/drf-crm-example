def create_choices_dict(list_choice) -> dict:
    data = {}
    for choice_class in list_choice:
        for attr in dir(choice_class):
            if isinstance(getattr(choice_class, attr), tuple):
                class_name = choice_class.__name__.lower()
                data.update({class_name: {}})
                for choice in getattr(choice_class, attr):
                    data[class_name].update({choice[0]: choice[1]})

    return data
