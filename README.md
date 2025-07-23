# Iris Veri Setinde Kümeleme ve Sınıflandırma: K-Means ve Lojistik Regresyon Yaklaşımı

Bu proje, klasik makine öğrenmesi algoritmaları olan **K-Means Kümeleme** ve **Lojistik Regresyon Sınıflandırma** yöntemlerini kullanarak, popüler **Iris veri seti** üzerinde temel veri analizi, kümeleme ve sınıflandırma uygulamalarını içermektedir.

## İçerik

- Veri setinin incelenmesi ve ön işlenmesi
- K-Means algoritması ile kümelere ayırma (clustering)
- Lojistik Regresyon ile sınıflandırma (classification)
- Sonuçların ve metriklerin görselleştirilmesi

## Kullanılan Kütüphaneler

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Projeyi Çalıştırma

1. **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install numpy pandas matplotlib seaborn scikit-learn
    ```
2. **Kod dosyasını çalıştırın:**
    - `reg&conf.py` dosyasını Python ortamınızda veya Google Colab’da çalıştırabilirsiniz.

3. **Veri seti**: Kod içinde otomatik olarak sklearn veya CSV dosyasıyla yüklenmektedir.

## Proje Akışı

1. **Veri Ön İşleme:**  
   - Eksik veriler, veri tipi kontrolleri, temel istatistiksel özetler ve görselleştirme (histogram, pairplot, heatmap).

2. **Kümeleme (K-Means):**  
   - 3 farklı iris türünü otomatik olarak kümelere ayırır, sonuçları scatter plot ile görselleştirir.

3. **Sınıflandırma (Lojistik Regresyon):**  
   - Eğitim ve test seti ayrımı (%80-%20), model eğitimi ve doğruluk/performans metriklerinin raporlanması.

4. **Görselleştirme:**  
   <img width="373" height="248" alt="image" src="https://github.com/user-attachments/assets/2c22f8e0-e1db-4166-978e-fe83b4868055" />


## Sonuçlar

- K-Means algoritması ile kümeler başarıyla ayrılmıştır.
- Lojistik Regresyon modeliyle yüksek doğruluk elde edilmiştir.
- Sonuçlar confusion matrix ve classification report ile detaylandırılmıştır.

## Katkıda Bulunanlar

- **Mert ULUSOY**  
  
  Izmir Demokrasi Üniversitesi  
  mertulusoyclass@gmail.com

## Kaynakça

- Fisher, R.A. (1936). "The use of multiple measurements in taxonomic problems." Annals of Eugenics, 7(2), 179-188.
- scikit-learn documentation: https://scikit-learn.org/
- [Kaggle: Iris Species Dataset](https://www.kaggle.com/datasets/uciml/iris)

---

