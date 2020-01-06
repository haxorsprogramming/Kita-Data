<?php
session_start();
$link = new mysqli('192.168.23.23','dwiky','asalammualaikum','dbs_aplikasi_produksi');

$acakBahan = 'qwertyuioplkjhgfdsazxcvbnm';
$acak = str_shuffle($acakBahan);
$token = substr($acak, 0, 6);
echo $token;
$acakAngkaBahan = "123456789";
$acakAngkaPersediaan = substr(str_shuffle($acakAngkaBahan), 0, 3);
$acakAngkaPembelian = substr(str_shuffle($acakAngkaBahan), 0, 3);
$acakAngkaPemakaian = substr(str_shuffle($acakAngkaBahan), 0, 3);
$acakAngkaFrekuensi = substr(str_shuffle($acakAngkaBahan), 0, 1);
echo "<br/>".$acakAngkaPersediaan;
echo "<br/>".$acakAngkaPembelian;
echo "<br/>".$acakAngkaPemakaian;
echo "<br/>".$acakAngkaFrekuensi;
$link -> query("INSERT INTO tbl_data_produksi VALUES(null,'234sd','A001','1','2019','12','12','12,'12');");
?>
