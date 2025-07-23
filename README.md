# Kitap Verileri Web Scraping Uygulaması

Bu Python uygulaması, belirlenen bir çevrimiçi kitap mağazasından kitap adları, stok durumları, fiyatlar ve ürün linkleri gibi önemli bilgileri çeker. Çekilen veriler, analiz için kolayca kullanılabilecek bir `.csv` (Comma Separated Values) dosyasına kaydedilir.

## Ne Yapar?

* **Kitap Bilgileri Çekimi:** Hedef sitedeki kitapların başlıklarını, stok durumlarını, fiyatlarını ve doğrudan ürün linklerini toplar.
* **Veri Kaydı (CSV):** Çekilen tüm verileri düzenli bir `.csv` dosyasına kaydeder.
* **Hızlı ve Etkin:** Statik HTML içeriğinden veri çekmek için optimize edilmiştir.

## Neden Önemli?

E-ticaret sektöründe veya kitap endüstrisinde faaliyet gösterenler için güncel ürün ve stok bilgisi kritik öneme sahiptir. Bu uygulama:

* **Piyasa Takibi:** Rakip sitelerdeki fiyat ve stok değişikliklerini hızlıca takip etme imkanı sunar.
* **Veriye Dayalı Kararlar:** Toplanan güncel ve doğru verilerle daha bilinçli iş kararları almanızı sağlar.

## Kullanılan Teknolojiler

* **Python:** Uygulamanın geliştirildiği ana programlama dili.
* **`requests` Kütüphanesi:** Web sitelerinden HTML içeriği almak için kullanılır.
* **`BeautifulSoup` Kütüphanesi:** Çekilen HTML içeriğini kolayca ayrıştırmak ve veri ayıklamak için kullanılır.

## Nasıl Çalışır?

1.  Uygulama, belirlenen kitap satış sitesine HTTP isteği gönderir ve sayfanın HTML içeriğini alır.
2.  `BeautifulSoup` kullanarak bu HTML içeriğini analiz eder.
3.  Her bir kitap için başlık, stok durumu, fiyat ve ürün linki gibi bilgileri tespit eder ve çeker.
4.  Bu DataFrame'i `kitap_verileri.csv` adında bir CSV dosyasına kaydeder.
