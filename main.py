import json
import sys
import xml.etree.ElementTree as ET


def preorder(root):
    # Dict of attributes the tag has
    root_obj = root.attrib

    children = []
    for child in root:
        child_obj = preorder(child)
        if child_obj:
            children.append(child_obj)

    if len(children) == 0:
        inner_text = ''.join(root.itertext())
        if len(inner_text) != 0:
            root_obj[root.tag[root.tag.index('}') + 1:]] = inner_text
    else:
        root_obj[root.tag[root.tag.index('}') + 1:]] = children

    return root_obj if root_obj else ''


def xml_to_json(filename):
    tree_root = ET.parse(filename).getroot()

    with open('%s_parsedAll.json' % filename[:-4], 'w') as outfile:
        json.dump(preorder(tree_root), outfile, indent=2)

    print('$ END: Finished parsing %s successfully!' % filename)


def xmlnode_json(filename, tag):
    # Converting xml file to tree
    tree = ET.parse(filename)
    root = tree.getroot()

    json_result = []
    # Iterate over nodes with 'Cabin' tag name
    for c in root.iter(tag):
        json_result.append(preorder(c))

    # Writing result JSON to result file
    with open('%s_parsed.json' % filename[:-4], 'w') as outfile:
        json.dump(json_result, outfile, indent=2)

    print('$ END: Finished parsing %s successfully!' % filename)


def parse_seatmap1(file):
    # Parsing only cabins data
    xmlnode_json(file, '{http://www.opentravel.org/OTA/2003/05/common/}CabinClass')


def parse_seatmap2(file):
    # Parsing only cabins data
    xmlnode_json(file, '{http://www.iata.org/IATA/EDIST/2017.2}Cabin')


def main():
    for i in range(1, len(sys.argv)):
        xml_to_json('%s.xml' % sys.argv[i])

    if len(sys.argv) < 3:
        print('Please pass filenames as argument')
    elif sys.argv[1] == 'seatmap1' and sys.argv[2] == 'seatmap2':
        # Parsing seatmap1 & seatmap1 throw system args (file name)
        parse_seatmap1('%s.xml' % sys.argv[1])
        parse_seatmap2('%s.xml' % sys.argv[2])


if __name__ == '__main__':
    main()
