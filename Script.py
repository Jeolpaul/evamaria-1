class script(object):
    CMD_LIST = """๐๐ข {},
โข /id - get id of a specifed user. 
โข /info  - get information about a user. 
โข /imdb  - get the film information from IMDb source. 
โข /search  - get the film information from various sources. 
โข /whois :-give a user full details 

 แดสษชs ษชs าแดส แดแดแดษชษดs 

โข /logs - to get the rescent errors 
โข /stats - to get status of files in db. 
โข /delete - to delete a specific file from db. 
โข /users - to get list of my users and ids. 
โข /chats - to get list of the my chats and ids 
โข /leave  - to leave from a chat. 
โข /disable  -  do disable a chat. 
โข /ban  - to ban a user. 
โข /unban  - to unban a user. 
โข /channel - to get list of total connected channels 
โข /broadcast - to broadcast a message to all users. 
โข /connect  - connect a particular chat to your PM. 
โข /disconnect  - disconnect from a chat. 
โข /connections - list all your connections. 
โข /pin :- Pin The Message You Replied To Message To Send A Notification To Group Members. 
โข /unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message. 
โข /filter - add a filter in chat. 
โข /filters - list all the filters of a chat. 
โข /del - delete a specific filter in chat. 
โข /delall - delete the whole filters in a chat (chat owner only)"""

    HELP_TXT = """Help๐๐ป"""

    FILE_TXT = """โค ๐๐๐ฅ๐ฉ: ๐๐ข๐ฅ๐ ๐๐ญ๐จ๐ซ๐ ๐๐จ๐๐ฎ๐ฅ๐../
<b>๐ฑ๐ ๐๐๐ธ๐ฝ๐ถ ๐๐ท๐ธ๐ ๐ผ๐พ๐ณ๐๐ป๐ด ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐พ๐๐ด ๐ต๐ธ๐ป๐ด๐ ๐ธ๐ฝ ๐ผ๐ ๐ณ๐ฐ๐๐ฐ๐ฑ๐ฐ๐๐ด ๐ฐ๐ฝ๐ณ ๐ธ ๐๐ธ๐ป๐ป ๐ถ๐ธ๐๐ด ๐๐พ๐ ๐ฐ ๐ฟ๐ด๐๐ผ๐ฐ๐ฝ๐ด๐ฝ๐ ๐ป๐ธ๐ฝ๐บ  ๐๐พ ๐ฐ๐ฒ๐ฒ๐ด๐๐ ๐๐ท๐ด ๐๐ฐ๐๐ด๐ณ ๐ต๐ธ๐ป๐ด๐.๐ธ๐ต ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐ฐ๐ณ๐ณ ๐ต๐ธ๐ป๐ด๐ ๐ต๐๐พ๐ผ ๐ฐ ๐ฟ๐๐ฑ๐ป๐ธ๐ฒ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐ด๐ฝ๐ณ ๐๐ท๐ด ๐ต๐ธ๐ป๐ ๐ป๐ธ๐ฝ๐บ ๐พ๐ฝ๐ป๐  ๐พ๐ ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐ฐ๐ณ๐ณ ๐ต๐ธ๐ป๐ด๐ ๐ต๐๐พ๐ผ ๐ฐ  ๐ฟ๐๐ธ๐๐ฐ๐๐ด ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ๐ ๐ผ๐๐๐ ๐ผ๐ฐ๐บ๐ด ๐ผ๐ด ๐ฐ๐ณ๐ผ๐ธ๐ฝ ๐พ๐ฝ ๐๐ท๐ด ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ ๐ฐ๐ฒ๐ฒ๐ด๐๐ ๐ต๐ธ๐ป๐ด๐...//</b>
โชผ ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐?๐ โบ
โช /plink โบโบ <b>๐๐ด๐ฟ๐ป๐ ๐๐พ ๐ฐ๐ฝ๐ ๐ผ๐ด๐ณ๐ธ๐ฐ ๐๐พ ๐ถ๐ด๐ ๐ป๐ธ๐ฝ๐บ.</b>
โช /pbatch โบโบ <b>๐๐๐ด ๐๐พ๐๐ ๐ผ๐ด๐ณ๐ธ๐ฐ ๐ป๐ธ๐ฝ๐บ ๐๐ธ๐๐ท ๐๐ท๐ธ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ.</b>
โช /batch โบโบ <b>๐๐พ ๐ฒ๐๐ด๐ฐ๐๐ด ๐ป๐ธ๐ฝ๐บ ๐ต๐พ๐ ๐ผ๐๐ป๐๐ธ๐ฟ๐ป๐ด ๐ต๐ธ๐ป๐ด๐.</b>
โชผ ๐๐ฑ๐๐ฆ๐ฉ๐ฅ๐ โบ
<code>/batch https://t.me/beta_updates/201 https://t.me/beta_updates/257</code>"""
 
    MUSIC_TXT = """๐ท๐ด๐ ๐ผ๐ฐ๐ฝ!
You Can Rename Files With permanent Thumbnail
Just Send Me Any File And Reply It By
/rename Command

For Setting Thumb Just Send Me Any Image to set Thumb"""

    BOT_TXT = """๐๐ข {},
โช How To Use This Bot

/update - To Join Our Main Channel, You can use this ๐"""
    UPDATE_CMD = """๐๐ข {}, 
โช To Working of This Bot, Join the Main Channel Below 

โช Joining Because of Updates of Bots and All Others are through Main Channel

โช It is because of Copyright Issue is Very Low Compairing to Other Channels ๐"""
    START_TXT = """Hแดส {},
๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด ๐ธ๐ <a href=https://t.me/{}>{}</a>,\n ๐ธ ๐ฒ๐ฐ๐ฝ ๐ฟ๐๐พ๐๐ธ๐ณ๐ด ๐ผ๐พ๐๐ธ๐ด๐, ๐น๐๐๐ ๐ฐ๐ณ๐ณ ๐ผ๐ด ๐๐พ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ ๐ฐ๐ฝ๐ณ ๐ผ๐ฐ๐บ๐ด ๐ผ๐ด ๐ฐ๐ณ๐ผ๐ธ๐ฝ..."""
    SOURCE_TXT = """<b>NOTE:</b>
- This is a Eva Mari Project
href=https://github.com/EvamariaTG/EvaMaria>EVA MARIA</a>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. This Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- This Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Beta_Bot_Updates)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""

    ABOUT_TXT = """Hey, My Name Is {}, \nMade With โค๏ธ By Jeol"""

    STATUS_TXT = """แโบ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
แโบ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
แโบ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
แโบ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> """
 
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
 
