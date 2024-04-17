<?php 

include_once("../conexao.php");

$funcionario = $_GET['funcionario'];


$dados = array();

$query = $pdo->query("SELECT * from tab_fun where fun_id = '$funcionario' ");
$res = $query->fetchAll(PDO::FETCH_ASSOC);

for ($i=0; $i < count($res); $i++) { 
      foreach ($res[$i] as $key => $value) {}

      	$dados = $res;


}

echo ($res) ?
json_encode(array("code" => 1, "result"=>$dados)) : 
json_encode(array("code" => 0, "message"=>"Dados incorretos!")) 

?>