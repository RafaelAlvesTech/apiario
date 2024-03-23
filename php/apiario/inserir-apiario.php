<?php 

include_once("../conexao.php");
 
 $id_usuario   = $_POST['id_usuario']; 
 $nome        = $_POST['nome'];
 $status        = $_POST['status'];
 $atividade   = $_POST['atividade'];
 $estrutura   = $_POST['estrutura'];
 $logradouro  = $_POST['logradouro'];
 $numero      = $_POST['numero'];
 $complemento = $_POST['complemento'];
 $bairro      = $_POST['bairro'];
 $cidade      = $_POST['cidade'];
 $estado      = $_POST['estado'];
 $cep         = $_POST['cep'];
 $telefone    = $_POST['telefone'];
 $latitude    = $_POST['latitude'];
 $longitude   = $_POST['longitude'];
 $responsavel = $_POST['responsavel'];
 $observacao = $_POST['observacao'];
 




  $datahora = date('Y-m-d H:i:s');  



$res = $pdo->prepare("INSERT INTO apiario (id_usuario,status,atividade,nome,estrutura,cep,logradouro,numero,complemento,bairro,cidade,estado,responsavel,telefone,latitude,longitude,observacao,data) VALUES (:id_usuario,:status,:atividade:,:nome,:estrutura,:cep,:logradouro,:numero,:complemento,:bairro,:cidade,:estado,:responsavel,:telefone,:latitude,:longitude,:observacao,:datahora )");



    
    $res->bindValue(":id_usuario", $id_usuario);
    $res->bindValue(":status", $status);
    $res->bindValue(":atividade", $atividade);
    $res->bindValue(":nome", $nome);
    $res->bindValue(":estrutura", $estrutura);
    $res->bindValue(":logradouro", $logradouro);
    $res->bindValue(":numero", $numero);
    $res->bindValue(":complemento", $complemento);
    $res->bindValue(":bairro", $bairro);
    $res->bindValue(":cidade", $cidade);
    $res->bindValue(":estado", $estado);
    $res->bindValue(":cep", $cep);
    $res->bindValue(":telefone", $telefone);
    $res->bindValue(":responsavel", $responsavel);
    $res->bindValue(":observacao", $observacao);
    $res->bindValue(":datahora", $datahora);
    $res->bindValue(":latitude", $latitude);
    $res->bindValue(":longitude", $longitude);
        
/*
    $res->execute();


echo ($res) ?
json_encode(array("code" => 1, "result"=>"Apiário cadastrado com sucesso." )) : 
json_encode(array("code" => 0, "result"=>"Dados incorretos!")) 

*/

try {
    $res->execute();
    echo  json_encode(array("code" => 1, "result"=> "result"=>"Apiário cadastrado com sucesso." ));

} catch(PDOException $e) {
    //echo $e->getMessage() . PHP_EOL;
    //$connection->rollBack();
    echo json_encode(array("code" => 0, "result"=> "Error: " . $e->getMessage())) ;

}


   

?>