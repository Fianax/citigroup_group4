import pathlib

from docling.document_converter import DocumentConverter

# 
source = 'data/codeconduct_en_2023.pdf'

converter = DocumentConverter()
result = converter.convert(source)
markdown = result.document.export_to_markdown()

#
pathlib.Path('data/codeconduct_en_2023.md').write_text(markdown)

print('fin')