$cöp_ayırmaimport discord
import random

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

liste=["Güzel yarınlar için çevrene bak.","Çevre bize emanettir, geleceğe mirastır","Doğal hayatı koru, gelecek için bir adım at"]

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$cevreyikoruma'):
        await message.channel.send(
            "**🌍 Çevreyi Koruma İçin Yapabileceklerin:**\n\n"
            "**♻ 1. Geri Dönüşüm ve Atık Azaltma**\n"
            "- Plastik, cam, kağıt ve metal atıkları geri dönüştür.\n"
            "- Tek kullanımlık plastikleri (pipet, poşet, plastik şişe vb.) azalt.\n"
            "- Organik atıkları kompost yaparak değerlendir.\n\n"
            
            "**💡 2. Enerji Tasarrufu**\n"
            "- Gereksiz ışıkları ve elektronik cihazları kapat.\n"
            "- Enerji tasarruflu ampuller (LED) kullan.\n"
            "- Çamaşır ve bulaşık makinelerini dolu çalıştır.\n\n"

            "**🚰 3. Su Kullanımını Azaltma**\n"
            "- Musluğu gereksiz yere açık bırakma.\n"
            "- Kısa duş al, damlatan muslukları tamir et.\n"
            "- Bahçeni veya bitkilerini sabah erken ya da akşam sulayarak suyu verimli kullan.\n\n"

            "**🚶‍♂️ 4. Ulaşımda Daha Çevreci Seçenekler**\n"
            "- Kısa mesafelerde yürüyerek veya bisikletle git.\n"
            "- Toplu taşıma kullan veya araç paylaşımı yap.\n"
            "- Elektrikli veya hibrit araçları tercih etmeyi düşün.\n\n"

            "**🛍 5. Çevre Dostu Ürünler Kullan**\n"
            "- Kimyasal içermeyen temizlik malzemeleri seç.\n"
            "- Yerel ve organik ürünler alarak karbon ayak izini azalt.\n"
            "- Dayanıklı ve uzun ömürlü ürünler kullan, ihtiyacın olmayan şeyleri alma.\n\n"

            "**🌱 6. Doğayı Koru**\n"
            "- Ağaç dik ve yeşil alanları koru.\n"
            "- Denizleri ve ormanları temiz tut, çöplerini doğaya bırakma.\n"
            "- Yerel çevre koruma projelerine katıl."
        )
    if message.content.startswith('$cevreslogan'):
        random_slogan = random.choice(liste)  
        await message.channel.send(random_slogan)
    if message.content.startswith("$cöp_ayırma"):
        await message.channel.send("""**♻ ÇÖP AYRIŞTIRMA NASIL YAPILIR?**  

**1️⃣ Geri Dönüştürülebilir Atıklar (Mavi Kutu / Geri Dönüşüm Kutusu)**  
Bu kategoriye giren atıklar geri dönüşüm tesislerinde işlenebilir.  

✅ **Kağıt ve Karton:**  
- Gazete, dergi, kitap, karton kutular, kağıt ambalajlar  
- Kullanılmış A4 kağıtlar (temiz ve kuru olmalı)  

✅ **Plastik:**  
- Plastik şişeler, yoğurt kapları, poşetler  
- Deterjan ve şampuan şişeleri (temizlenmiş olmalı)  

✅ **Cam:**  
- Cam şişeler, kavanozlar, pencere camları (PVC camlar hariç)  

✅ **Metal:**  
- Alüminyum kutular (kola, meyve suyu kutuları)  
- Konserve kutuları  
""")
    
    

client.run("TOKEN")
