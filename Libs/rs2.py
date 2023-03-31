"""
Random Sentences(rs) library second version. It was started to be written on 2023.02.16 at 20:00.
Written by developer Mahmut P. It was written to be used in many projects, especially Mah-Framework.
It was written to be used in many projects, especially Mah-Framework. Shared as open source code.
My only request from the people who use it: they give me feedback, I would appreciate it if you do :)
rs legacy: https://github.com/C0derByM4H6301/mah-framework/blob/main/lib/rs.py
"""
import random
class RS2:
    Version = 2.0
    liste = [
        "Öğüt vermek kolay , Örnek olmak zordur...",
        "hücum için hazır ol çünkü her an savaş var",
        "Zafer için çabala ve savaş",
        "Emin olmak zor...",
        "Adım Erkan olmadığından Mahmut'u seviyorum",
        "Bir oyuncunun değer verdiği bir karekter: Kamikaze Xaero",
        "iki kişi hata yaptı birisi yüzü için sevdi,\n birisi sevmeyeceği bildiği halde sevdi",
        "Süleyman Çakır (d. 1964 - ö. 8 Nisan 2004)",
        "Klavyem kesici aletlerimden daha çok can yakar.\n Mahmut P.",
        "Eğer bir gün benim sözlerim bilimle ters düşerse bilimi seçin. \n Mustafa Kemal Atatürk",
        "Beni görmek demek mutlaka yüzümü görmek demek değildir. Benim fikirlerimi, benim duygularımı anlıyorsanız ve hissediyorsanız bu yeterlidir.\n Mustafa Kemal Atatürk",
        "Dünyada her şey için, medeniyet için, hayat için, başarı için, en hakiki mürşit bilimdir, fendir.\n Mustafa Kemal Atatürk",
        "Bilim ve fen nerede ise oradan alacağız ve her ulus kişisinin kafasına koyacağız. Bilim ve fen için kayıt ve şart yokur.\n Mustafa Kemal Atatürk",
        "Bir millet ki resim yapmaz, bir millet ki heykel yapmaz, bir millet ki tekniğin gerektirdiği şeyleri yapmaz, itiraf etmeli ki o milletin ilerleme yolunda yeri yoktur.\n Mustafa Kemal Atatürk",
        "Bir millet eğitim ordusuna sahip olmadıkça, savaş meydanlarında ne kadar parlak zaferler elde ederse etsin, o zaferlerin kalıcı sonuçlar vermesi ancak eğitim ordusuyla mümkündür.\n Mustafa Kemal Atatürk",
        "Gençliği yetiştiriniz. Onlara ilim ve irfanın müspet fikirlerini veriniz. Geleceğin aydınlığına onlarla kavuşacaksınız.\ Mustafa Kemal Atatürk",
        "“Sizden farklı düşünen insanların savlarını da dinleyin. Yalnız dikkat edin, cümlenin içerisinde ‘düşünen’ ibaresi var. Bu ayrımı iyi yapın.”\n İlber Ortaylı",
        "“Cahillik hiç ayıplanacak bir şey değildir hatta cahil tutarlıdır kendi içinde. Kötü olan yarı cahillerdir.”\n İlber Otaylı",
        "Ben milletime ikiyüzlülüğü yakıştıramıyorum.\n Çelal Şengör",
        "Bilim gerçeği bulduğunu değil, yanlışı teşhis edip onu elediğini iddia eder.\n Çelal Şengör",
        "Dünyanın neresinde din egemen olmuşsa, ahlaksızlık tavana vurmuştur.\n Çelal Şengör",
        "Klavyem kesici aletlerimden daha çok can yakar.\n Mahmut P.",
        "Din-bilim diyaloğu olacaksa, ya bilimi adam gibi öğreneceksin, ya bilimden gelen adamlara saygı göstereceksin.\n Çelal Şengör",
        "Hiç kimse her şeyi bilemez.\n Çelal Şengör",
        "Görüşüne katılalım katılmayalım, hiçbir tarihi karakteri aşağılamamak lazım, insan olmak lazım. \n Çelal Şengör",
        "Eğer bu dünya bir gün kıtlık ve sefalet yaşarsa biz insanları din değil, bilim kurtaracak.\n Çelal Şengör",
        "İnançlar hakikat düşmanları olarak, yalanlardan daha tehlikelidir.\n Friedrich Nietzsche",
        "Ruh arayanda, hiç ruh yoktur.\n Friedrich Nietzsche",
        "Öyle bir hava vardır; esaret gören kimseler, başkalarını ezmeyi sever.\n İlber Ortaylı"
        ]
    def all():
        for i in RS2.liste:
            print(i)
    def random():
         return random.choice(RS2.liste)
            
            