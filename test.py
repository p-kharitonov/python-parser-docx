from parser_docx import ParserDocx

def main():
  path = "test.docx"
  text = ParserDocx(path).get_text()
  print(text)

if __name__ == "__main__":
  main()
