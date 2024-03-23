<?php 

include_once("../conexao.php");


$nome     = $_POST['nome'];
$email    = $_POST['email'];
$senha    = $_POST['senha'];
$telefone = $_POST['telefone'];


$sel = $pdo->query("SELECT * from usuario where email = '$email' ");
$dados = $sel->fetchAll(PDO::FETCH_ASSOC);
$linhas = count($dados);

if($linhas > 0){
   echo(json_encode(array("code" => 0, "result"=>"Email já Cadastrado.")));
    exit();
}

$datahora = date('Y-m-d H:i:s');



$res = $pdo->prepare("INSERT into usuario (nome, email, telefone, senha, status, data_cadastro, data_confirmacao) values (:nome, :email, :telefone, :senha, :status, :data_cadastro, :data_cadastro)");

    $res->bindValue(":nome", $nome);
    $res->bindValue(":email", $email);
    $res->bindValue(":telefone", $telefone);
    $res->bindValue(":senha", $senha);
    $res->bindValue(":status", 'A');
    $res->bindValue(":data_cadastro", $datahora);

    


    $res->execute();


echo ($res) ?
json_encode(array("code" => 1, "result"=>"Usuário cadastrado com sucesso." )) : 
json_encode(array("code" => 0, "result"=>"Dados incorretos!")) 


   

?>