import json


def get_class(kls):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


def object_parse(object):
    tvb_object = object.tvb_ht_class

    output_dict = {
        "description": tvb_object.__doc__,
        "arguments": {}
    }

    for attr_name in tvb_object.declarative_attrs:
        doc = getattr(tvb_object, attr_name).doc
        if doc != "":
            output_dict['arguments'][attr_name] = doc

    return output_dict


def save_json_description(class_path, output_path):
    class_obj = get_class(class_path)()
    description_dictionary = object_parse(class_obj)
    json_object = json.dumps(description_dictionary, indent=4)

    with open(output_path, "w+") as outfile:
        outfile.write(json_object)


