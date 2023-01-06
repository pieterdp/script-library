#!/usr/bin/env python3
import csv
from copy import deepcopy
import argparse
from ruamel.yaml import YAML

SCAFFOLDING = {
    'title': 'Stands',
    'stand_list': []
}

BUILDINGS = {
    'K+1': {
        'name': 'K (level 1)',
        'map': 'map_k_1',
        '_groups': {
            'A': {
                'info': {
                    'building': 'K',
                    'floor': 1,
                    'amount': 12,
                    'group': 'A'
                },
                '_stands': {}
            },
            'B': {
                'info': {
                    'building': 'K',
                    'floor': 1,
                    'amount': 12,
                    'group': 'B'
                },
                '_stands': {}
            },
            'C': {
                'info': {
                    'building': 'K',
                    'floor': 1,
                    'amount': 12,
                    'group': 'C'
                },
                '_stands': {}
            }
        }
    },
    'K+2': {
        'name': 'K (level 2)',
        'map': 'map_k_2',
        '_groups': {
            'A': {
                'info': {
                    'building': 'K',
                    'floor': 2,
                    'amount': 12,
                    'group': 'A'
                },
                '_stands': {}
            }
        }
    },
    'AW+1': {
        'name': 'AW',
        'map': 'map_aw',
        '_groups': {
            'A': {
                'info': {
                    'building': 'AW',
                    'floor': 1,
                    'amount': 12,
                    'group': 'A'
                },
                '_stands': {}
            }
        }
    },
    'H+1': {
        'name': 'H',
        'map': 'map_h',
        '_groups': {
            'A': {
                'info': {
                    'building': 'H',
                    'floor': 1,
                    'amount': 10,
                    'group': 'A'
                },
                '_stands': {}
            }
        }
    }
}


def parse_csv(csv_file):
    """
    Convert a CSV file to whatever object from hell the website wants.
    CSV structure
    Stand; Points; Theme; Location; Group
    Does not support Sunday/Saturday stands.
    """
    structured_stands = deepcopy(BUILDINGS)
    with open(csv_file, 'r') as fh:
        reader = csv.reader(fh)
        for row in reader:
            stand = {
                'name': row[0]
            }
            theme = row[2]
            building = row[3]
            group = row[4]
            if theme not in structured_stands[building]['_groups'][group]['_stands']:
                structured_stands[building]['_groups'][group]['_stands'][theme] = {
                    'theme': theme,
                    'stands': {
                        'all': []
                    }
                }
            structured_stands[building]['_groups'][group]['_stands'][theme]['stands']['all'].append(stand)
    return structured_stands


def main():
    parser = argparse.ArgumentParser(
        'ConvertCSVToStandsYaml',
        description='''
        Convert a CSV of the format Stand; Points; Theme; Location; Group
        to a horrible YAML that the website accepts for stands-building.yaml.
        '''
    )
    parser.add_argument('csv_file')
    args = parser.parse_args()

    parsed_csv = parse_csv(args.csv_file)

    # Convert themes to a list
    for building in parsed_csv.keys():
        for group in parsed_csv[building]['_groups'].keys():
            parsed_csv[building]['_groups'][group]['stands'] = []
            for theme, theme_obj in parsed_csv[building]['_groups'][group]['_stands'].items():
                parsed_csv[building]['_groups'][group]['stands'].append(theme_obj)
            del parsed_csv[building]['_groups'][group]['_stands']
    
    for building in parsed_csv.keys():
        parsed_csv[building]['groups'] = []
        for group, group_obj in parsed_csv[building]['_groups'].items():
            parsed_csv[building]['groups'].append(group_obj)
        del parsed_csv[building]['_groups']
    
    # Add scaffolding
    stands_building = deepcopy(SCAFFOLDING)
    for building, building_obj in parsed_csv.items():
        stands_building['stand_list'].append(building_obj)
    
    # Convert to YAML
    yaml = YAML()
    with open('stands-building.yaml', 'w') as fh:
        yaml.dump(stands_building, fh)

    return 0


if __name__ == '__main__':
    exit(main())
