
import sys
import xml.etree.ElementTree as ET

# compares a list of junit files for unique test names

args = sys.argv
tests = []
counts = {}
def visit(node, prefix):
    if node.tag == 'testsuites':
        for child in node:
            visit(child, prefix)
    if node.tag == 'testsuite':
        for child in node:
            visit(child, prefix + node.attrib['name'])
    elif node.tag == 'testcase':
        test_name = prefix + node.attrib['name']
        tests.append(test_name)
        if test_name in counts:
            counts[test_name] += 1
        else:
            counts[test_name] = 1

for arg in args[1:]:
    tree = ET.parse(arg)
    root = tree.getroot()
    visit(root, '')

print(len(tests))
print(len(list(set(tests))))
for key, value in counts.items():
    if value > 1:
        print(key)
