<?php 

$id_usuario     = $_GET['id_usuario']; 
$nome         ='%'.$_GET['nome'].'%'; 

include_once("../conexao.php");


	

$dados = array();

$query = $pdo->query("SELECT *  from apiario where nome like '$nome' or responsavel like '$nome' or id like '$nome'  or observacao like '$nome'  or logradouro like '$nome'  or cidade like '$nome' or telefone like '$nome' or bairro like '$nome' or complemento like '$nome' and id_usuario = '$id_usuario'  order by nome ");

$res = $query->fetchAll(PDO::FETCH_ASSOC);

for ($i=0; $i < count($res); $i++) { 
      foreach ($res[$i] as $key => $value) {}

      	$dados = $res;


}

echo ($res) ?
json_encode(array("code" => 1, "result"=>$dados),JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_NUMERIC_CHECK) : 
json_encode(array("code" => 0, "result"=>"Dados não encontrados!"),JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_NUMERIC_CHECK) 

 ?>