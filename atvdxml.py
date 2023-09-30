import xml.etree.ElementTree as ET

def criar_contato():
  nome = input("Nome: ")
  phone_number = input("Número de telefone: ")
  email = input("E-mail: ")
  contato = ET.Element("contato")
  nome_element = ET.SubElement(contato, "nome")
  nome_element.text = nome
  phone_number_element = ET.SubElement(contato, "phone_number")
  phone_number_element.text = phone_number
  email_element = ET.SubElement(contato, "email")
  email_element.text = email
  return contato
def save_contatos(contatos, filenome):
  """Salva no xml"""
  root = ET.Element("contatos")
  for contato in contatos:
    root.append(contato)
  tree = ET.ElementTree(root)
  tree.write(filenome)
def main():
  """pede os dados e salva no xml"""
  contato = criar_contato()
  contatos = [contato]
  save_contatos(contatos, "contatos.xml")
if __name__ == "__main__":
  main()