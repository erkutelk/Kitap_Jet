var kitap_ismi = document.querySelectorAll(".box-info>h2>a");
var kitap_yayinevi = document.querySelectorAll(".box-info>h3:nth-child(2)");
var kitap_yazar = document.querySelectorAll(".box-info>h3:nth-child(3)");
var kitap_fiyat = document.querySelectorAll(".price-box>p>span:nth-child(2)>span");
var kitap_stok = document.querySelectorAll(".special-price:nth-child(2)>.price:nth-child(2)");
var kitap_iskonto = document.querySelectorAll(".iskontolu>span>span");

kitap_ismi.forEach(function(item, index) {
  var isim = item.textContent.trim();
  var yayinEvi = kitap_yayinevi[index] ? kitap_yayinevi[index].textContent.trim() : "Bilinmiyor";
  var yazar = kitap_yazar[index] ? kitap_yazar[index].textContent.trim() : "Bilinmiyor";
  var fiyat = kitap_fiyat[index] ? kitap_fiyat[index].textContent.trim() : "Fiyat Bilgisi Yok";
  var stok = kitap_stok[index] ? kitap_stok[index].textContent.trim() : "Stok Durumu Bilgisi Yok";
  var iskonto = kitap_iskonto[index] ? kitap_iskonto[index].textContent.trim() : "İndirim Bilgisi Yok";

  console.log(`Kitap Adı: ${isim} | Yayınevi: ${yayinEvi} | Yazar: ${yazar} | Fiyat: ${fiyat} | Stok Durumu: ${stok} | İndirim: ${iskonto}`);
});
