from tvb.basic.neotraits.api import HasTraits
import json
from docutils.core import publish_parts
from tvbextxircuits.logger.builder import get_logger

LOGGER = get_logger(__name__)


def convert_rst_to_html(doc):
    """
    Convert from rst to html that can be rendered by Mathjax
    """
    kwargs = {
        'writer_name': 'html',
        'settings_overrides': {
            '_disable_config': True,
            'report_level': 5,
            'math_output': "MathJax /dummy.js",
        },
    }

    return publish_parts(doc, **kwargs)['html_body']


def doc_to_html(doc):
    html = convert_rst_to_html(doc)
    github_imgs_url = r'https://raw.githubusercontent.com/the-virtual-brain/tvb-root/master/tvb_documentation/sim_doc/'
    return html.replace(r'<object data="', r'<img width="500" height="500" src="' + github_imgs_url)\
        .replace(r'</object>', r'</img>')


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
        "description": doc_to_html(tvb_object.__doc__) if tvb_object.__doc__ else "",
        "arguments": {}
    }

    try:
        if issubclass(tvb_object, HasTraits):
            for attr_name in tvb_object.declarative_attrs:
                doc = getattr(tvb_object, attr_name).doc
                if doc != "":
                    output_dict['arguments'][attr_name] = doc_to_html(doc) if doc else ""
    except TypeError:
        LOGGER.warn(str(tvb_object) + "     " + str(type(tvb_object)))

    return output_dict


def save_json_description(class_path, output_path):
    class_obj = get_class(class_path)()
    description_dictionary = object_parse(class_obj)
    json_object = json.dumps(description_dictionary, indent=4)

    with open(output_path, "w+") as outfile:
        outfile.write(json_object)


