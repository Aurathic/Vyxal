import os
import yaml

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
ELEMENTS_YAML = os.path.join(CURR_DIR, "elements.yaml")
ELEMENTS_TXT = os.path.join(CURR_DIR, "elements.txt")

with open(ELEMENTS_YAML, "r", encoding="utf-8") as elements:
    data = yaml.safe_load(elements)

with open(ELEMENTS_TXT, "w", encoding="utf-8") as output:
    for element in data:
        if "modifier" in element:
            output.write(element["modifier"] + " (" + element["name"] + ")\n\n")
            output.write("- " + element["description"] + "\n\n")
            output.write("    " + element["usage"] + "\n\n")

        else:
            output.write(
                str(element["element"]) + " (" + str(element["name"]) + ")\n\n"
            )
            output.write("- " + str(element["description"]) + "\n\n")
            if "overloads" in element:
                for overload in element["overloads"]:
                    data_types = map(
                        lambda x: " ".join(x), zip(overload.split("-"), "abc")
                    )
                    output.write(
                        "    "
                        + ", ".join(data_types)
                        + ": "
                        + str(element["overloads"][overload])
                        + "\n"
                    )
            if "vectorise" in element and element["vectorise"]:
                output.write("    otherwise: vectorise\n")
        output.write("-------------------------------\n")
