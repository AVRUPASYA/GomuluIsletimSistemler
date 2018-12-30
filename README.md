# GomuluIsletimSistemleri<h1>
 <br>
<h2>Projenin genel tanımı ve amacı</h2><br>
<br> 
Akıllı Ev Sistemi, nano teknoloji ev otomasyonu ile geliştirilen bir kontrol sistemidir. Bu sistem, evlerde hem büyük bir konfor, hem de güvenlik sağlar. Sistemlerin kontrolü, ayrı ayrı kumandalar yerine, görsel bir paneli bulunan Web  aracılığıyla yapılmıştır.Veritabanı kullanılarak raspberry pi ile proje gerçekleşimi sağlanmıştır.Proje kontrol yapısını dünyanın her yerine ulaştırmada kolaylık sağlamıştır
<br>
 <br>
 <br>
<p>
<img align="center" width="500" height="300" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfuUW1DTZkOg6C6WhlTGwkIKYflG3_NSda12g1s51z8pETksD2">
</p>

<h2>Kullanılan teknolojiler</h2><br>
Python, nesne yönelimli, yorumlamalı, birimsel ve etkileşimli yüksek seviyeli bir programlama dilidir. Yorumlanan ve dinamik bir dil olan Python, esas olarak nesne tabanlı programlama yaklaşımlarını ve belli bir oranda da fonksiyonel programlamayı desteklemektedir.
Flask python ile çalışabileceğiniz çok güçlü ve bir o kadarda kolay öğrenilen minimal bir framework. O kadar kolayki python bilginiz olmasa bile bu framework ile çalışırken öğrenebilirsiniz. Flask küçük çaplı projeler için size hem hız kazandırır hemde gereksiz konfigrasyonlar ile boğuşmanızı önler.
&nbsp;&nbsp;&nbsp;&nbsp;<p>
<img align="left" width="350" height="300" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTN_04uVSv9oZdMmC4VuUwvrDb3bvDOYlKONjri27PNQ4Y416q0Gg" >
 <img align="center" width="350" height="300" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiLNB1g8cK7wS1fI0b9t-yr8qQxpaMreoPzbA_vuzVL6koQfEjkg">
</p>
<br>
<br>
Veritabanı olarak SQLite, dünyada en çok dağıtılan ve tavsiye edilen kaynak kodları halka açık, tamamen C/C++ programlama dilleriyle geliştirilmiş sunucu yazılımı ve yapılandırma gereksinimi olmayan, işlemsel ve ilişkisel bir SQL veritabanı ile buton işlemleri gerçekleştirilmiştir.

<h2>Sistem bileşen diyagramı</h2><br><br>
Sistemde butonlara basarak veritabanda bulunan sistemdeki yapılar açma-kapanma yöntemi ile veritabanında güncellenerek Phytonun flask web uygulaması ile açma  kapama işlemi veritabanına aktarılmaktadır.
Sistemin anasayfa yapısı aşağıdaki gibidir EKLE ve GÖSTER MENÜLERİYLE SAYFALARIMIZ yüklenicektir.
<br><br>
<br><p>
<img align="left" width="300" height="250" src="http://4gp.me/bbtc/1546124885172.jpg" >
 <img align="center" width="500" height="250" src="http://m.YollaYap.com/bbtc/1546125121206.jpg">
</p>
Aynı zamanda kod kısmımızda sag taraftadır!<br><br>
Gerekli Ev Aletlerinin Gösterilmesi için gerekli sayfa yapısı listeleme durumu aşağıdaki geniş bir ayayüz ekranıyla database bağlantısı sağlanılarak sağlanmıstır.Kod kısmı ve sayfa kodları aşağıdadır!<br><br>

<img align="left" width="450" height="400" src="http://4gp.me/bbtc/1546125697669.jpg" >
 <img align="center" width="400" height="400" src="http://4gp.me/bbtc/1546125760168.jpg">

<br>
<br>
Her bir butona basılıp Flask'ta route edilme kısmında yani ev aletlerinin web üzerinden Database ortamına aktarılıp üçer saniye aralıklarla otomatik güncelleme yapılıp sayfaya düstüğü aşamadır. <html> tagları içinde yazılmıştır sayfa yapısı! 
 <br>
<br>

<img align="left" width="500" height="300" src="http://4gp.me/bbtc/1546126302788.jpg" ><br> <br>Butonlardan gelen bilgiler flaskaap.py dosyasında route edilir ilgli link'den database güncellenir.<br><br>
Database bağlantısı SQLİTE veritabana bağlantısı kullanılarak  databaseteki  ilgili yerler açık veya kapalı olarak değiştirilmiştir!
 <br>
 <br>


 
 <br>
 <br>
  <br>
 <br>SQLİTE ve sayfa yapısındaki durumlar resimle gösterilmiştir!<br>
  <br><br>
  
 <img align="center" width="800" height="300" src="http://4gp.me/bbtc/1546127343450.jpg" >
 <br>
 <br>
 Raspberry pi GPIO kütüphaneleriyle gerekli emulatör kurulmuştur.Test için gerekli dosyalar sayfa yapısında bulunmaktadır.Veritabanında bulunan eşyalara göre GPIO giriş çıkışları sağlanarak emulatör de test ortamı kurulmuştur.<br>
 <br>
 <br>
 <br>
 <img align="left" width="400" height="300" src="http://4gp.me/bbtc/1546128013959.jpg" > Gerekli pin tanımlamaları her bir led ev eşyası düşünülerek ikişer butonla açma kapama işlemi yapılmış ve veri tabanına aktarılmıştır.<br>
  <br>
 <br>
 <br>
Butonlar yardımı ile kapatıp açma usulü led ile düşünülerek iki buton yardımı ile açma kapama işlemi gerçekleştirilmiştir!  <br>
 <br>
 <br>
 <img align="center" width="800" height="300" src="http://4gp.me/bbtc/1546128031122.jpg" >
