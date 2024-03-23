<?php 

include_once("../conexao.php");

$usuario = $_GET['email'];
$senha   = $_GET['senha'];




$dados = array();



$query = $pdo->query("SELECT *  from usuario where ltrim(rtrim(email)) = '$usuario' ");

$res = $query->fetchAll(PDO::FETCH_ASSOC);



$linhas = count($res);


if($linhas <= 0 ){

        echo(json_encode(array("code" => 0, "result"=>"Usuário não encontrato")));
        exit();
}


   $id          = $res[0]['id'] ;
   $email       = $res[0]['email'] ;
   $Esenha      = $res[0]['senha'] ;
   $nome        = $res[0]['nome'] ; 
   $confirmacao = $res[0]['data_confirmacao'] ;    


if($senha != $Esenha ){

    echo(json_encode(array("code" => 0, "result"=>"Senha não confere!")));
    exit();
}




if( $confirmacao == null ){

    echo(json_encode(array("code" => 0, "result"=>"Usuário não confirmado.")));
    exit();
}


$dados[] = array(
            'id' => $id,    
            'email' => $email,
            'senha' => $senha,
            'nome' => $nome,
            'data_confirmacao' => $confirmacao,
      );    
    





echo ($res) ?
json_encode(array("code" => 1, "result"=>$dados, )) : 
json_encode(array("code" => 0, "result"=>"Dados incorretos!")) 



?>