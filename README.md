# WhatsappDBAnalysis
This program takes export from WhatsApp Chats/Group Chats and saves them to a Postgres DB after which extensive EDA analysis will be done to generate insights.

### WhatsApp Export
The .txt export from whatsapp is used for this project. Export has to be done without media attachments and fed into the main.py file. The program reads the name of the file and subsequently creates a DB of the same name but stripped off the extension.
<br>
<br>
If a DB already exists, it pulls out the data from DB, loads it into Pandas and proceeds to analyse it. 
But if DB does not exist, it creates one and proceeds to insert cleaned data into the DB.
<br>
<br>
### Data Cleaning
While cleaning the data, the following log formats are exempted.
- Messages and calls are end-to-end encrypted. No one...
- `user` created group `group_name`
- You joined using this group's invite link
- `user` changed the subject from `subject1` to `subject2`
- `user` changed this group's settings to allow only admins to send messages to this group. 
- `user` changed this group's settings to allow all participants to send messages to this group. 
- `user` changed the group description.
- `user`changed to `new user`
- `user` added `user`
- `user` removed `user`
- `user` joined using this group's invite link., 
- `user` was added. 
- `user` left.
- `user` changed this group's icon. 

<mark>Please note that every valid message have the format: </mark> <br>
`date(m/d/y), time(24h) - user: message`, 
<br>
<mark>But these exempted sentences normally comes in the format: </mark>  <br>
`date(m/d/y), time(24h) - info message`, 

Due to the above deductions, the data can be analysed and cleaned using the following steps:
1. Load file and read one line after the other in a for loop, note the following:
   1. Some msg logs flow into the next line and python reads it as a new message
   2. To curb such error, first check using regex if the first few letters have a date format
   3. If yes, take it as a new message, else append it to previous message
   4. The date parsing supports Whatsapp messages from 2019 to 2022, this will be fixed in coming updates
2. Replace newlines with ". ", also replace null strings and split into 2 with '-'.
3. Take the first split and clean up time format
4. Take the second split and work on exemptions, then separate user from message in the allowed logs
5. Save row to DB.

### Data Analysis

This is WIP, Pandas will be used for analysis

### Data Visualization

This is WIP, Streamlit will be used for visualization

