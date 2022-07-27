def check_removals(user_str):
    both_contacts = []
    cleaned_contacts = []
    if ' changed to ' in user_str:
        both_contacts = user_str.split(' changed to ')
    if ' removed ' in user_str:
        both_contacts = user_str.split(' removed ')
    if ' added ' in user_str:
        both_contacts = user_str.split(' added ')

    for one_contact in both_contacts:
        one_contact = one_contact.replace('.', '').replace(' ', '')
        cleaned_contacts.append(one_contact)

    if cleaned_contacts[0].startswith('+') and cleaned_contacts[1].startswith('+'):
        if len(cleaned_contacts[0]) == len(cleaned_contacts[1]):
            return True
    if len(user_str.split(':')) == 1:
        return True
    else:
        return False


def check_who_changed_group_details(user_str):
    all_words = ["changed this group's settings to allow only admins to send messages to this group. ",
                 ' changed the group description. ',
                 " changed this group's settings to allow all participants to send messages to this group. ",
                 "You joined using this group's invite link. ",
                 'Messages and calls are end-to-end encrypted. No one outside of this chat, not even ' 
                 'WhatsApp, can read or listen to them. Tap to learn more.. ',
                 ' changed to ', " added ", ' removed ', "joined using this group's invite link. ", " was added. ",
                 ' left. ',
                 " changed this group's icon. "
                 ]
    if len(user_str.split(':')) == 1:
        for word in all_words:
            if word in user_str:
                return True


def check_str_conditions(strg):
    print(strg)
    pass
