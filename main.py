
import telebot
bot = telebot.TeleBot("6843685082:AAHeTwi1J9mWBJ93oWPQMEIfh3C-VPgkJNE")



from bs4 import BeautifulSoup
import requests

def getlink():
  url="https://bingotingo.com/best-social-media-platforms/"
  page=requests.get(url)
  html=page.content
  soup = BeautifulSoup(html,"html.parser") 
  job_desc = soup.find(
    'a', 
    class_='su-button su-button-style-soft su-button-wide')
  l = str(job_desc)
  list = l.split()
  for i in list:
    if "href" in i:
      j = (i.lstrip('href='))
      job_desc=j.replace('"', '')
      
  
    
  
  url2=job_desc
  page2=requests.get(url2)
  html2=page2.content
  soup2 = BeautifulSoup(html2,"html.parser")
  div = soup2.find(
    'div',class_="public-container noselect")
  div2=div.find('div',class_='pb-links justify-content-center pb-links-noimg row m-0 effect-standard dl-LAYOUT_LIST_SMALL_RND ml-LAYOUT_LIST_SMALL_RND group-container-u')
  a=div2.find('a',class_="d-block pb-linkbox pb-desktop-list-small-rnd pb-mobile-list-small-rnd bt-2 mb-2 col-md-12 col-12")
  hi = str(a)
  li = hi.split()
  b=''
  for i in li:
    if "href" in i:
      b = (i.lstrip('href='))
  g=b.replace('"', '')
  print(g)
  finallink=f'https://ln.ki{g}'
  def remove(string):
    return string.replace(" ", "") 
  if "canva" in finallink:
      return remove(finallink)
  else:
      return "Will be available in few Hours"



@bot.message_handler(commands=['start'])
def send_link(message):
    chat_id = message.chat.id
    link = getlink()
    markup = telebot.types.InlineKeyboardMarkup()
    if link == "will be available in 1hr":
     bot.send_message(chat_id, f"will be available in 1hr{link}")
    else:
     btn_link = telebot.types.InlineKeyboardButton(text="Get canva pro", url=link)
     markup.add(btn_link)
     bot.send_message(chat_id, "Click the button below to access the link:", reply_markup=markup)


print("Bot is running")
bot.polling()
