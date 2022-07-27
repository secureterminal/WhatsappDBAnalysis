# WhatsappDBAnalysis
This takes export from WhatsApp Chats/Group Chats and saves them to a Postgres DB after which extensive EDA analysis will be done to generate insights.

### WhatsApp Export
The .txt export from whatsapp is used for this project. Export has to be done without media attachments and fed into the main.py file. The program reads the name of the file and subsequently creates a DB of the same name but stripped off the extension.
