def FilterExternalEmails():
    """
    Receives a list of emails and filters for external emails only
    """

    emails_list: list[str] = ["email1@empresa.pt",
                     "email2@empresa.pt",
                     "email3@externo.pt",
                     "email4@empresa.pt",
                     "email5@externo.pt",
                     "email6@externo.pt"]

    for curr_email in emails_list:
        if curr_email.endswith("@empresa.pt"):
            continue
        else:
            print(f"{curr_email} Enviar campanha de marketing para o email analisado")

FilterExternalEmails()