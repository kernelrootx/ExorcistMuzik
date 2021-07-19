# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Merhaba 👋 [{}](tg://user?id={})!**\n\n🤖 Ben telegram gruplarına Sesli sohbetlerde Müzik calmak icin yapıldım & Hoşgeldin\n\n✅ Bana  /help yazarak bilgi alabirsin."
      HELP_MSG = [
        ".",
f"""
**Hey ♪ tekrar Hoş Geldiniz {PROJECT_NAME}

⚪️ {PROJECT_NAME} grubunuzun sesli sohbetinde ve kanal sesli sohbetlerinde müzik çalabilir

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**Ayarlama**

1) bot admin olun (cplay kullanıyorsanız grup ve kanalda)
2) sesli sohbet başlatın
3) bir yönetici tarafından ilk kez [şarkı adı] çalmayı /çalmayı deneyin
* ) Userbot katıldıysa, müzik keyfini çıkarın, değilse grubunuza @{ASSISTANT_NAME} ekleyin ve tekrar deneyin

** Kanal Müzik Çalma İçin**
1) beni kanalınızın yöneticisi yapın 
2) bağlantılı grupta / userbotjoinchannel Gönder
3) Şimdi bağlantılı grupta komutlar gönderin
""",
f"""
**Commands**

**=>> Song Playing 🎧**

- /oynat: Müzüği başlatir
- /oynat: [yt url] : Belirlediginiz Yt url atarsanız calısır
- /oynat: [reply yo audio]: her hangi bi muzugi aratabilirsin
- /dplay: Deezerden Müzik acabilirsiniz
- /splay: sp Platformdan Müzüğinizi baslatir
- /ytplay: Youtubeden Müzik çalar

**=>> Playback ⏯**

- /player: Müzük Menüsü Açılır
- /atla: Müzüği atlarsınız
- /durdur: Müzik durur
- /devam: Müzik devam eder
- /bitir: Durur medya lı müzik
- /current: Geçerli çalma parçasını gösterir
- /playlist: Çalma listesini gösterir

*Player cmd ve /play, /current ve /playlist dışındaki diğer tüm cmd'ler yalnızca grubun yöneticileri içindir.
""",

f"""
**=>> Channel Music Play 🛠**

✔ Sadece bağlı grup yöneticileri için:

- /cplay [şarkı adı] - istediğiniz şarkıyı çalın
- /cdplay [şarkı adı] - deezer aracılığıyla istediğiniz şarkıyı çalın
- /csplay [şarkı adı] - jio saavn aracılığıyla istediğiniz şarkıyı çalın
- /cplaylist-şimdi çalma listesini göster
- /cccurrent-şimdi göster oynuyor
- /cplayer-açık müzik çalar ayarları paneli
- /cpause-şarkı çalmayı Duraklat
- /cresume-şarkı çalmaya devam et
- /cskıp-bir sonraki şarkıyı çal
- /cend-müzik çalmayı Durdur
- /userbotjoinchannel-asistanınızı sohbetinize davet edin

kanal c yerine de kullanılabilir (/cplay = / channelplay )

⚪️ Eğer böyle oynamaya donlt varsa bağlı grup içinde :

1) kanal kimliğinizi alın.
2) tittle ile bir grup oluşturun: Kanal müzik: your_channel_id
3) tam perma ile kanal yöneticisi olarak bot ekleyin
4) kanala yönetici olarak @{ASSISTANT_NAME} ekleyin.
5) sadece grubunuza komutlar gönderin. (bunun yerine /ytplay /play kullanmayı unutmayın)
""",

f"""
**=>> Daha fazla araç 🧑🔧**

- /musicplayer [on / off]: müzik çaları Etkinleştir / devre dışı bırak
- /admincache: grubunuzun yönetici bilgilerini günceller. Bot yönetici tarafından tanınmıyorsa deneyin
- /asistanekle: @{ASSISTANT_NAME} kullanıcısını sohbetinize davet edin
""",
f"""
**=>> Şarkı İndir 🎸**

- /video [şarkı mame]: youtube'dan Video şarkı indir
- /song [şarkı adı]: youtube'dan ses şarkısı indir
- /saavn [şarkı adı]: saavn'dan şarkı indir
- /deezer [şarkı adı]: deeze'den şarkı indir

**=>> Arama Araçları 📄**

- /search [şarkı adı]: şarkılar için YouTube'da arama yapın
- /lyrics sözleri [şarkı adı]: Şarkı Sözleri alın
""",

f"""
**=>> Sudo kullanıcıları için komutlar:**

 - /asistantamamencikar-Asistanı tüm sohbetlerden Kaldır
 - /broadcast <Mesaja cevap ver> - global olarak brodcast tüm sohbetlere mesaj yanıtladı
 - /pmpermit [açık/kapalı] - pmpermit mesajını Etkinleştir/devre dışı bırak
*Sudo kullanıcıları herhangi bir gruptaki herhangi bir komutu çalıştırabilir

"""
      ]
