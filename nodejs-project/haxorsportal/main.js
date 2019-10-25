const path = require('path');
var express = require('express');
const hbs = require('hbs');
//use bodyParser middleware
const bodyParser = require('body-parser');
//use mysql database
const mysql = require('mysql');
var app = express();
app.use(bodyParser.urlencoded({extended:false}));

const conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'nusaID@201910',
  database: 'dbs_haxors'
});

conn.connect((err) =>{
  if(err) throw err;
  console.log('Mysql Connected...');
});
//endpoint home
app.get('/', function(req, res){
  res.send("Node test");
});
//endpoint => mahasiswa (get)
app.get('/mahasiswa/:nama', function(req, res){
    let nama = req.params.nama;
    let sql = "SELECT * FROM tbl_profile where username='"+nama+"';";
    conn.query(sql, function (err, result, fields) {
    if (err) throw err;
    res.json(result);
  });
});
//endpoint => mahasiswa (post)
app.post('/mahasiswa',function(req, res){
  let nama = req.body.nama;
  var data = {
    'nama' : nama
  }
  res.json(data);
});

//jalankan server
app.listen(8080, () => {
  console.log('Server sedang berjalan ... ');
});
