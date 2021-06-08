# ORDINAL - ORD
# Numerical - NUM
from collections import defaultdict
# * CG: {[0,7]}; Degree:{BTech, MTech}-> poor

class AOI_attribute_parser:
    def __init__(self, filename):
        self.filename = filename
        self.attribute_type = {}
        self.
        # self.delim_char = delim

    def parse_rule_line(self, line):
        rules_text, label = line.split("->")
        label = label.strip()
        rules_list_strings = rules_text.split(';')

        for rule_string in rules_list_strings:
            rule_list = [rule.strip() for rule in rule_string.split()]

            for rule in rule_list:
                attr, accepted_values = [u.strip() for u in rule.split(':')]

                if attr not in self.attribute_type.keys():
                    print("Error")
                    exit()

                attr_type = self.attribute_type[attr]

                if attr_type == 'ORD':
                    pass
                elif attr_type == 'NUM':
                    pass

    def parse(self):

        with open(self.filename, 'r') as fp:
            file_lines = [line.strip() for line in fp.readlines()]
            line_number = 0

            attribute_types_assigned = False

            while not attribute_types_assigned:
                if file_lines[line_number].strip() == '--/':
                    attribute_types_assigned = True

                key, value = file_lines[line_number].split(':')
                self.attribute_type[key.strip()] = value.strip()

                line_number += 1

            rules = []

            while line_number < len(file_lines):
                rules.append(self.parse_rule_line(file_lines[line_number]))
                line_number += 1
