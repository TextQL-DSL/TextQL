from dsl.parser import parser

data = "USE './data.docx'"
print(parser.parse(data))