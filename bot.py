from pyrogram import Client, filters
from config import Config

bot = Client(
    'notesbot',
    api_id = Config.API_ID,
    api_hash = Config.API_HASH,
    bot_token = Config.BOT_TOKEN
    )

@bot.on_message(filters.command(['start']))
def echo(client, message):
    message.reply_text("Hy")

@bot.on_message(filters.command(['help']))
def help(client, message):
    message.reply(Config.HELP_TEXT)

@bot.on_message(filters.command(['addprincipal']) & filters.chat(chats = Config.ADMIN_ID))
def add_princi(client, message):
    try: # If empty command was passed
        id_to_add = message.command[1]
    except IndexError:
        print('IndexError')
        message.reply_text('Enter an id after the command.')
        return
    try: # If string was passed instead of a Number
        id_to_add = int(id_to_add)
    except Exception as e:
        print(e)
        message.reply_text('The id should be a number.')
        return
    Config.PRINCIPAL_ID.append(id_to_add) # Add the id to the Global Variable

@bot.on_message(filters.command(['removeprincipal']) & filters.chat(chats = Config.ADMIN_ID))
def add_princi(client, message):
    try: # If empty command was passed
        id_to_add = message.command[1]
    except IndexError:
        print('IndexError')
        message.reply_text('Enter an ID after the command.')
        return
    try: # If string was passed instead of a Number
        id_to_add = int(id_to_add)
    except Exception as e:
        print(e)
        message.reply_text('The ID should be a number.')
        return
    Config.PRINCIPAL_ID.remove(id_to_add) # Remove the id from the Global Variable

@bot.on_message(filters.command(['addhod']) & filters.chat(chats = (Config.PRINCIPAL_ID + Config.ADMIN_ID)))
def add_hod(client, message):
    try: # If empty comand is passed
        id_to_add = message.command[1]
    except IndexError:
        message.reply_text('Enter an ID after the command.')
        return
    try: # If the ID is entered as a string
        id_to_add = int(id_to_add)
    except Exception as e:
        print(e)
        message.reply_text('The ID should be a number.')
        return
    Config.HOD_ID.append(id_to_add)

@bot.on_message(filters.command(['removehod']) & filters.chat(chats = (Config.PRINCIPAL_ID + Config.ADMIN_ID)))
def add_princi(client, message):
    try: # If empty command was passed
        id_to_add = message.command[1]
    except IndexError:
        print('IndexError')
        message.reply_text('Enter an ID after the command.')
        return
    try: # If string was passed instead of a Number
        id_to_add = int(id_to_add)
    except Exception as e:
        print(e)
        message.reply_text('The ID should be a number.')
        return
    Config.HOD_ID.remove(id_to_add) # Remove the id from the Global Variable

@bot.on_message(filters.command(['addteacher']) & filters.chat(chats = (Config.HOD_ID + Config.PRINCIPAL_ID + Config.ADMIN_ID)))
def add_hod(client, message):
    try: # If empty comand is passed
        id_to_add = message.command[1]
    except IndexError:
        message.reply_text('Enter an ID after the command.')
        return
    try: # If the ID is entered as a string
        id_to_add = int(id_to_add)
    except Exception as e:
        print(e)
        message.reply_text('The ID should be a number.')
        return
    Config.TEACHERS_ID.append(id_to_add)

@bot.on_message(filters.command(['removeteacher']) & filters.chat(chats = (Config.HOD_ID + Config.PRINCIPAL_ID + Config.ADMIN_ID)))
def add_princi(client, message):
    try: # If empty command was passed
        id_to_add = message.command[1]
    except IndexError:
        print('IndexError')
        message.reply_text('Enter an ID after the command.')
        return
    try: # If string was passed instead of a Number
        id_to_add = int(id_to_add)
    except Exception as e:
        print(e)
        message.reply_text('The ID should be a number.')
        return
    Config.TEACHERS_ID.remove(id_to_add) # Remove the id from the Global Variable

@bot.on_message(filters.command(['addstudent']) & filters.chat(chats = (Config.HOD_ID + Config.PRINCIPAL_ID + Config.ADMIN_ID)))
def add_hod(client, message):
    try: # If empty comand is passed
        id_to_add = message.command[1]
    except IndexError:
        message.reply_text('Enter an ID after the command.')
        return
    try: # If the ID is entered as a string
        id_to_add = int(id_to_add)
    except Exception as e:
        print(e)
        message.reply_text('The ID should be a number.')
        return
    Config.STUDENTS_ID.append(id_to_add)

@bot.on_message(filters.command(['removeteacher']) & filters.chat(chats = (Config.HOD_ID + Config.PRINCIPAL_ID + Config.ADMIN_ID)))
def add_princi(client, message):
    try: # If empty command was passed
        id_to_add = message.command[1]
    except IndexError:
        print('IndexError')
        message.reply_text('Enter an ID after the command.')
        return
    try: # If string was passed instead of a Number
        id_to_add = int(id_to_add)
    except Exception as e:
        print(e)
        message.reply_text('The ID should be a number.')
        return
    Config.STUDENTS_ID.remove(id_to_add) # Remove the id from the Global Variable

@bot.on_message(filters.command(['addguest']) & filters.chat(chats = (Config.HOD_ID + Config.PRINCIPAL_ID + Config.ADMIN_ID)))
def add_hod(client, message):
    try: # If empty comand is passed
        id_to_add = message.command[1]
    except IndexError:
        message.reply_text('Enter an ID after the command.')
        return
    try: # If the ID is entered as a string
        id_to_add = int(id_to_add)
    except Exception as e:
        print(e)
        message.reply_text('The ID should be a number.')
        return
    Config.GUEST_ID.append(id_to_add)

@bot.on_message(filters.command(['removeguest']) & filters.chat(chats = (Config.HOD_ID + Config.PRINCIPAL_ID + Config.ADMIN_ID)))
def add_princi(client, message):
    try: # If empty command was passed
        id_to_add = message.command[1]
    except IndexError:
        print('IndexError')
        message.reply_text('Enter an ID after the command.')
        return
    try: # If string was passed instead of a Number
        id_to_add = int(id_to_add)
    except Exception as e:
        print(e)
        message.reply_text('The ID should be a number.')
        return
    Config.GUEST_ID.remove(id_to_add) # Remove the id from the Global Variable

@bot.on_message(filters.command(['adddept']) & filters.chat(chats = (Config.PRINCIPAL_ID + Config.ADMIN_ID)))
def add_dept(client, message):
    try: # If dept_id or dept_name was empty
        dept_id, dept_name = message.command[1], message.command[2]
    except Exception as e:
        print(e)
        message.reply_text('Did you enter it correctly? Check logs for more info.')
        return
    try: # If dept_id is NaN
        dept_id = int(dept_id)
    except ValueError:
        print('ValueError')
        message.reply_text('Department ID should be a Number')
        return

bot.run()
