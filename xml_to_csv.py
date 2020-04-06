import argparse
import os
import pandas as pd
import xml.etree.ElementTree as ET
from glob import glob

parser = argparse.ArgumentParser(description='Parser PascalVoc files to only csv file')
parser.add_argument("--path_xmls", help="Folder containing the xml files ", required=True)
parser.add_argument("--path_save_csv", help="Folder containing the xml files ", required=True)
parser.add_argument("--name_csv", help="File's name csv", required=True)

args = parser.parse_args()

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    xml_df = xml_to_csv(args.path_xmls)
    xml_df.to_csv(args.path_save_csv + "\\" + args.name_csv, index=None)
    print('Successfully converted xml to csv.')


main()