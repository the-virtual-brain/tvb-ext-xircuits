import json

from tvb.basic.neotraits.api import HasTraits


def _format_doc(doc):
    return _multiline_math_directives_to_matjax(doc).replace('&', '&amp;').replace('.. math::', '')


def _multiline_math_directives_to_matjax(doc):
    """
    Looks for multi-line sphinx math directives in the given rst string
    It converts them in html text that will be interpreted by mathjax
    The parsing is simplistic, not a rst parser.
    Wraps .. math :: body in \[\begin{split}\end{split}\]
    """

    # doc = text | math
    BEGIN = r'\[\begin{split}'
    END = r'\end{split}\]'

    in_math = False  # 2 state parser
    out_lines = []
    indent = ''

    for line in doc.splitlines():
        if not in_math:
            # math = indent directive math_body
            indent, sep, _ = line.partition('.. math::')
            if sep:
                out_lines.append(BEGIN)
                in_math = True
            else:
                out_lines.append(line)
        else:
            # math body is at least 1 space more indented than the directive, but we tolerate empty lines
            if line.startswith(indent + ' ') or line.strip() == '':
                out_lines.append(line)
            else:
                # this line is not properly indented, math block is over
                out_lines.append(END)
                out_lines.append(line)
                in_math = False

    if in_math:
        # close math tag
        out_lines.append(END)

    return '\n'.join(out_lines)


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
        "description": _format_doc(tvb_object.__doc__) if tvb_object.__doc__ else "",
        "arguments": {}
    }


    try:
        if issubclass(tvb_object, HasTraits):
            for attr_name in tvb_object.declarative_attrs:
                doc = getattr(tvb_object, attr_name).doc
                if doc != "":
                    output_dict['arguments'][attr_name] = _format_doc(doc) if doc else ""
    except TypeError:
        print(str(tvb_object) + "     " + str(type(tvb_object)))

    return output_dict


def save_json_description(class_path, output_path):
    class_obj = get_class(class_path)()
    description_dictionary = object_parse(class_obj)
    json_object = json.dumps(description_dictionary, indent=4)

    with open(output_path, "w+") as outfile:
        outfile.write(json_object)


