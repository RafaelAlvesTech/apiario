<?php 

include_once("../conexao.php");
 
 $id           = $_POST['id']; 
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
 







$res = $pdo->prepare("UPDATE apiario
                        SET status = :status,
                        atividade = :atividade,
                        nome = :nome,
                        estrutura = :estrutura,
                        cep = :cep,
                        logradouro = :logradouro,
                        numero = :numero,
                        complemento = :complemento,
                        bairro = :bairro,
                        cidade = :cidade,
                        estado = :estado,
                        responsavel = :responsavel,
                        telefone = :telefone,
                        latitude = :latitude,
                        longitude = :longitude,
                        observacao = :observacao,
                        WHERE id = :id and
                            id_usuario = :id_usuario;
                    ");



    
    $res->bindValue(":id", $id);
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
    $res->bindValue(":latitude", $latitude);
    $res->bindValue(":longitude", $longitude);
        

try {
    $res->execute();
    echo  json_encode(array("code" => 1, "result"=> "result"=>"Apiário alterado com sucesso." ));

} catch(PDOException $e) {
    
    echo json_encode(array("code" => 0, "result"=> "Error: " . $e->getMessage())) ;

}


   

?>