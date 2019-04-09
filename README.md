# GomuluIsletimSistemleri<h1>
 <br>
<h2>Projenin genel tanımı ve amacı</h2><br>
<br> 
Akıllı Ev Sistemi, nano teknoloji ev otomasyonu ile geliştirilen bir kontrol sistemidir. Bu sistem, evlerde hem büyük bir konfor, hem de güvenlik sağlar. Sistemlerin kontrolü, ayrı ayrı kumandalar yerine, görsel bir paneli bulunan Web  aracılığıyla yapılmıştır.Veritabanı kullanılarak raspberry pi ile proje gerçekleşimi sağlanmıştır.Proje kontrol yapısını dünyanın her yerine ulaştırmada kolaylık sağlamıştır
<br>
 <br>
 <br>
<p>
<img align="center" width="500" height="300" src="https://user-images.githubusercontent.com/43750173/55800518-92942c80-5adc-11e9-8779-9eccba123938.jpg">
</p>

<h2>Kullanılan teknolojiler</h2><br>
Python, nesne yönelimli, yorumlamalı, birimsel ve etkileşimli yüksek seviyeli bir programlama dilidir. Yorumlanan ve dinamik bir dil olan Python, esas olarak nesne tabanlı programlama yaklaşımlarını ve belli bir oranda da fonksiyonel programlamayı desteklemektedir.
Flask python ile çalışabileceğiniz çok güçlü ve bir o kadarda kolay öğrenilen minimal bir framework. O kadar kolayki python bilginiz olmasa bile bu framework ile çalışırken öğrenebilirsiniz. Flask küçük çaplı projeler için size hem hız kazandırır hemde gereksiz konfigrasyonlar ile boğuşmanızı önler.
&nbsp;&nbsp;&nbsp;&nbsp;<p>
<img align="left" width="350" height="300" src="https://user-images.githubusercontent.com/43750173/55800520-932cc300-5adc-11e9-8da8-9a1a9b3d65ba.jpg" >
 <img align="center" width="350" height="300" src="https://user-images.githubusercontent.com/43750173/55800521-93c55980-5adc-11e9-8b33-5581dd944f13.jpg">
</p>
<br>
<br>
Veritabanı olarak SQLite, dünyada en çok dağıtılan ve tavsiye edilen kaynak kodları halka açık, tamamen C/C++ programlama dilleriyle geliştirilmiş sunucu yazılımı ve yapılandırma gereksinimi olmayan, işlemsel ve ilişkisel bir SQL veritabanı ile buton işlemleri gerçekleştirilmiştir.
<h2>Sistem bileşen diyagramı</h2><br><br><br>Sistem bileşen diyagramı<br><br><br>
 <img align="center" width="800" height="400" src="https://user-images.githubusercontent.com/43750173/55799447-1862a880-5ada-11e9-97e6-6d75d7fcd065.jpg"><br><br><br>
<h2>Projenin Uygulama Aşamaları</h2><br><br>


Sistemde butonlara basarak veritabanda bulunan sistemdeki yapılar açma-kapanma yöntemi ile veritabanında güncellenerek Phytonun flask web uygulaması ile açma  kapama işlemi veritabanına aktarılmaktadır.
Sistemin anasayfa yapısı aşağıdaki gibidir EKLE ve GÖSTER MENÜLERİYLE SAYFALARIMIZ yüklenicektir.
<br><br>
<br><p>
<img align="left" width="300" height="250" src="https://user-images.githubusercontent.com/43750173/55800543-a0e24880-5adc-11e9-8073-993f2bc681e5.PNG" >
 <img align="center" width="500" height="250" src="https://user-images.githubusercontent.com/43750173/55800505-8e680f00-5adc-11e9-9c7f-ddf6f3c311a1.PNG">
</p>
Aynı zamanda kod kısmımızda sag taraftadır!<br><br>
Gerekli Ev Aletlerinin Gösterilmesi için gerekli sayfa yapısı listeleme durumu aşağıdaki geniş bir ayayüz ekranıyla database bağlantısı sağlanılarak sağlanmıstır.Kod kısmı ve sayfa kodları aşağıdadır!<br><br>

<img align="left" width="450" height="400" src="https://user-images.githubusercontent.com/43750173/55800526-958f1d00-5adc-11e9-94bc-b74b2f31847b.PNG" >
 <img align="center" width="400" height="400" src="https://user-images.githubusercontent.com/43750173/55800524-94f68680-5adc-11e9-9f50-124b5c785c9c.PNG">

<br>
<br>
Her bir butona basılıp Flask'ta route edilme kısmında yani ev aletlerinin web üzerinden Database ortamına aktarılıp üçer saniye aralıklarla otomatik güncelleme yapılıp sayfaya düstüğü aşamadır. <html> tagları içinde yazılmıştır sayfa yapısı! 
 <br>
<br>

<img align="left" width="500" height="300" src="https://user-images.githubusercontent.com/43750173/55800510-9031d280-5adc-11e9-8bef-d6f38e31d98a.PNG" ><br> <br>Butonlardan gelen bilgiler flaskaap.py dosyasında route edilir ilgli link'den database güncellenir.<br><br>
Database bağlantısı SQLİTE veritabana bağlantısı kullanılarak  databaseteki  ilgili yerler açık veya kapalı olarak değiştirilmiştir!
 <br>
 <br>


 
 <br>
 <br>
  <br>
 <br>SQLİTE ve sayfa yapısındaki durumlar resimle gösterilmiştir!<br>
  <br><br>
  
 <img align="center" width="800" height="300" src="https://user-images.githubusercontent.com/43750173/55800526-958f1d00-5adc-11e9-94bc-b74b2f31847b.PNG" >
 <br>
 <br>
 Raspberry pi GPIO kütüphaneleriyle gerekli emulatör kurulmuştur.Test için gerekli dosyalar sayfa yapısında bulunmaktadır.Veritabanında bulunan eşyalara göre GPIO giriş çıkışları sağlanarak emulatör de test ortamı kurulmuştur.<br>
 <br>
 <br>

 <img align="left" width="600" height="300" src="http://4gp.me/bbtc/1546128031122.jpg" > Gerekli pin tanımlamaları her bir led ev eşyası düşünülerek ikişer butonla açma kapama işlemi yapılmış ve veri tabanına aktarılmıştır.<br>
  
 <br>
 <br>
Butonlar yardımı ile kapatıp açma usulü led ile düşünülerek iki buton yardımı ile açma kapama işlemi gerçekleştirilmiştir! <br>
 <br>
 <br>
<br>Aynı zamanda internet üzerinde güncellemesi de sayfa yardımıyla 3 'er saniye aralıklarla güncellenerek gösterilmiştir!
<br>
 <br><br>
<p>
 <img align="center" width="800" height="400" src="http://4gp.me/bbtc/1546128735189.jpg">
</p><br><br><br>
<h2>Proje Sonuçları</h2> 
 <br>
<br> <br>
 Akıllı Ev Sistemi, web teknoloji ev otomasyonu ile geliştirilip veritabanına aktarılmıştır.İlk önce web sitesi üzerinde güncelleme yapıldı daha sonra raspberri pi üzerinde yapıldı en son iki uygulama aynı projede birleştirildi!En çok web sitesi üzerinden Emulatöre erişim de sıkıntı yaşandı yapılan diğer işlemler başarıyla gerçekleştirildi. 
 <br>
<br> <br>
 <img align="center" width="850" height="500" src="http://4gp.me/bbtc/1546185235742.jpg">
