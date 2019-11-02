from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://rss.acast.com/losersclub"
url2 = "https://rss.acast.com/theopus"
url3 = "https://rss.acast.com/consequenceofsound"
url4 = "https://rss.acast.com/thismustbethegig"
url5 = "https://rss.acast.com/discography"
url6 = "https://rss.acast.com/filmography"
url7 = "https://rss.acast.com/halloweenies"
url8 = "https://rss.acast.com/kylemeredith"
url9 = "https://rss.acast.com/fifthdimension"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30099),
            'path': "http://rfcmedia.streamguys1.com/consequence.mp3",
            'thumbnail': "https://cdn-profiles.tunein.com/s308323/images/logoq.png",
            'is_playable': True},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://consequenceofsound.net/wp-content/uploads/2018/04/king1000-png-red-text.png"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://consequenceofsound.net/wp-content/uploads/2018/11/opus-dylan_final-e1542655628913.jpg"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://consequenceofsound.net/wp-content/uploads/2018/04/cospod-horiz.png"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://consequenceofsound.net/wp-content/uploads/2018/04/tmbtg-horizontal.png"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://consequenceofsound.net/wp-content/uploads/2018/04/discography-horizontal.png"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://consequenceofsound.net/wp-content/uploads/2018/06/filmography-kubrick-horizontal-2.png"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://consequenceofsound.net/wp-content/uploads/2019/02/halloweenies-horizontal.png"},
        {
            'label': plugin.get_string(30008),
            'path': plugin.url_for('episodes8'),
            'thumbnail': "https://consequenceofsound.net/wp-content/uploads/2018/05/kyle-meredith-horiz.png"},
        {
            'label': plugin.get_string(30009),
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://thumborcdn.acast.com/pVzS9Kn5eYpIDpLav1ds0Q4Irgg=/3000x3000/https://mediacdn.acast.com/assets/c838ff43-d9ac-4636-8b24-93b34dce5b69/cover-image-jvsbpekc-fifth_dimension_album_art.png"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)   
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items
@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items
@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items
@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7) 
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items
@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(url8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items
@plugin.route('/episodes9/')
def episodes9():
    soup9 = mainaddon.get_soup9(url9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items
if __name__ == '__main__':
    plugin.run()
