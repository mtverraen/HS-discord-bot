import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'weChall')


def add_user_as_document(disc_uName, weChall_uname):
    doc_ref.document(disc_uName).set({'wechall_username': weChall_uname})


def update_user_document(disc_uName, weChall_uname):
    doc_ref.document(disc_uName).update({'wechall_username': weChall_uname})


def delete_user(disc_uName):
    doc_ref.document(disc_uName).delete()
    print('Deleted: ' + disc_uName)

def get_all_users():
    user_dict = {}
    doc = doc_ref.get() #DeprecationWarning: 'Collection.get' is deprecated:  please use 'Collection.stream' instead.
    doc = doc_ref.get()

    for col in doc:
        colDict=col.to_dict()
        user_dict[col.id] = colDict['wechall_username']
    return user_dict


def get_wechall_uname(discord_uname):
    doc = doc_ref.document(discord_uname).get().to_dict()
    return doc['wechall_username']


def get_discord_uname(wechall_uname):
    dict = get_all_users()
    return dict[wechall_uname]


def get_discord_users():
    users = []
    for value in get_all_users().values():
        users.append(value)
    return users

def does_discord_user_exist(username):
    return doc_ref.document(username).get().to_dict()
