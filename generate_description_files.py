from tvbextxircuits.handlers.component_parser import ComponentsParser


def main():
    route_handler = ComponentsParser()
    route_handler.generate_doc_files()


if __name__ == "__main__":
    main()
