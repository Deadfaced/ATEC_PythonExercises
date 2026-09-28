import re

texto = """Cliente: Marta Lopes
Email: marta.lopes@cliente.pt Alternativo: marta+apoio@exemplo.com
Contactos: 912345678 / 223456789 / 934567890"""

padrao_email = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
padrao_telemovel = r"(?<!\d)9\d{8}(?!\d)"

emails = re.findall(padrao_email, texto)
telemoveis = re.findall(padrao_telemovel, texto)

texto = re.sub(padrao_email, "[EMAIL]", texto)
texto = re.sub(padrao_telemovel, "[TELEMÓVEL]", texto)

texto = re.sub(r"\s+", " ", texto).strip()

print("Texto:", texto)
print("Emails detetados:", len(emails))
print("Telemóveis detetados:", len(telemoveis))