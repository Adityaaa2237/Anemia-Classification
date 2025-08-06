clear; clc;

% membaca data
data = readtable("C:\Users\HP\Documents\anemiaexcel.xlsx","VariableNamingRule","preserve");

% menyusun variabel data latih dan kelas latih
data_latih = table2array(data(2:1137,[2 3]));
kelas_latih = table2array(data(2:1137,6));

% plot data
x = data_latih(:,1); 
y = data_latih(:,2); 
figure
gscatter(x, y, kelas_latih, 'rb','o')
grid on
xlabel('Hemoglobin')
ylabel('MCH')
title('Klasifikasi K-Nearest Neighbor')

% klasifikasi
mdl = fitcknn(data_latih,kelas_latih,'NumNeighbors',3,'BreakTies','nearest','Standardize',true);

% memprediksi kelas hasil pelatihan
hasil_latih = predict(mdl,data_latih);

% menghitung akurasi hasil pelatihan
jumlah_latih = numel(hasil_latih);
tp1 = 0;
tn1 = 0;
fp1 = 0;
fn1 = 0;
for i = 1:jumlah_latih
    if hasil_latih(i) == 1 && kelas_latih(i) == 1
        tp1 = tp1+1;
    elseif hasil_latih(i) == 0 && kelas_latih(i) == 0
        tn1 = tn1+1;
    elseif hasil_latih(i) == 1 && kelas_latih(i) == 0
        fp1 = fp1+1;
    elseif hasil_latih(i) == 0 && kelas_latih(i) == 1
        fn1 = fn1+1;
    end
end
akurasi_pelatihan = (tp1+tn1)/jumlah_latih*100
recall_pelatihan = tp1/(tp1+fn1)*100
presisi_pelatihan = tp1/(tp1+fp1)*100

% confusion matrix
figure
evaluasi_pelatihan = confusionchart(kelas_latih,hasil_latih);

% data uji
data_uji = table2array(data(1138:1421,[2 3]));
kelas_uji = table2array(data(1138:1421,6));

% plot data
x = data_uji(:,1);
y = data_uji(:,2);

gscatter(x, y, kelas_uji,'brgy','x')
grid on
xlabel('Hemoglobin')
ylabel('MCH')
title('Klasifikasi K-Nearest Neighbor')
legend('nonanemic(uji)','anemic(uji)')
hold off

hasil_uji = predict(mdl,data_uji);

jumlah_uji = numel(hasil_uji);
tp2 = 0;
tn2 = 0;
fp2 = 0;
fn2 = 0;
for i = 1:jumlah_uji
    if hasil_uji(i) == 1 && kelas_uji(i) == 1
        tp2 = tp2+1;
    elseif hasil_uji(i) == 0 && kelas_uji(i) == 0
        tn2 = tn2+1;
    elseif hasil_uji(i) == 1 && kelas_uji(i) == 0
        fp2 = fp2+1;
    elseif hasil_uji(i) == 0 && kelas_uji(i) == 1
        fn2 = fn2+1;
    end
end
akurasi_pengujian = (tp2+tn2)/jumlah_uji*100
recall_pengujian = tp2/(tp2+fn2)*100
presisi_pengujian = tp2/(tp2+fp2)*100

figure
evaluasi_pengujian = confusionchart(kelas_uji,hasil_uji)