<?php 

include_once("../conexao.php");



$senha = $_POST['senha'];
$id    = $_POST['id'];


if($senha == '' ){
	
  echo(json_encode(array("code" => 0, "result"=>"Preencha os Dados")));
   exit();
}


	$res = $pdo->prepare("UPDATE usuario SET senha = :senha where id = :id");

    $res->bindValue(":senha", $senha);
    $res->bindValue(":id", $id);

    $res->execute();



echo ($res) ?
json_encode(array("code" => 1, "result"=>$"Senha alterada com sucesso.", )) : 
json_encode(array("code" => 0, "message"=>"Dados incorretos!")) 






   

?>