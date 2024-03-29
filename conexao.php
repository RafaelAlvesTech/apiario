<?php 

file_get_contents('php://input');

e


$banco = "medesp76_apiario";
$host = "br204.hostgator.com.br";

$usuario = "medesp76_master";
$senha = "mb@2022"


header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8"); 
header("Access-Control-Allow-Methods: POST,GET,DELETE,PUT,HEAD,OPTIONS");
header("Access-Control-Allow-Headers: X-Authorization,X-Requested-With,XMLHttpRequest");


date_default_timezone_set("America/Sao_Paulo");

try {
    $pdo = new PDO("mysql:dbname=$banco;host=$host;charset=utf8", "$usuario", "$senha");

     $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

} catch (Exception $e) {
    echo "Erro ao conectar com o banco de dados! ".$e;
}
?>