import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import webbrowser

#2025 MASAK Verileri kullanarak hazırladığım verilerin görselleştirilmesi projem

#2025 MASAK kullandığım verilerin linki
#MASAK_2025 = "https://ms.hmb.gov.tr/uploads/sites/12/2026/04/FR-2025-a59599f8141eec0b.pdf"
#webbrowser.open(MASAK_2025)

yukumlu_sayisi_2025 = 559
yukumlu_sayisi_2024 = 442
supheli_islem_bildirim_sayisi_2025 = 464.010
supheli_islem_bildirim_analiz_orani = "yüzde 71"
analiz_edilen_supheli_islem_bildirim_sayisi = 329.150

supheli_islem_gonderen_yukumlulerin_dagilimi_2025 = {
    "yükümlüler" : ["Bankalar","Ödeme Kuruluşları ile Elektronik Para Kuruluşları","Kripto Varlık Hizmet Sağlayıcılar",
                    "Diğer","Talih ve Bahis Oyunları Alanında FAaliyet Gösterenler"],
    "yükümlülerin oranları" :[57.2,24.1,13.2,3.9,1.6]

}

df_supheli_islem_gonderen_yukumlulerin_dagilimi_2025 = pd.DataFrame(supheli_islem_gonderen_yukumlulerin_dagilimi_2025)
print(df_supheli_islem_gonderen_yukumlulerin_dagilimi_2025)


supheli_islem_bildirimlerinin_suc_kategorilerine_gore_dagilimi_2025 = {
    "Suç kategorileri" :["Dolandırıcılık","Bilişim Suçları","Başkası hesabına işlem yapıldığının beyan edilmemesi",
                         "yasa dışı bahis/kumar","diğer"],
    "suç kategorileri yüzde" :[65.3,16.7,12.2,4.0,3.2]

}

df_supheli_islem_bildirimlerinin_suc_kategorilerine_gore_dagilimi_2025 = pd.DataFrame(supheli_islem_bildirimlerinin_suc_kategorilerine_gore_dagilimi_2025)
print(df_supheli_islem_bildirimlerinin_suc_kategorilerine_gore_dagilimi_2025)


#yükümlü dagilimina göre şib
plt.style.use('seaborn-v0_8')
plt.figure(figsize =(9,6))


sns.barplot(x = "yükümlüler", y = "yükümlülerin oranları", data =df_supheli_islem_gonderen_yukumlulerin_dagilimi_2025 , palette = "Blues" )
plt.title("MASAK Şüpheli İşlem Gönderen Yükümlülerin Dağılımı")
plt.xlabel("yükümlüler")
plt.ylabel("yükümlülerin oranları")
plt.show()

sns.barplot(x = "Suç kategorileri",y = "suç kategorileri yüzde" ,data = df_supheli_islem_bildirimlerinin_suc_kategorilerine_gore_dagilimi_2025, palette="Reds")
plt.title("MASAK Şüpheli İşlem bildirimlerinin Suç Kategorilerine Göre Dağılımı")
plt.xlabel("Suç kategorileri")
plt.ylabel("suç kategorileri yüzde")
plt.show()



