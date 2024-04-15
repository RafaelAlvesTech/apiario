<?php 

include_once("../conexao.php");



$id          = $_POST['id'];
$token       = $_POST['token'];


$res = $pdo->prepare("UPDATE usuario SET token = :token where id = :id");

$res->bindValue(":token", $token);
$res->bindValue(":id", $id);

$res->execute();


echo ($res) ?
json_encode(array("code" => 1, "result"=>"Token alterada com sucesso.")) : 
json_encode(array("code" => 0, "message"=>"Dados incorretos!")) 



   

?>